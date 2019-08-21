#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getopt
import os
import pathlib
import re
import shutil
import sys
from os.path import commonprefix, isfile, exists
from string import Template
from urllib.parse import urlsplit
from datetime import datetime
from rdflib import Graph, BNode, RDF, URIRef, OWL, RDFS
from rdflib.namespace import Namespace, NamespaceManager

from modules.filesystem import read_file, write_file

__author__ = "Sascha KAUFMANN"
__copyright__ = "Copyright 2018, NIE-INE"
__credits__ = []
__license__ = "3-Clause BSD License"
__version__ = "0.0.3"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Production"

_KNORA_NS = Namespace("http://www.knora.org/ontology/")
_KBO_NS = Namespace("http://www.knora.org/ontology/knora-base")
KBO_NS = Namespace("http://www.knora.org/ontology/knora-base#")
_DIRSEP = os.sep
_TIMESTAMP = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def is_shortcode(code):
    """
    check it the given code is a shortcode

    :param code:
    :return:
    """
    re_code = re.compile('[0-9A-F]{4}|shared')
    try:
        if re_code.match(code):
            return True
    except TypeError:
        pass
    return False


def split_ns(ns_name):
    """

    :param ns_name:
    :return:
    """

    try:
        components = ns_name.split('#')
        if len(components) == 2:
            return components[0].strip(), components[1].strip()
    except AttributeError:
        pass
    return None, None


def strip_prefix(content, prefix):
    """

    :param content:
    :param prefix:
    :return:
    """
    try:
        if content.startswith(prefix):
            return content[len(prefix):]
    except Exception as e:
        pass

    return content


def import_path(source_path, target_path):
    """

    :param source_path:
    :param target_path:
    :return:
    """
    source_parts = source_path.split('.')
    target_parts = target_path.split('.')

    index = 0
    for (source, target) in zip(source_parts, target_parts):
        if source == target:
            index += 1
        else:
            break
    path = "{}{}".format("." * (len(target_parts) - index),
                         ".".join(target_parts[-(len(target_parts) - index)]))
    return path


def generate_file_comment(comment_type, namespace, name, source=None):
    """

    :param comment_type: kind of file (i.e. class or property)
    :param namespace: namespace
    :param name: class or property name
    :param source: the (turtle) source file
    :return:
    """
    try:
        ns_name = "{}:{}".format(namespace.split('/')[-1], name)
        description = "definition of {} {}".format(comment_type, ns_name)
        description += "\n\ncreated at: {}".format(_TIMESTAMP)
        if source:
            description += "\ncreated from: {}".format(source)
        return description
    except Exception as e:
        print(e)
    return ""


def generate_file_description(desc_type, namespace, name, source=None):
    """

    :param desc_type: description type
    :param namespace:
    :param name:
    :param created:
    :param source:
    :return:
    """
    try:
        ns_name = "{}:{}".format(namespace.split('/')[-1], name)
        description = "definition of {} {}".format(desc_type, ns_name)
        description += "\n\ncreated at: {}".format(_TIMESTAMP)
        if source:
            description += "\ncreated from: {}".format(source)
        return description
    except Exception as e:
        print(e)
    return ""


def generate_file_information(file_information):
    """

    :param file_information:
    :return:
    """

    information = ""
    try:
        components = []
        for key, value in file_information.items():
            components.append("""__{}__ = "{}"\n""".format(key, value))
        if components:
            information = "".join(components)
    except Exception as e:
        print(e)

    return information


def get_namespaces(graph):
    """

    :param graph:
    :return:
    """
    try:
        ns_manager = NamespaceManager(graph=graph)
        return {n[0]: n[1] for n in ns_manager.namespaces()}
    except Exception as e:
        print(e)
    return {}


def graph_classes(graph):
    """

    :param graph:
    :return:
    """
    try:
        return [s for s in graph.subjects(predicate=RDF.type,
                                          object=OWL.Class)]
    except Exception as e:
        print(e)
        class_list = []
    return class_list


def graph_properties(graph):
    """

    :param graph:
    :return:
    """

    try:
        return [s for s in graph.subjects(predicate=RDF.type,
                                          object=OWL.ObjectProperty)]
    except Exception as e:
        print(e)
        property_list = []

    return property_list


