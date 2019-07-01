#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC
from hashlib import md5
from ..properties.hasLinkTo import LinkValue

"""
definition of abstract class knora-base:Resource
"""


class Resource(ABC):
    """

    """

    _ontology = "http://www.knora.org/ontology"
    _project_prefix = "http://rdfh.ch/projects"

    def __init__(self, label, seqnum=None):
        self._namespace = "http://www.knora.org/ontology/knora-base"
        self._project_id = None
        self._name = "Resource"
        self._label = label
        self.seqnum = seqnum

    def __getattribute__(self, item):
        """

        :param item:
        :return:
        """
        try:
            return object.__getattribute__(self, item)._value
        except AttributeError as e:
            return object.__getattribute__(self, item)

    def namespaces(self):
        """

        :return: a set of the used namespaces (resource and its properties)
        """

        result = set()
        # We won't deal with kbo.Resource directly
        if not type(self) is Resource and self._namespace:
            result.add('http://www.knora.org/ontology/knora-base')
            result.add(self._namespace)
            for attr, value in self.__dict__.items():
                if attr.startswith('_') or attr == 'seqnum':
                    continue
                try:
                    prop_type = self.__dict__.get("_{}".format(attr))
                    prop_dummy = prop_type(None)
                    result.add(prop_dummy._namespace)
                except (TypeError, AttributeError) as e:
                    print(e)
        return result

    def json(self):
        """

        :return:
        """

        # We won't deal with kbo.Resource directly
        if not type(self) is Resource and self._namespace:
            restype_id = "{:s}#{:s}".format(self._namespace, self._name)
            properties = {}
            for attr, value in self.__dict__.items():
                if attr.startswith('_') or attr == 'seqnum' or value in ['', None]:
                    continue
                try:
                    prop_type = self.__dict__.get("_{}".format(attr))
                    tmp_value = prop_type(value)
                    json_struct = tmp_value.__json_struct__()
                    if json_struct:
                        properties[tmp_value.key()] = tmp_value.__json_struct__()
                except (TypeError, AttributeError) as e:
                    print(e)

            try:
                seqnum = int(self.seqnum)
                if seqnum >= 0:
                    key = 'http://www.knora.org/ontology/knora-base#seqnum'
                    properties[key] = seqnum
            except TypeError:
                if self.seqnum:
                    print("seqnum isn't neither a non-negative integer nor None!")

            return {'restype_id': restype_id,
                    'label': self._label,
                    'project_id': self._project_id,
                    'properties': properties}
        return None

    def __getitem__(self, item):
        """

        :return:
        """

        return item._value

    def __repr__(self):
        """

        :return:
        """

        return "{}".format(self.json())

    def __str__(self):
        """

        :return:
        """

        return "{}".format(self.json())

    def checksum(self):
        """
        Calculates a checksum based on the attribute names and their current values

        :return: integer, that represents the checksum
        """

        def _calc_checksum(value):
            """
            caluculates the checksum of a given item (i.e. value)

            :param item: the value we want to calculate the checksum for
            :return: int; checksum of item => 0 := neutral element
            """

            def _calc_md5(val):
                """

                :param val:
                :return:
                """
                m = md5()
                m.update(("{}".format(val)).encode(encoding='utf-8'))
                return m.hexdigest()

            checksum_md5 = ''
            if value is None:
                checksum_md5 = ''
            elif isinstance(value, LinkValue):
                if 'iri' == value.linkType.lower() and value.target:
                    # we want to deal with 'real' links, only (i.e. from type 'iri' and not empty)
                    checksum_md5 = _calc_md5(value.target)
            elif isinstance(value, list) or isinstance(value, set):
                # process collection
                if len(value) == 0:
                    checksum_md5 = ''
                else:
                    tmp_checksum = 0
                    for item in value:
                        if isinstance(item, LinkValue):
                            # process LinkValue values
                            if 'iri' == item.linkType.lower() and item.target:
                                # we want to deal with 'real' links, only (i.e. from type 'iri' and not empty)
                                tmp_checksum ^= int(_calc_md5(item.target), 16)
                            continue
                        tmp_checksum ^= int(_calc_md5(value), 16)
                    checksum_md5 = "{:X}".format(tmp_checksum)
            else:
                checksum_md5 = _calc_md5(value)
            return checksum_md5

        checksum_value = 0
        if not type(self) is Resource and self._namespace:
            for attr, value in sorted(self.__dict__.items()):
                if attr.startswith('_') and attr not in ['_namespace', '_project_id', '_name']:
                    continue

                attr_md5 = md5()
                attr_md5.update(("{}:{}".format(attr, _calc_checksum(value))).encode(encoding='utf-8'))

                checksum_value ^= int(attr_md5.hexdigest(), 16)

        return "{:032X}".format(checksum_value)
