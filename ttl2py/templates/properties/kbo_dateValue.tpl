#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue
"""
DateValue: definition of a datatype to handle Knora Base Ontology (KBO) dates
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class DateValue(HasValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, date_string, calendar_type=None):
        """

        :param string:
        """
        super(DateValue, self).__init__(date_string)
        self._property_type = 'date_value'
        self.calendar_type = 'JULIAN' if calendar_type in ['j', 'J'] else 'GREGORIAN'

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if key == '_value' and value is not None and not isinstance(value, str):
            ### TODO: check a date's format (Nice to have)
            raise TypeError("Wrong data type for DateValue")
        super().__setattr__(key, value)

    def __repr__(self):
        """

        :return:
        """
        return """['date_value': 'GREGORIAN:{:s}']""".format(self._value)

    def __str__(self):
        """

        :return:
        """
        return """['date_value': 'GREGORIAN:{:s}']""".format(self._value)

    def __json_struct__(self):
        """

        :return:
        """
        if self._value:
            return [{self._property_type: '{:s}:{:s}'.format(self.calendar_type, self._value)}]