def info(lst):
    """

    :param lst:
    :return:
    """
    for item in lst:
        path, name = split_ns(item)
        print("{} -> {} {}".format(item, path.split('/')[-1], name))


def to_class_name(name):
    """

    :param name:
    :return:
    """
    try:
        return "{}{}".format(name[0].upper(), name[1:])
    except (AttributeError, IndexError) as e:
        print(name, e)
    return name


def to_property_name(name):
    """

    :param name:
    :return:
    """
    try:
        return "{}{}".format(name[0].lower(), name[1:])
    except (AttributeError, IndexError) as e:
        print(name, e)
    return name


def get_entries(graph, key):
    """

    :param graph:
    :param key:
    :return:
    """
    entries = []
    try:
        for obj in graph.objects(subject=URIRef(key),
                                 predicate=RDFS.subClassOf):
            if isinstance(obj, BNode):
                for o in graph.objects(subject=obj,
                                       predicate=OWL.onProperty):
                    entries.append(o)
    except Exception as e:
        print(e)
        entries = []

    return entries


def extract_comment(graph, uri):
    """

    :param graph:
    :param uri:
    :return:
    """

    try:
        for comment in graph.objects(subject=URIRef(uri),
                                     predicate=RDFS.comment):
            return str(comment)
    except Exception as e:
        print(e)
    return ""


def extract_label(graph, uri):
    """

    :param graph:
    :param uri:
    :return:
    """

    labels = {}
    try:
        for label in graph.preferredLabel(subject=URIRef(uri)):
            labels[label[1].language] = label[1]
    except Exception as e:
        print(e)
    return labels


def ns_fragement(uri):
    """

    :param uri:
    :return:
    """
    try:
        components = urlsplit(uri)
        namespace = "{}://{}{}".format(components.scheme,
                                       components.netloc,
                                       components.path)
        fragment = components.fragment
    except Exception as e:
        print(e)
        namespace = None
        fragment = None

    return namespace, fragment


def class_dependencies(graph, uri, allowed_ns=None):
    """

    :param graph:
    :param uri:
    :param allowed_ns: list of allowed namespaces
    :return:
    """

    classes = set()
    try:
        for obj in graph.objects(subject=URIRef(uri),
                                 predicate=RDFS.subClassOf):
            str_obj = str(obj)
            if isinstance(obj, URIRef) and str_obj != uri:
                namespace, frag = ns_fragement(str_obj)
                if namespace and frag:
                    if allowed_ns and namespace not in allowed_ns:
                        continue
                    classes.add(str_obj)
    except Exception as e:
        print(e)

    # TODO: the following is just a quick-fix! Make it more intelligent! (SK_20180302)
    try:
        classes.remove('http://www.knora.org/ontology/knora-base#StillImageRepresentation')
        if not classes:
            classes.add('http://www.knora.org/ontology/knora-base#Resource')
    except KeyError:
        pass

    return classes


def property_dependencies(graph, uri):
    """

    :param graph:
    :param uri:
    :return:
    """

    properties = set()
    try:
        for obj in graph.objects(subject=URIRef(uri),
                                 predicate=RDFS.subClassOf):
            try:
                for obj in graph.objects(subject=obj,
                                         predicate=OWL.onProperty):
                    properties.add(str(obj))
            except Exception as e:
                print(e)

        # TODO: the following is just a quick-fix! Make it more 'intelligent'! (SK_20180302)
        value_list = [uri for uri in properties if uri.endswith('Value')]
        for value in value_list:
            properties.discard(value) if value[:-5] in properties else None

    except Exception as e:
        print(e)

    return properties


def prop_coordinates(graph, uri):
    """

    :param graph:
    :param uri:
    :return:
    """

    coordinates = {}

    if uri in graph_properties(graph):
        try:
            coordinates['subPropertyOf'] = set(obj for obj in graph.objects(subject=URIRef(uri), predicate=RDFS.subPropertyOf))
            coordinates['subjectClassConstraint'] = set(obj for obj in graph.objects(subject=URIRef(uri), predicate=KBO_NS.subjectClassConstraint))
            coordinates['objectClassConstraint'] = set(obj for obj in graph.objects(subject=URIRef(uri), predicate=KBO_NS.objectClassConstraint))
        except Exception as e:
            pass

    return coordinates


