#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
IntValue: definition of a datatype to handle Knora Base Ontology (KBO) integers
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class IntValue(HasValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, integer):
        if integer is not None:
            integer = int(integer)
        super().__init__(integer)
        self._name = 'IntValue'
        self._property_type = 'int_value'

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if (key == '_value' and value is not None
                and not isinstance(value, int)
                and not (isinstance(value, list) or isinstance(value, set))):
            raise TypeError("Wrong data type for IntValue")
        super().__setattr__(key, value)

    def __json_struct__(self):
        """

        :return:
        """
        if self._value or self._value == 0:
            super().__json_struct__()