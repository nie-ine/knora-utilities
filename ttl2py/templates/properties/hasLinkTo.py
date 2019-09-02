#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from .hasValue import HasValue

"""
hasLinkTo: definition to handle Knora Base Ontology (KBO) dates
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"

LinkValue = namedtuple('LinkValue', 'linkType target')


class HasLinkTo(HasValue):  # Subclass link to get handy functions
    """

    """

    def __init__(self, link):
        """

        :param link:
        """
        super(HasLinkTo, self).__init__(link)
        self._name = 'LinkValue'
        self._property_type = 'link_value'
        self._objectClassConstraint = None

    def __json_struct__(self):
        """

        :return:
        """
        if self._value:
            if isinstance(self._value, list) or isinstance(self._value, set):
                attrib_representation = []
                for item in self._value:
                    try:
                        attrib_representation.append({self._property_type: item.target})
                    except AttributeError:
                        pass

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
