#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .teachingByValue import TeachingByValue

"""
definition of property teaching:LectureByValue

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class LectureByValue(TeachingByValue):
    """
    Relating a lecture to a reification statement of the relation between the lecture and a person having the lecturer role.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/teaching"
        self._name = "lectureByValue"
