#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Expression import Expression
from ...information_carrier.properties.isInDiary import IsInDiary
from ...information_carrier.properties.hasDiaryEnteringDate import HasDiaryEnteringDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:DiaryEntry

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class DiaryEntry(Expression):
    """
    Periodical, usually daily description of a personal experience or
    observation written in a diary.

    Labels: Tagebucheintrag (de) / diary entry (en)
    """
    def __init__(self, isInDiary=None, hasDiaryEnteringDate=None, **kwargs):
        """

        :param isInDiary:
        :param hasDiaryEnteringDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DiaryEntry"

        self.isInDiary = IsInDiary(isInDiary)
        self.hasDiaryEnteringDate = HasDiaryEnteringDate(hasDiaryEnteringDate)