def property_class_dependencies(graph, uri, allowed_ns=None):
    """

    :param graph:
    :param uri:
    :param allowed_ns: list of allowed namespaces
    :return:
    """

    classes = set()
    try:
        a = prop_coordinates(graph=graph, uri=uri)
        # filter LinkValues
        if URIRef('{}LinkValue'.format(KBO_NS)) in a['objectClassConstraint']:
            return classes

        elif str(uri).endswith("Value"):
            subject = URIRef(uri)
            predicate = KBO_NS.objectClassConstraint
            for obj in graph.objects(subject=subject,
                                     predicate=predicate):
                if str(obj) == '{}LinkValue'.format(KBO_NS):
                    return classes

        for obj in graph.objects(subject=URIRef(uri),
                                 predicate=RDFS.subPropertyOf):

            if isinstance(obj, URIRef):
                str_obj = str(obj)
                if str_obj == 'http://www.knora.org/ontology/knora-base#hasValue':
                    for (p, o) in graph.predicate_objects(subject=URIRef(uri)):
                        if str(p) == "http://www.knora.org/ontology/knora-base#objectClassConstraint":
                            str_o = str(o)
                            if str_o != uri:
                                namespace, frag = ns_fragement(str_o)
                                if namespace and frag:
                                    if allowed_ns and namespace not in allowed_ns:
                                        continue
                                    classes.add(str_o)
                                    break
                elif str_obj != uri:
                    namespace, frag = ns_fragement(str_obj)
                    if namespace and frag:
                        if allowed_ns and namespace not in allowed_ns:
                            continue
                        classes.add(str_obj)

    except Exception as e:
        print(e)

    return classes


def dir_to_pypath(directory):
    """

    :param directory:
    :return:
    """
    try:
        return directory.replace(_DIRSEP, '.')
    except AttributeError as e:
        print(e)

    return None


def generate_alias(source):
    """

    :param source:
    :return:
    """

    try:
        return "".join([item[:min(3, len(source))] for item in source.split('/')])
    except (AttributeError, IndexError) as e:
        print(source, e)
    return ""


def generate_import(source, target):
    """

    :param source: source_path, where the source file is located
    :param target: target_path, where the file that should be included,
                   is located
    :return:
    """

    try:
        source_parts = source.lstrip(_DIRSEP).split(_DIRSEP)
        target_parts = target.lstrip(_DIRSEP).split(_DIRSEP)
        common_parts = commonprefix([source_parts, target_parts])
        if len(target_parts) == len(common_parts) == len(source_parts):
            return ""
        upwards = len(source_parts) - len(common_parts) + 1
        downwards = len(target_parts) - len(common_parts)
        return "{}{}".format("." * upwards,
                             ".".join(target_parts[len(target_parts) - downwards:]))
    except (AttributeError, Exception) as e:
        print(source, target)
        print(e)

    return None


