#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .intValue import IntValue
"""
seqnum: definition to handle Knora Base Ontology (KBO)
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class Seqnum(IntValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, number):
        """

        :param number:
        """
        super(Seqnum, self).__init__(number)
        self._name = 'seqnum'
        self._property_type = 'seqnum'

#    def __repr__(self):
#        """
#
#        :return:
#        """
#        return """[{{'seqnum': {:d}}}]""".format(self._value)

#    def __str__(self):
#        """
#
#        :return:
#        """
#        return """[{{'{:s}': {:d}}}]""".format(self._json['value_type'], self._value)

#    def __json_struct__(self):
#        """
#
#        :return:
#        """
#        if value:
#            return [{self._property: self._value}]
