#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import os
import pathlib
import re
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
__version__ = "0.0.2"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Production"


header_information = None

_KNORA_NS = Namespace("http://www.knora.org/ontology/")
_KBO_NS = Namespace("http://www.knora.org/ontology/knora-base")
_DIRSEP = os.sep
_TIMESTAMP = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def is_shortcode(code):
    """
    check it the given code is a shortcode

    :param code:
    :return:
    """
    p = re.compile('[0-9A-F]{4}')
    try:
        if p.match(code):
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
    path = "{}{}".format("."*(len(target_parts)-index),
                         ".".join(target_parts[-(len(target_parts)-index)]))
    return path


def file_comment(comment_type, ns, name, source=None):
    """

    :param comment_type: kind of file (i.e. class or property)
    :param ns: namespace
    :param name: class or property name
    :param source: the (turtle) source file
    :return:
    """
    try:
        ns_name = "{}:{}".format(ns.split('/')[-1], name)
        description = "definition of {} {}".format(comment_type, ns_name)
        description += "\n\ncreated at: {}".format(_TIMESTAMP)
        if source:
            description += "\ncreated from: {}".format(source)
        return description
    except Exception as e:
        print(e)
    return ""


def generate_file_description(desc_type, ns, name, source=None):
    """

    :param desc_type:
    :param ns:
    :param name:
    :param created:
    :param source:
    :return:
    """
    try:
        ns_name = "{}:{}".format(ns.split('/')[-1], name)
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
    except AttributeError as e:
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
    ns = None,
    fragment = None
    try:
        components = urlsplit(uri)
        ns = "{}://{}{}".format(components.scheme,
                                components.netloc,
                                components.path)
        fragment = components.fragment
    except Exception as e:
        print(e)

    return ns, fragment


def class_dependencies(graph, uri, allowed_ns=None):
    """

    :param graph:
    :param uri:
    :param allowed_ns: list of allowed namespaces
    :return:
    """

    classes = set()
    try:
        for o in graph.objects(subject=URIRef(uri),
                               predicate=RDFS.subClassOf):
            str_o = str(o)
            if isinstance(o, URIRef) and str_o != uri:
                ns, frag = ns_fragement(str_o)
                if ns and frag:
                    if allowed_ns and ns not in allowed_ns:
                        continue
                    classes.add(str_o)
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
        tmp_properties = set()
        for obj in graph.objects(subject=URIRef(uri),
                                 predicate=RDFS.subClassOf):
            # if isinstance(obj, BNode):
            try:
                for o in graph.objects(subject=obj, predicate=OWL.onProperty):
                    tmp_properties.add(str(o))
            except Exception as e:
                print(e)
        properties = {item for item in tmp_properties if not item.endswith('Value') or item[:-5] not in tmp_properties}

        # TODO: the following is just a quick-fix! Make it more 'intelligent'! (SK_20180302)
        properties.discard('http://www.knora.org/ontology/knora-base#hasStillImageFileValue')

    except Exception as e:
        print(e)

    return properties