def create_classes(template_file, graph, mappings, src_filename):
    """

    :param template_file:
    :param graph:
    :param mappings:
    :param filename: name of the (turtle) source file
    :return:
    """

    for class_uri in graph_classes(graph=graph):
        known_namespaces = ""
        argument = ""
        argument_comment = ""
        class_internal_vars = ""
        class_properties = ""
        class_properties_types = ""

        class_ns, class_fragment = ns_fragement(class_uri)
        class_dir = "{}{ps}classes".format(mappings[class_ns]['path'],
                                           ps=_DIRSEP)

        cls_dependencies = class_dependencies(graph=graph,
                                              uri=class_uri,
                                              allowed_ns=known_namespaces)
        prop_dependencies = property_dependencies(graph=graph,
                                                  uri=class_uri)

        if 'http://www.knora.org/ontology/knora-base#hasStillImageFileValue' in prop_dependencies:
            class_internal_vars = "        self._image_file = None\n"
            prop_dependencies.discard('http://www.knora.org/ontology/knora-base#hasStillImageFileValue')


        # $class_name
        class_name = to_class_name(class_fragment)

        # $general_comment
        general_comment = generate_file_comment('class',
                                                namespace=class_ns,
                                                name=class_name,
                                                source=src_filename)

        # $class_comment
        class_comment = extract_comment(graph, uri=class_uri)
        if class_comment:
            class_comment = "    {}".format(class_comment)
        i = 1
        while len(class_comment) > i * 80:
            idx = class_comment.rfind(' ', (i - 1) * 80, i * 80)
            class_comment = class_comment[:idx] + "\n    " + class_comment[idx + 1:]
            i += 1
        class_labels = extract_label(graph, uri=class_uri)
        if class_labels:
            labels = []
            for key in sorted(class_labels):
                labels.append('{} ({})'.format(class_labels[key], key))
            plural = "s" if len(labels) > 1 else ""
            class_comment = "{}\n\n    Label{}: {}".format(class_comment,
                                                           plural,
                                                           " / ".join(labels))

        # $sub_class_of
        cls_data = {}
        for dependency in cls_dependencies:
            ns, dep_name = ns_fragement(dependency)
            if ns not in mappings:
                continue
            dep_name = to_class_name(dep_name)
            alias = None
            if dep_name == class_name or dep_name in cls_data:
                alias = "{}_{}".format(mappings[ns]['name'], dep_name)
            if dep_name not in cls_data:
                cls_data[dep_name] = []
            cls_data[dep_name].append((ns, alias))

        tmp = []
        modules_to_import = []
        for key, value in cls_data.items():
            for item in value:
                cur_path = generate_import("{}{ps}classes".format(mappings[class_ns]['rel_path'], ps=_DIRSEP),
                                           "{}{ps}classes".format(mappings[item[0]]['rel_path'], ps=_DIRSEP))
                import_str = "from {}.{} import {}".format(cur_path, key, to_class_name(key))
                if item[1]:
                    tmp.append(item[1])
                    import_str = "{} as {}".format(import_str, item[1])
                else:
                    tmp.append(key)
                modules_to_import.append(import_str)
        sub_class_of = ", ".join(tmp) if tmp else ''

        prop_data = {}
        for dependency in prop_dependencies:
            ns, dep_name = ns_fragement(dependency)
            dep_name = to_property_name(dep_name)
            if dep_name not in prop_data:
                prop_data[dep_name] = []
            ns_prefix = mappings[ns]['name_ns']
            prop_data[dep_name].append((ns, ns_prefix))

        arg = []
        arg_comment = []
        cls_properties = []
        cls_properties_types = []
        for key, value in prop_data.items():
            for item in value:
                key_prop = key
                key_class = to_class_name(key)
                cur_path = generate_import("{}{ps}classes".format(mappings[class_ns]['rel_path'], ps=_DIRSEP),
                                           "{}{ps}properties".format(mappings[item[0]]['rel_path'], ps=_DIRSEP))
                import_str = "from {}.{} import {}".format(cur_path,
                                                           key_prop,
                                                           key_class)

                key_prop = '{}_{}'.format(item[1], key_prop)
                key_class = '{}_{}'.format(item[1], key_class)
                import_str = "{} as {}".format(import_str, key_class)

                arg.append(key_prop)
                arg_comment.append("{}:param {}:".format(" " * 8, key_prop))
                modules_to_import.append(import_str)
                cls_properties.append("{}self.{} = {}".format(" " * 8, key_prop, key_prop))
                cls_properties_types.append("{}self._{} = {}".format(" " * 8, key_prop, key_class))

        if arg:
            arg_init = ["{}=None".format(item) for item in arg]
            argument = " {},".format(", ".join(arg_init))
            argument_comment = "\n{}".format("\n".join(arg_comment))
            class_properties = "\n{}\n".format("\n".join(cls_properties))
            comment = "        # data type"
            if len(class_properties_types) > 1:
                comment = "{}s".format(comment)
            class_properties_types = "{}\n{}".format(comment, "\n".join(cls_properties_types))

        # read template and generate file
        module_import = "\n".join(modules_to_import)

        class_template = read_template(template_file)
        content = class_template.substitute(module_import=module_import,
                                            general_comment=general_comment,
                                            class_name=class_name,
                                            sub_class_of=sub_class_of,
                                            class_comment=class_comment,
                                            argument=argument,
                                            argument_comment=argument_comment,
                                            namespace=class_ns,
                                            class_internal_vars=class_internal_vars,
                                            class_properties=class_properties,
                                            class_properties_types=class_properties_types)
        filename = "{}{ps}{}.py".format(class_dir, class_name, ps=_DIRSEP)
        write_file(filename=filename, content=content)


