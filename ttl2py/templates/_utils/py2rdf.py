#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from collections import OrderedDict, namedtuple

try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                except ImportError:
                    print("Failed to import ElementTree from any known place")


_xmlns_rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
_xmlns_rdfs = "http://www.w3.org/2000/01/rdf-schema#"
_xmlns_knora_base = "http://www.knora.org/ontology/knora-base#"
_xmlns_TODO = "todo#"
_tag_tpl = "{{{:s}}}{:s}"
_onto_tpl = "{:s}#{:s}"
_knoraType_to_xsd = {'richtext_value': 'http://www.w3.org/2001/XMLSchema#string',
                     'int_value': 'http://www.w3.org/2001/XMLSchema#integer',
                     'decimal_value': 'http://www.w3.org/2001/XMLSchema#decimal',
                     'uri_value': 'http://www.w3.org/2001/XMLSchema#anyURI',
                     'date_value': 'http://www.w3.org/2001/XMLSchema#dateTime',  # TODO: clean up calendar system
                     'color_value': 'http://www.w3.org/2001/XMLSchema#string',  # TODO
                     'hlist_value': 'http://www.w3.org/2001/XMLSchema#string',  # TODO
                     'interval_value': 'http://www.w3.org/2001/XMLSchema#string'}  # TODO


def _sanitize_id(text):
    """

    :param text:
    :return:
    """

    return "_".join(text.split())