def property_class_dependencies(graph, uri, allowed_ns=None):
    """

    :param graph:
    :param uri:
    :param allowed_ns: list of allowed namespaces
    :return:
    """

    classes = set()
    try:
        for o in graph.objects(subject=URIRef(uri),
                               predicate=RDFS.subPropertyOf):

            if isinstance(o, URIRef):
                str_o = str(o)
                if str_o == 'http://www.knora.org/ontology/knora-base#hasValue':
                    for (p , o) in graph.predicate_objects(subject=URIRef(uri)):
                        b = 0
                        if str(p) == "http://www.knora.org/ontology/knora-base#objectClassConstraint":
                            str_o = str(o)
                            if str_o != uri:
                                ns, frag = ns_fragement(str_o)
                                if ns and frag:
                                    if allowed_ns and ns not in allowed_ns:
                                        continue
                                    classes.add(str_o)
                                    break
                elif str_o != uri:
                    ns, frag = ns_fragement(str_o)
                    if ns and frag:
                        if allowed_ns and ns not in allowed_ns:
                            continue
                        classes.add(str_o)

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
        return "{}{}".format("."*upwards,
                             ".".join(target_parts[len(target_parts)-downwards:]))
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
        module_import = ""
        general_comment = ""
        class_name = ""
        sub_class_of = ""
        class_comment = ""
        argument = ""
        argument_comment = ""
        namespace = ""
        class_properties = ""

        class_ns, class_fragment = ns_fragement(class_uri)
        class_dir = "{}{ps}classes".format(mappings[class_ns]['path'],
                                           ps=_DIRSEP)

        cls_dependencies = class_dependencies(graph=graph,
                                              uri=class_uri,
                                              allowed_ns=known_namespaces)
        prop_dependencies = property_dependencies(graph=graph,
                                                  uri=class_uri)

        # $class_name
        class_name = to_class_name(class_fragment)

        # $general_comment
        general_comment = file_comment('class',
                                       ns=class_ns,
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
            class_comment = "{}\n\n    Label{}: {}".format(class_comment, plural, " / ".join(labels))

        # $module_import

        # $sub_class_of
        cls_data = {}
        for dependency in cls_dependencies:
            ns, dep_name = ns_fragement(dependency)
            if ns not in mappings:
                continue
            dep_name = to_class_name(dep_name)
            alias = None
            if dep_name == class_name or dep_name in cls_data:
                # alias = "{}_{}".format(generate_alias(mappings[ns]['rel_path']), dep_name)
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
                    modules_to_import.append("{} as {}".format(import_str, item[1]))
                else:
                    tmp.append(key)
                    modules_to_import.append(import_str)
        sub_class_of = ", ".join(tmp) if tmp else ''

        prop_data = {}
        prop_external_dependencies = set()
        for dependency in prop_dependencies:
            ns, dep_name = ns_fragement(dependency)
            if ns != class_ns:
                prop_external_dependencies.add(dependency)
                continue
            dep_name = to_property_name(dep_name)
            if dep_name not in prop_data:
                prop_data[dep_name] = []
            prop_data[dep_name].append((ns, None))
        for dependency in prop_external_dependencies:
            ns, dep_name = ns_fragement(dependency)
            dep_name = to_property_name(dep_name)
            ns_prefix = None
            if dep_name == class_name or dep_name in prop_data:
                ns_prefix = mappings[ns]['name']
            if dep_name not in prop_data:
                prop_data[dep_name] = []
            prop_data[dep_name].append((ns, ns_prefix))

        arg = []
        arg_comment = []
        cls_properties = []
        for key, value in prop_data.items():
            for item in value:
                cur_path = generate_import("{}{ps}classes".format(mappings[class_ns]['rel_path'], ps=_DIRSEP),
                                           "{}{ps}properties".format(mappings[item[0]]['rel_path'], ps=_DIRSEP))
                import_str = "from {}.{} import {}".format(cur_path, key, to_class_name(key))

                if item[1]:
                    key_prop = '{}_{}'.format(item[1], key)
                    key_class = '{}_{}'.format(item[1], to_class_name(key))
                    arg.append(key_prop)
                    arg_comment.append("{}:param {}:".format(" " * 8, key_prop))
                    modules_to_import.append("{} as {}".format(import_str, key_class))
                    cls_properties.append("{}self.{} = {}({})".format(" " * 8, key_prop, key_class, key_prop))
                else:
                    arg.append(key)
                    arg_comment.append("{}:param {}:".format(" " * 8, key))
                    tmp.append(key)
                    modules_to_import.append(import_str)
                    cls_properties.append("{}self.{} = {}({})".format(" "*8, key, to_class_name(key), key))

        if arg:
            arg_init = ["{}=None".format(item) for item in arg]
            argument = " {},".format(", ".join(arg_init))
            argument_comment = "\n{}".format("\n".join(arg_comment))
            class_properties = "\n{}\n".format("\n".join(cls_properties))

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
                                            class_properties=class_properties)
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
        known_namespaces = ''
        module_import = ''
        general_comment = ''
        class_name = ''
        sub_property_of = ''
        class_comment = ''
        property_ns = ''
        property_name = ''

        property_ns, property_fragment = ns_fragement(property_uri)
        property_dir = "{}{ps}properties".format(mappings[property_ns]['path'], ps=_DIRSEP)

        cls_dependencies = property_class_dependencies(graph=graph, uri=property_uri, allowed_ns=known_namespaces)

        # $class_name
        class_name = to_class_name(property_fragment)
        property_name = property_fragment

        # $general_comment
        general_comment = file_comment('property', ns=property_ns, name=class_name, source=src_filename)

        # $class_comment
        class_comment = extract_comment(graph, uri=property_uri)

        # $module_import

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

        modules_to_import = []
        parent_properties = []
        for key, value in cls_data.items():
            for item in value:
                cur_path = generate_import("{}{ps}properties".format(mappings[property_ns]['rel_path'], ps=_DIRSEP),
                                           "{}{ps}properties".format(mappings[item[0]]['rel_path'], ps=_DIRSEP))
                import_str = "from {}.{} import {}".format(cur_path, to_property_name(key), to_class_name(key))
                if item[1]:
                    parent_properties.append(item[1])
                    modules_to_import.append("{} as {}".format(import_str, item[1]))
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
                                            name=property_name)
        filename = "{}{ps}{}.py".format(property_dir, property_name, ps=_DIRSEP)
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


