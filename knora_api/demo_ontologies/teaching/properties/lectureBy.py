#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .teachingBy import TeachingBy

"""
definition of property teaching:LectureBy

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class LectureBy(TeachingBy):
    """
    Relating a lecture to a person having the lecturer role.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/teaching"
        self._name = "lectureBy"
