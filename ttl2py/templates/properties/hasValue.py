#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import collections

"""
knora-base:hasValue: definition of class knora-base:hasValue
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.2"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasValue(object):
    """

    """

    def __init__(self, value):
        self._namespace = "http://www.knora.org/ontology/knora-base"
        self._name = "hasValue"
        self._property_type = 'value'
        self._value = value

    def key(self):
        """

        :return:
        """
        return """{:s}#{:s}""".format(self._namespace, self._name)

    def __json_struct__(self):
        """

        :return:
        """

        if self._value not in [None, '']:
            return [{self._property_type: self._value}]

    def json(self):
        """

        :return:
        """

        value = self.__json_struct__()
        if value not in [None, '']:
            return json.dumps(value)