def create_properties(template_file, graph, mappings, src_filename):
    """

    :param template_file:
    :param graph:
    :param mappings:
    :param src_filename:
    :return:
    """

    for property_uri in graph_properties(graph=graph):
        if str(property_uri).endswith('Value'):
            if URIRef(str(property_uri)[:-5]) in graph_properties(graph=graph):
                continue

        known_namespaces = ''
        property_internal_vars = ''

        property_ns, property_fragment = ns_fragement(property_uri)
        property_dir = "{}{ps}properties".format(mappings[property_ns]['path'],
                                                 ps=_DIRSEP)

        cls_dependencies = property_class_dependencies(graph=graph,
                                                       uri=property_uri,
                                                       allowed_ns=known_namespaces)

        # $class_name
        class_name = to_class_name(property_fragment)
        property_name = property_fragment

        # $general_comment
        general_comment = generate_file_comment('property',
                                                namespace=property_ns,
                                                name=class_name,
                                                source=src_filename)

        # $class_comment
        class_comment = extract_comment(graph, uri=property_uri)

        # $sub_class_of
        cls_data = {}
        for dependency in cls_dependencies:
            ns, dep_name = ns_fragement(dependency)
            if ns not in mappings:
                continue
            dep_name = to_class_name(dep_name)
            alias = None
            if dep_name == class_name or dep_name in cls_data:
                alias = "{}_{}".format(mappings[ns]['name'], dep_name)
            if dep_name not in cls_data:
                cls_data[dep_name] = []
            cls_data[dep_name].append((ns, alias))

        if URIRef("{}Value".format(str(property_uri))) in graph_properties(graph=graph):
            coordinates = prop_coordinates(graph=graph, uri=property_uri)
            try:
                obj_class_constraint = str(coordinates['objectClassConstraint'].pop())
                property_internal_vars = '        self._objectClassConstraint = "{}"'.format(obj_class_constraint)
            except Exception as e:
                print(e)

        modules_to_import = []
        parent_properties = []
        for key, value in cls_data.items():
            for item in value:
                cur_path = generate_import("{}{ps}properties".format(mappings[property_ns]['rel_path'], ps=_DIRSEP),
                                           "{}{ps}properties".format(mappings[item[0]]['rel_path'], ps=_DIRSEP))
                import_str = "from {}.{} import {}".format(cur_path, to_property_name(key), to_class_name(key))
                if item[1]:
                    parent_properties.append(item[1])
                    modules_to_import.append("{} as {}".format(import_str,
                                                               item[1]))
                else:
                    parent_properties.append(key)
                    modules_to_import.append(import_str)
        sub_property_of = ",".join(parent_properties)

        # read template and generate file
        module_import = "\n".join(modules_to_import)

        class_template = read_template(template_file)
        content = class_template.substitute(module_import=module_import,
                                            general_comment=general_comment,
                                            class_name=class_name,
                                            sub_property_of=sub_property_of,
                                            class_comment=class_comment,
                                            namespace=property_ns,
                                            name=property_name,
                                            property_internal_vars=property_internal_vars)
        filename = "{}{ps}{}.py".format(property_dir, to_property_name(property_name), ps=_DIRSEP)
        write_file(filename=filename, content=content)


def get_path(namespace):
    """

    :param namespace:
    :return:
    """

    return strip_prefix(namespace, 'http://').replace('.', '_').replace('-', '_')


def read_template(filename):
    """

    :param filename:
    :return:
    """

    try:
        content = read_file(filename=filename)
        template = Template(content)
    except Exception as e:
        print(e)
        template = None

    return template


