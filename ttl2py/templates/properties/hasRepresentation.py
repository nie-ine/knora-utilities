#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasLinkTo import HasLinkTo

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


class HasRepresentation(HasLinkTo):  # Subclass link to get handy functions
    """

    """

    def __init__(self, link):
        """

        :param link:
        """
        super(HasRepresentation, self).__init__(link)
        self._name = 'hasRepresentation'
        self._objectClassConstraint = "http://www.knora.org/ontology/knora-base#Representation"

    # def __json_struct__(self):
    #     """
    #
    #     :return:
    #     """
    #     if self._value:
    #         try:
    #             value: str = self._value.target
    #         except AttributeError:
    #             value: str = self._value
    #         if value:
    #             return [{self._property_type: self.value}]
