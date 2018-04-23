#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Teaching import Teaching
from ..properties.lectureBy import LectureBy
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class teaching:Lecture

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class Lecture(Teaching):
    """
    Teaching by oral presentation about a particular subject.

    Labels: Vorlesung (de) / lecture (en)
    """
    def __init__(self, lectureBy=None, **kwargs):
        """

        :param lectureBy:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Lecture"

        self.lectureBy = LectureBy(lectureBy)