def create_dirstruct(home_dir, namespace):
    """

    :param home_dir:
    :param namespace:
    :return:
    """

    ns_path = get_path(namespace=namespace)
    dir_struct = "ontologies{}{}".format(_DIRSEP, ns_path)

    cur_dir = home_dir + '{}{}'.format(_DIRSEP, dir_struct)
    pathlib.Path(cur_dir).mkdir(parents=True, exist_ok=True)

    for item in ['classes', 'properties']:
        current_dir = '{}{}{}'.format(cur_dir, _DIRSEP, item)
        pathlib.Path(current_dir).mkdir(parents=True, exist_ok=True)

    filename = "{}{ps}templates{ps}__init__.tpl".format(home_dir, ps=_DIRSEP)
    template = read_template(filename=filename)
    content = template.substitute(namespace=namespace)
    filename = "{}{}__init__.py".format(cur_dir, _DIRSEP)
    print(filename, content)
    write_file(filename=filename, content=content)

    return cur_dir


def create_kbo(template_dir, target_dir):
    """

    :param template_dir: directory, where we find the templates
    :param target_dir: directory, from where we derive the files' final
                       destination(s)
    :return:
    """

    for context in ['classes', 'properties']:
        context_templates = "{}/{}".format(template_dir, context)
        context_directory = "{}/{}".format(target_dir, context)
        for (_, _, filenames) in os.walk(context_templates):
            for filename in filenames:
                if filename.endswith('.py'):
                    shutil.copy(src="{}/{}".format(context_templates, filename),
                                dst="{}/{}".format(context_directory, filename))

    return


def create_utils(source_dir, target_dir):
    """

    :param source_dir: directory, where we find the templates
    :param target_dir: directory, from where we derive the files' final
                       destination(s)
    :return:
    """

    pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)
    for (_, _, filenames) in os.walk(source_dir):
        for filename in filenames:
            shutil.copy(src = "{}/{}".format(source_dir, filename),
                        dst = "{}/{}".format(target_dir, filename))

    return


def determine_namespaces(files):
    """

    :param files: list of files, where each of it contains information about
                  an ontology
    :return:
    """

    namespaces = set()
    for file in files:
        try:
            graph = Graph().parse(file, format="n3")
        except Exception as e:
            print("An error occurred while building the graph from file '{}'".format(file))
            print("({})".format(e))
            continue
        classes = graph_classes(graph)
        for cls in classes:
            components = urlsplit(cls)
            namespaces.add("{}://{}{}".format(components.scheme,
                                              components.netloc,
                                              components.path))
        properties = graph_properties(graph)
        for cur_property in properties:
            components = urlsplit(cur_property)
            namespaces.add("{}://{}{}".format(components.scheme,
                                              components.netloc,
                                              components.path))
    if namespaces:
        namespaces.add('http://www.knora.org/ontology/knora-base')
    return list(namespaces)


def namespace_file_structure(namespaces, target_dir):
    """

    :param namespaces: list of namespaces to convert into a file structure
    :return:
    """

    mapping = {}
    for namespace in namespaces:
        tmp_path = namespace.replace('://', '/').replace('.', '_').replace('-', '_')
        mapping[namespace] = tmp_path

    min_fs = minimize_file_structure(mapping)
    ns_mapping = {}
    for key, value in min_fs.items():
        path = value
        path_elems = path.split(_DIRSEP)
        cur_dir = path_elems[-1]
        short_code = None
        try:
            short_code = path_elems[-2]
            if is_shortcode(short_code):
                del path_elems[-2]
                path = _DIRSEP.join(path_elems)
        except IndexError:
            pass

        name_ns_parts = cur_dir.split('_')
        if len(name_ns_parts) > 1:
            cc_parts = [to_class_name(part) for part in name_ns_parts[1:]]
            name_ns_parts = [name_ns_parts[0]] + cc_parts
        name_ns = "".join(name_ns_parts)

        scode = short_code if short_code else cur_dir
        project_id = "http://rdfh.ch/projects/{}".format(scode)

        ns_mapping[key] = {'path': '{}{}'.format(target_dir, path),
                           'rel_path': path,
                           'name': cur_dir,
                           'name_ns': name_ns,
                           'short_code': short_code,
                           'project_id': project_id}

    return ns_mapping


def minimize_file_structure(ns_fs_mapping):
    """

    :param ns_fs_mapping: dictionary with namespace -> file structure mapping
    :return:
    """

    common_prefix_len = len(commonprefix([item for key, item in ns_fs_mapping.items()]))

    if common_prefix_len:
        for key, item in ns_fs_mapping.items():
            fs = item[common_prefix_len:]
            if not fs.startswith(_DIRSEP):
                fs = "{}{}".format(_DIRSEP, fs)
            ns_fs_mapping[key] = fs

    return ns_fs_mapping


