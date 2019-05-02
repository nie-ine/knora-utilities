#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC
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
                    value = prop_type(value)
                    properties[value.key()] = value.__json_struct__()
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

        def _calc_checksum(item):
            """
            caluculates the checksum of a given item (i.e. value)

            :param item: the value we want to calculate the checksum for
            :return: int; checksum of item => 0 := neutral element
            """

            if isinstance(item, LinkValue):
                if 'iri' == item.linkType.lower() and item.target:
                    # we want to deal with 'real' links, only (i.e. from type 'iri' and not empty)
                    return hash(item.target)
            else:
                return hash(item)

            return 0

        if not type(self) is Resource and self._namespace:
            checksum_value = 0
            for attr, value in self.__dict__.items():
                if attr.startswith('_'):
                    if attr in ['_namespace', '_project_id', '_name']:
                        checksum_value ^= hash(value)
                    continue

                try:
                    checksum_value ^= (hash(attr) ^ _calc_checksum(value))
                except TypeError as e:
                    # this parts handles a collection of values
                    # (i.e. a set or a list; dict has to be implemented)
                    # calculate a property's checksum composed by a checksum of each item
                    collection_checksum = 0
                    try:
                        for item in value:
                            try:
                                collection_checksum ^= _calc_checksum(item)
                            except TypeError:
                                continue
                    except Exception:
                        pass

                    checksum_value ^= (hash(attr) ^ hash(collection_checksum))

        return checksum_value