def create_dirstruct(home_dir, ns):
    """

    :param home_dir:
    :param ns:
    :return:
    """

    ns_path = get_path(namespace=ns)
    dir_struct = "ontologies{}{}".format(_DIRSEP, ns_path)

    cur_dir = home_dir + '{}{}'.format(_DIRSEP, dir_struct)
    pathlib.Path(cur_dir).mkdir(parents=True, exist_ok=True)

    for item in ['classes', 'properties']:
        current_dir = '{}{}{}'.format(cur_dir, _DIRSEP, item)
        pathlib.Path(current_dir).mkdir(parents=True, exist_ok=True)

    filename = "{}{ps}templates{ps}__init__.tpl".format(home_dir, ps=_DIRSEP)
    template = read_template(filename=filename)
    content = template.substitute(namespace=ns)
    filename="{}{}__init__.py".format(cur_dir, _DIRSEP)
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
        for (dirpath, dirnames, filenames) in os.walk(context_templates):
            for filename in filenames:
                if filename.startswith('kbo_') and filename.endswith('.tpl'):
                    target_file = "{}/{}.py".format(context_directory,
                                                    filename[4:-4])
                    template = read_template(filename="{}/{}".format(context_templates, filename))
                    content = template.substitute()
                    write_file(filename=target_file, content=content)
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
            namespaces.add("{}://{}{}".format(components.scheme, components.netloc, components.path))
        properties = graph_properties(graph)
        for cur_property in properties:
            components = urlsplit(cur_property)
            namespaces.add("{}://{}{}".format(components.scheme, components.netloc, components.path))
    namespaces.add('http://www.knora.org/ontology/knora-base') if namespaces else None
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

        if short_code:
            project_id = "http://rdfh.ch/projects/{}".format(short_code)
        else:
            project_id = "http://rdfh.ch/projects/{}".format(cur_dir)

        ns_mapping[key] = {'path': '{}{}'.format(target_dir, path),
                           'rel_path': path,
                           'name': cur_dir,
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

    files_to_process = set()
    for arg in args:
        if not exists(arg):
            print("'{}' does not exist!".format(arg))
            continue
        if isfile(arg):
            if not arg.startswith('.'):
                files_to_process.add(os.path.abspath(arg))
            continue
        for (dir_path, dir_names, file_names) in os.walk(arg):
            for file_name in file_names:
                if not file_name.startswith('.'):
                    data = {'dir_path': dir_path,
                            'file_name': file_name,
                            'ps': _DIRSEP}
                    files_to_process.add(os.path.abspath("{dir_path}{ps}{file_name}".format(**data)))
    files_to_process = list(files_to_process)
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

#    fs_ns_structure = ["{}{}".format(target_dir, value) for key, value in ns_fs_mappings.items()]
    create_ns_structure(ns_fs_mappings)

    create_kbo(template_dir=template_dir,
               target_dir=ns_fs_mappings['http://www.knora.org/ontology/knora-base']['path'])

    data = {'template_dir': template_dir, 'ps': _DIRSEP}
    class_template = "{template_dir}{ps}classes{ps}Resource.tpl".format(**data)
    property_template = "{template_dir}{ps}properties{ps}property.tpl".format(**data)

    for file in files_to_process:
        try:
            graph = Graph().parse(file, format="n3")
        except Exception as e:
            print("An error occurred, while building the graph from file '{}'".format(file))
            print("({})".format(e))
            continue

        # ns = get_namespaces(graph=graph)
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
