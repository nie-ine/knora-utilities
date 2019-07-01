#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
LinkValue: definition to handle Knora Base Ontology (KBO) dates
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class LinkValue(HasValue):
    """

    """

    def __init__(self, link):
        """

        :param link:
        """
        super().__init__(link)
        self._name = 'LinkValue'
        self._property_type = 'link_value'

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if key == '_value' and value is not None and not isinstance(value, str):
            raise TypeError("Wrong data type for LinkValue")
        super().__setattr__(key, value)

    def __json_struct__(self):
        """

        :return:
        """
        if self._value:
            if isinstance(self._value, list) or isinstance(self._value, set):
                attrib_representation = []
                for item in self._value:
                    try:
                        value: str = item._value.target
                    except AttributeError:
                        value: str = item._value
                    if value:
                        attrib_representation.append({self._property_type: value})
                if attrib_representation:
                    return attrib_representation
            else:
                try:
                    value: str = self._value.target
                except AttributeError:
                    value: str = self._value
                if value:
                    return [{self._property_type: value}]
        return None

