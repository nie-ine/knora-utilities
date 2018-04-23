#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from ...information_carrier.classes.Manuscript import Manuscript
from ...information_carrier.classes.Diary import Diary as inf_Diary
from ...information_carrier.classes.Book import Book
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Diary

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Diary(ArchiveElement, Manuscript, inf_Diary, Book):
    """
    Diary with entries authored by Kuno Raeber.

    Labels: Tagebuch (de) / diary (en)
    """
    def __init__(self, hasArchiveSignature=None, **kwargs):
        """

        :param hasArchiveSignature:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Diary"

        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
