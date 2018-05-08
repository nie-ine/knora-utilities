#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC

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

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if key in ['_namespace', '_project_id', '_name', '_label', 'seqnum']:
            super().__setattr__(key, value)
        else:
            try:
                if value is None or isinstance(value, HasValue):
                    super().__setattr__(key, value)
                elif object.__getattribute__(self, key):
                    object.__getattribute__(self, key)._value = value
                else:
                    raise TypeError("Data type not allowed as a resource property")
            except AttributeError as e:
                return object.__setattr__(self, key, value)

    def json(self):
        """

        :return:
        """

        # We won't deal with kbo.Resource directly
        if not type(self) is Resource and self._namespace:
            restype_id = "{:s}#{:s}".format(self._namespace, self._name)
            properties = {}
            for attr, value in self.__dict__.items():
                if value is None or attr.startswith('_'):
                    continue
                try:
                    if value._value in ['', None]:
                        continue
                    properties[value.key()] = value.__json_struct__()
                except Exception as e:
                    print(e)

            if self.seqnum == 0 or self.seqnum:
                key = 'http://www.knora.org/ontology/knora-base#seqnum'
                properties[key] = [{'int_value': self.seqnum}]

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
        return "{}".format(self.json())

    def __str__(self):
        return "{}".format(self.json())