def __xml_struct__(resource_set):
    """

    :param resource_set: a set that contains the resource to create
    :return: string that contains the created xml-description to be used with knora
    """

    nsmap = {'rdf': _xmlns_rdf,
             'rdfs': _xmlns_rdfs}

    namespaces = {}
    resource_info = {}

    try:
        for entry in resource_set:

            # get metadata about resources to process properties
            resource = entry[0] # resource - as opposed to client id
            resource_ns = resource._namespace # full namespace of resource (as in ontology)

            if resource_ns not in namespaces:

                # collect missing namespaces
                xmlns_prefix = resource_ns.split('/')[-1] # xml namespace prefix of resource
                namespaces[resource_ns] = (xmlns_prefix, resource_ns + '#') # add to namespaces
                nsmap[xmlns_prefix] = resource_ns + '#' # add to map for xml creation

            resource_key = "{}:{}".format(namespaces[resource_ns][0], resource._name)
            if resource_key not in resource_info:
                properties = {}
                for attr, value in resource.__dict__.items():

                    # process properties
                    if attr.startswith('_') or attr == 'seqnum':
                        nsmap['knoraBase'] = _xmlns_knora_base
                        continue
                    try:

                        # collect missing namespaces
                        prop_type = resource.__dict__.get("_{}".format(attr))
                        prop_dummy = prop_type(None)
                        property_ns = prop_dummy._namespace # namespace of property (as in ontology)
                        xmlns_prefix = property_ns.split('/')[-1] # xml namespace prefix of property
                        namespaces[property_ns] = (xmlns_prefix, property_ns + '#') # add to namespaces
                        nsmap[xmlns_prefix] = property_ns + '#'  # add to map for xml creation

                        property_key = "{}:{}".format(xmlns_prefix, prop_dummy._name) # short namespace and class of property
                        properties[property_key] = {'xmlns': property_ns,
                                                    'name': prop_dummy._name,
                                                    'knoraType': prop_dummy._property_type}

                    except (TypeError, AttributeError) as e:
                        print(e)

                property_key = "{}:{}".format(namespaces[resource_ns][0], 'seqnum')
                properties[property_key] = {'xmlns': namespaces[resource_ns][1],
                                            'name': 'seqnum',
                                            'knoraType': 'int_value'}

                resource_info[resource_key] = OrderedDict(sorted(properties.items(), key=lambda t: t[0])) # add metadata about properties
    except Exception as e:
        print(e)

    try:
        nsmap['xsi'] = "http://www.w3.org/2001/XMLSchema-instance"

        # make root for response XML
        root = etree.Element(_tag_tpl.format(_xmlns_rdf, 'RDF'),
                             nsmap=nsmap)

        # process resources
        for entry in resource_set:
            resource = entry[0]
            client_id = _sanitize_id(entry[1]) # ID given by source data
            resource_key = "{}:{}".format(namespaces[resource._namespace][0], resource._name) # short ns and tag of resource

            # xml node defining the resource
            resource_root = etree.SubElement(root,
                                             _tag_tpl.format(_xmlns_rdf, 'Description'),
                                             attrib={_tag_tpl.format(_xmlns_rdf, 'about'): client_id})

            rdf_type = etree.SubElement(resource_root, _tag_tpl.format(_xmlns_rdf, 'type'))  # subnode for label
            rdf_type.set(_tag_tpl.format(_xmlns_rdf, 'resource'), _onto_tpl.format(resource._namespace, resource._name))  # set class the value of the label subnode

            label = etree.SubElement(resource_root, _tag_tpl.format(_xmlns_rdfs, 'label'))  # subnode for label
            label.text = resource._label # set the value of the label subnode

            try:
                if resource._file:
                    path = resource._file['path']
                    mimetype = resource._file['mimetype']
                    etree.SubElement(resource_root,
                                     _tag_tpl.format(_xmlns_TODO, 'file'),  # TODO add mechanism for images
                                     path=path,
                                     mimetype=mimetype)
                    label.text = resource._label
            except AttributeError:
                pass
            properties_info = resource_info[resource_key] # properties of this resource in the iteration

            seqnum = None
            for key, prop_info in properties_info.items():
                # key: short namespace and property name
                # prop_info: list of property metadata

                property_value = resource.__dict__.get(prop_info['name'])
                if prop_info['name'] == 'seqnum':
                    if property_value is not None:
                        seqnum = (prop_info, property_value)
                    continue
                if property_value not in ['', {}, None]:

                    # turn properties into tuple
                    if isinstance(property_value, str) or isinstance(property_value, tuple):
                        prop_values = {property_value}
                    else:
                        try:
                            prop_values = set(property_value)
                        except TypeError:
                            prop_values = {property_value}

                    tag = _tag_tpl.format(prop_info['xmlns'] + '#', prop_info['name']) # combine property name with resource namespace

                    # format property values
                    for value in prop_values:
                        if isinstance(value, bool): # boolean
                            value = 1 if value is True else 0
                        if isinstance(value, int): # integer
                            print('DEBUG - value is int ({})'.format(value))
                        if value is None: # no value specified
                            print('DEBUG - value is None ({})')
                        if prop_info['knoraType'] == 'link_value':

                            # subnode for link property
                            link = etree.SubElement(resource_root, tag)
                            link.set(_tag_tpl.format(_xmlns_rdf, 'resource'), value.target)

                        elif not isinstance(value, str) and prop_info['knoraType'] == 'richtext_value':
                            # annotated text is included as XML literal
                            text_property = etree.SubElement(resource_root, tag, attrib={_tag_tpl.format(_xmlns_rdf, 'datatype'): 'http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral'})

                            text_property.append(value.textContent)

                        else:
                            # strings and similar types
                            # make a subnode for the property:
                            cur_entry = etree.SubElement(resource_root,
                                                         tag,
                                                         attrib={_tag_tpl.format(_xmlns_rdf, 'datatype'): _knoraType_to_xsd[prop_info['knoraType']]})
                            # set the value of the property as subnode text
                            cur_entry.text = str(value)
            if seqnum is not None:
                # seqnum ...
                prop_info, value = seqnum

                # subnode for seqnum
                cur_entry = etree.SubElement(resource_root, _tag_tpl.format(_xmlns_knora_base, 'seqnum'),
                                             attrib={_tag_tpl.format(_xmlns_rdf, 'datatype'): _knoraType_to_xsd['int_value']})
                # value as content
                cur_entry.text = str(value)

        return root

        #    tag = _tag_tpl.format(namespaces[resource_ns][1], resource._name)

    except Exception as e:
        print(e)
    return

def xml_struct(resource_set, encoding=None):
    """

    :param resource_set:
    :param standard_xmlns:
    :param schema_xsd:
    :param encoding:
    :return:
    """

    if not encoding:
        encoding = 'UTF-8'

    xml_struct = __xml_struct__(resource_set)

    try:
        result = etree.tostring(xml_struct, pretty_print=True, xml_declaration=True, encoding=encoding)
    except Exception:
        result = None

    return result
