#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Text import Text
from ...text.classes.DiaryEntry import DiaryEntry as tex_DiaryEntry
from ..properties.isInDiaryConvolute import IsInDiaryConvolute
from ..properties.isInDiary import IsInDiary
from ...text_structure.properties.hasStructure import HasStructure
from ...publishing.properties.hasNachlassPublicationDescription import HasNachlassPublicationDescription
from ...information_carrier.properties.hasDiaryEnteringDate import HasDiaryEnteringDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:DiaryEntry

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class DiaryEntry(Text, tex_DiaryEntry):
    """
    Diary entry authored by Kuno Raeber.

    Labels: Tagebucheintrag (de) / diary entry (en)
    """
    def __init__(self, isInDiaryConvolute=None, isInDiary=None, hasStructure=None, hasNachlassPublicationDescription=None, hasDiaryEnteringDate=None, **kwargs):
        """

        :param isInDiaryConvolute:
        :param isInDiary:
        :param hasStructure:
        :param hasNachlassPublicationDescription:
        :param hasDiaryEnteringDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DiaryEntry"

        self.isInDiaryConvolute = IsInDiaryConvolute(isInDiaryConvolute)
        self.isInDiary = IsInDiary(isInDiary)
        self.hasStructure = HasStructure(hasStructure)
        self.hasNachlassPublicationDescription = HasNachlassPublicationDescription(hasNachlassPublicationDescription)
        self.hasDiaryEnteringDate = HasDiaryEnteringDate(hasDiaryEnteringDate)
