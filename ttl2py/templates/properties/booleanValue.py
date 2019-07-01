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
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class BooleanValue(HasValue):
    """

    """

    def __init__(self, boolean):
        """

        :param boolean:
        """
        super().__init__(bool(boolean))
        self._name = "BooleanValue"
        self._property_type = 'boolean_value'

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        if key == '_value' and value is not None:
            value = bool(value)

        super().__setattr__(key, value)
