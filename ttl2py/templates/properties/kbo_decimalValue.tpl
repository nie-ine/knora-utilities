#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
test.py: a simple program to test the abilities of py-redis
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class DecimalValue(HasValue):
    """

    """

    def __init__(self, integer):
        super().__init__(int(integer))
        self._name = 'DecimalValue'
        self._property_type = 'decimal_value'

    def __json_struct__(self):
        """

        :return:
        """
        if self._value or self.value == 0:
            return [{self._json['value_type']: self._value}]