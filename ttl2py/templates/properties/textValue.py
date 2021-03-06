#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from .hasValue import HasValue

"""
RichTextValue: definition of a datatype to handle Knora Base Ontology (KBO) text
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"

RichTextValue = namedtuple('RichTextValue', 'mappingId textContent')


class TextValue(HasValue):  # Subclass string to get handy functions
    """

    """

    def __init__(self, text):
        """

        :param text:
        """
        super().__init__(text)
        self._name = "TextValue"
        self._property_type = 'richtext_value'
        self._value_type = 'utf8str'

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if (key == '_value' and value is not None
                and not isinstance(value, str)
                and not (isinstance(value, list) or isinstance(value, set))):
            raise TypeError("Wrong data type for textValue")
        super().__setattr__(key, value)

    def __json_struct__(self):
        """

        :return:
        """
        if self._value:
            return [{self._property_type: {self._value_type: self._value}}]
