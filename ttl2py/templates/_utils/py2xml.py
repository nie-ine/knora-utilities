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

from ..knora_base.properties.hasLinkTo import LinkValue

_XMLNS_tpl = "http://api.knora.org/ontology/{}/{}/xml-import/v1#"
_xmlns_knoraXmlImport = "http://api.knora.org/ontology/knoraXmlImport/v1#"
_xmlns_prefix_tpl = "p{}-{}"
_tag_tpl = "{{{:s}}}{:s}"


def validate_xml(source_xml, schema_xsd):
    """
    validates the source_xml against the main xml schema SCHEMA_FILE received from knora.

    :param source_xml:
    :return:
    """
    schema = get_schema(schema_xsd)
    if isinstance(etree, source_xml):
        to_validate = source_xml
    else:
        to_validate = etree.parse(source_xml)

    if schema.validate(to_validate):
        print("{} was successfully validated!".format(source_xml))
    else:
        schema.assertValid(to_validate)


def get_schema(schema_xsd):
    """
    gets the xml schemas from knora for validating
    :param: OUTPUT_XML: The generated import xml which should be validated
    :return: the xml schema against which the OUTPUT_XML will be validated
    """
    xmlschema_doc = etree.parse(schema_xsd)
    return etree.XMLSchema(xmlschema_doc)


def _sanitize_id(text):
    """

    :param text:
    :return:
    """

    return "_".join(text.split())


