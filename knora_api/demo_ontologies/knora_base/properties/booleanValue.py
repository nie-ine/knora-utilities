#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
from .hasValue import HasValue

"""
BooleanValue: definition to handle Knora Base Ontology (KBO)
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasBoolean(HasValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, boolean):
        """

        :param boolean:
        """
        super(HasBoolean, self).__init__(bool(boolean))
        self._name = "hasBoolean"
        self._property_type: 'boolean_value'}

#    def __repr__(self):
#        """
#
#        :return:
#        """
#        if self._value or self._value is False:
#            return """[{{'boolean_value': {}}}]""".format(self._value)

#    def __str__(self):
#        """
#
#        :return:
#        """
#        if self._value or self._value is False:
#            return """[{{'boolean_value': {}}}]""".format(self._value)

#    def __json_struct__(self):
#        """
#
#        :return:
#        """
#
#        return [{self._json['value_type']: self._value}]

#    def json(self):
#        """
#
#        :return:
#        """
#        if self._value or self._value is False:
#            return [{'boolean_value': self._value}]