def create_ns_structure(ns_structure):
    """

    :param ns_structure: list of path names that leading to an ontologies
                         "home directory"
    :return:
    """

    for key, value in ns_structure.items():
        for directory in ['classes', 'properties']:
            current_dir = "{}{}{}".format(value['path'], _DIRSEP, directory)
            pathlib.Path(current_dir).mkdir(parents=True, exist_ok=True)

        write_file(filename="{}{}__init__.py".format(value['path'], _DIRSEP),
                   content="ONTOLOGY_NS = '{}'\nPROJECT_ID = '{}'\n".format(key, value['project_id']))

    return


def extract_files_to_process(arguments):
    """

    :param arguments: arguments (files)
    :return: list with filenames that we want process
    """
    files_to_process = set()
    for arg in arguments:
        if not exists(arg):
            print("'{}' does not exist!".format(arg))
            continue
        if isfile(arg):
            if not arg.startswith('.'):
                files_to_process.add(os.path.abspath(arg))
            continue
        for (dir_path, _, file_names) in os.walk(arg):
            for file_name in file_names:
                if not file_name.startswith('.') and file_name.endswith('.ttl'):
                    data = {'dir_path': dir_path,
                            'file_name': file_name,
                            'ps': _DIRSEP}
                    files_to_process.add(os.path.abspath("{dir_path}{ps}{file_name}".format(**data)))
    return list(files_to_process)


def usage():
    """
    prints information how to use this script (parameters)

    :return:
    """

    print('ttl2py.py [-t <target_dir>] <file|dir> ...')


def main(argv):
    """

    :return:
    """

    target_dir = ".{}ontologies".format(_DIRSEP)
    try:
        opts, args = getopt.getopt(argv, "ht:", ["help", "target="])
    except getopt.GetoptError:
        usage()
        return 2

    for opt, arg in opts:
        if opt in ('-h', '--help') or not args:
            usage()
            return 0
        elif opt in ('-t', '--target'):
            target_dir = arg
    if not args:
        usage()
        return 2

    files_to_process = extract_files_to_process(args)
    if not files_to_process:
        return 2

    home_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = "{}{ps}templates".format(home_dir, ps=_DIRSEP)

    if not target_dir.startswith(_DIRSEP):
        data = {'home_dir': home_dir, 'target_dir': target_dir, 'ps': _DIRSEP}
        target_dir = os.path.realpath("{home_dir}{ps}{target_dir}".format(**data))
        if target_dir == home_dir:
            target_dir = "{home_dir}{ps}ontologies".format(**data)
    if os.path.isfile(target_dir):
        print("There is already a file '{}'!".format(target_dir))
        return 2

    namespaces = determine_namespaces(files_to_process)
    ns_fs_mappings = namespace_file_structure(namespaces, target_dir)

    create_ns_structure(ns_fs_mappings)

    create_utils(source_dir="{}{}_utils".format(template_dir, _DIRSEP),
                 target_dir="{}{}_utils".format(target_dir, _DIRSEP))

    target_dir = ns_fs_mappings['http://www.knora.org/ontology/knora-base']['path']
    create_kbo(template_dir=template_dir,
               target_dir=target_dir)

    data = {'template_dir': template_dir, 'ps': _DIRSEP}
    class_template = "{template_dir}{ps}classes{ps}_Resource.tpl".format(**data)
    property_template = "{template_dir}{ps}properties{ps}_property.tpl".format(**data)

    for file in files_to_process:
        try:
            graph = Graph().parse(file, format="n3")
        except Exception as e:
            print("An error occurred, while building the graph from file '{}'".format(file))
            print("({})".format(e))
            continue

        src_filename = file.split(_DIRSEP)[-1]
        create_classes(template_file=class_template,
                       graph=graph,
                       mappings=ns_fs_mappings,
                       src_filename=src_filename)
        create_properties(template_file=property_template,
                          graph=graph,
                          mappings=ns_fs_mappings,
                          src_filename=src_filename)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