def __xml_struct__(resource_set, standard_xmlns, schema_xsd=None):
    """

    :param resource_set: a set that contains the resource to create
    :return: string that contains the created xml-description to be used with knora
    """

    nsmap = {'knoraXmlImport': _xmlns_knoraXmlImport,
             None: standard_xmlns}

    namespaces = {}
    resource_info = {}

    try:
        for entry in resource_set:
            resource = entry[0]
            resource_ns = resource._namespace
            if resource_ns not in namespaces:
                onto_code = resource_ns.split('/')[-2]
                onto_name = resource_ns.split('/')[-1]
                xmlns_prefix = _xmlns_prefix_tpl.format(onto_code, onto_name)
                xmlns = _XMLNS_tpl.format(onto_code, onto_name)
                namespaces[resource_ns] = (xmlns_prefix, xmlns)
                nsmap[xmlns_prefix] = xmlns

            resource_key = "{}:{}".format(namespaces[resource_ns][0], resource._name)
            if resource_key not in resource_info:
                properties = {}
                for attr, value in resource.__dict__.items():
                    if attr.startswith('_') or attr == 'seqnum':
                        continue
                    try:
                        prop_type = resource.__dict__.get("_{}".format(attr))
                        prop_dummy = prop_type(None)
                        property_ns = prop_dummy._namespace
                        onto_code = property_ns.split('/')[-2]
                        onto_name = property_ns.split('/')[-1]
                        xmlns_prefix = _xmlns_prefix_tpl.format(onto_code, onto_name)
                        xmlns = _XMLNS_tpl.format(onto_code, onto_name)
                        namespaces[property_ns] = (xmlns_prefix, xmlns)
                        nsmap[xmlns_prefix] = xmlns
                        property_key = "{}:{}".format(xmlns_prefix, prop_dummy._name)
                        properties[property_key] = {'xmlns': xmlns,
                                                    'name': prop_dummy._name,
                                                    'knoraType': prop_dummy._property_type}
                        if prop_dummy._property_type == 'link_value':
                            target = prop_dummy._objectClassConstraint
                            target_ns, target_name = target.split('#')
                            onto_code = target_ns.split('/')[-2]
                            onto_name = target_ns.split('/')[-1]
                            xmlns_prefix = _xmlns_prefix_tpl.format(onto_code, onto_name)
                            xmlns = _XMLNS_tpl.format(onto_code, onto_name)
                            namespaces[target_ns] = (xmlns_prefix, xmlns)
                            nsmap[xmlns_prefix] = xmlns
                            properties[property_key]['objectClassConstraint'] = (xmlns, target_name)
                    except (TypeError, AttributeError) as e:
                        print(e)

                property_key = "{}:{}".format(namespaces[resource_ns][0], 'seqnum')
                properties[property_key] = {'xmlns': namespaces[resource_ns][1],
                                            'name': 'seqnum',
                                            'knoraType': 'int_value'}

                resource_info[resource_key] = OrderedDict(sorted(properties.items(), key=lambda t: t[0]))
    except Exception as e:
        print(e)

    try:
        if schema_xsd:
            nsmap['xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
            attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
            attrib = {attr_qname: schema_xsd}
        else:
            attrib = None

        root = etree.Element(_tag_tpl.format(_xmlns_knoraXmlImport, 'resources'),
                             attrib=attrib,
                             nsmap=nsmap)

        for entry in resource_set:
            resource = entry[0]
            client_id = _sanitize_id(entry[1])
            resource_ns = resource._namespace
            resource_key = "{}:{}".format(namespaces[resource_ns][0], resource._name)
            resource_xmlns = namespaces[resource_ns][1]
            resource_root = etree.SubElement(root,
                                             _tag_tpl.format(resource_xmlns, resource._name),
                                             id=client_id)
            label = etree.SubElement(resource_root, _tag_tpl.format(_xmlns_knoraXmlImport, 'label'))
            label.text = resource._label

            try:
                if resource._file:
                    path = resource._file['path']
                    mimetype = resource._file['mimetype']
                    etree.SubElement(resource_root,
                                     _tag_tpl.format(_xmlns_knoraXmlImport, 'file'),
                                     path=path,
                                     mimetype=mimetype)
                    label.text = resource._label
            except AttributeError:
                pass
            properties_info = resource_info[resource_key]

            seqnum = None
            for key, prop_info in properties_info.items():
                property_value = resource.__dict__.get(prop_info['name'])
                if prop_info['name'] == 'seqnum':
                    if property_value is not None:
                        seqnum = (prop_info, property_value)
                    continue
                if property_value not in ['', {}, None]:
                    if isinstance(property_value, str) or isinstance(property_value, tuple):
                        prop_values = {property_value}
                    else:
                        try:
                            prop_values = set(property_value)
                        except TypeError:
                            prop_values = {property_value}

                    if prop_info['xmlns'] == resource_xmlns:
                        tag_name = prop_info['name']
                    else:
                        tag_name = '__'.join(key.split(':'))
                    tag = _tag_tpl.format(resource_xmlns, tag_name)

                    for value in prop_values:
                        if isinstance(value, bool):
                            value = 1 if value is True else 0
                        if isinstance(value, int):
                            print('DEBUG - value is int ({})'.format(value))
                        if value is None:
                            print('DEBUG - value is None ({})')
                        if prop_info['knoraType'] == 'link_value':
                            link = etree.SubElement(resource_root, tag)
                            linkType = value.linkType
                            target = value.target
                            a = _tag_tpl.format(prop_info['objectClassConstraint'][0],
                                                prop_info['objectClassConstraint'][1])
                            etree.SubElement(link,
                                             a,
                                             knoraType=prop_info['knoraType'],
                                             linkType=linkType,
                                             target=target)
                        else:
                            cur_entry = etree.SubElement(resource_root,
                                                         tag,
                                                         knoraType=prop_info['knoraType'])
                            cur_entry.text = str(value)
            if seqnum is not None:
                prop_info, value = seqnum
                tag = _tag_tpl.format(prop_info['xmlns'], 'knoraXmlImport__seqnum')
                cur_entry = etree.SubElement(resource_root,
                                             _tag_tpl.format(prop_info['xmlns'], 'knoraXmlImport__seqnum'),
                                             knoraType=prop_info['knoraType'])
                cur_entry.text = str(value)

        return root

        #    tag = _tag_tpl.format(namespaces[resource_ns][1], resource._name)

    except Exception as e:
        print(e)
    return

def xml_struct(resource_set, standard_xmlns, schema_xsd=None, encoding=None):
    """

    :param resource_set:
    :param standard_xmlns:
    :param schema_xsd:
    :param encoding:
    :return:
    """

    if not encoding:
        encoding = 'UTF-8'

    xml_struct = __xml_struct__(resource_set, standard_xmlns, schema_xsd)

    try:
        result = etree.tostring(xml_struct, pretty_print=True, xml_declaration=True, encoding=encoding)
    except Exception:
        result = None

    return result
