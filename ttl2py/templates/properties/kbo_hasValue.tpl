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
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasValue(object):
    """

    """

    # def __new__(cls, string):
    #     """
    #
    #     :param string:
    #     :return:
    #     """
    #     if string is not None:
    #         return super(HasValue, cls).__new__(cls, string)
    #     return None

    def __init__(self, value):
        self._namespace = "http://www.knora.org/ontology/knora-base"
        self._name = "hasValue"
        self._value = value

        self._property_type = 'value'

    def key(self):
        """

        :return:
        """
        return """{:s}#{:s}""".format(self._namespace, self._name)

    def __repr__(self):
        """

        :return:
        """

        return self._value
#        return json.dumps({self._value_type: self._value})

    def __str__(self):
        """

        :return:
        """

        return self._value
#        return json.dumps({self._value_type: self._value})

    def __json_struct__(self):
        """

        :return:
        """

        if self._value:
            return [{self._property_type: self._value}]

    def json(self):
        """

        :return:
        """

        value = self.__json_struct__()
        if value:
            return json.dumps(value)