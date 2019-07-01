#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
HasLinkToValue: definition to handle Knora Base Ontology (KBO) hasLinkToValue
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasLinkToValue(HasValue):
    """

    """

    def __init__(self, link):
        """

        :param string:
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
            raise TypeError("Wrong data type for hasLinkToValue")
        super().__setattr__(key, value)
