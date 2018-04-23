#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ProsodicStructure import ProsodicStructure
from .Line import Line
from ..properties.isVerseOfNovel import IsVerseOfNovel
from ..properties.isVerseOfPoem import IsVerseOfPoem
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Verse

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Verse(ProsodicStructure, Line):
    """
    Text line with prosody.

    Labels: Vers (de) / verse (en)
    """
    def __init__(self, isVerseOfNovel=None, isVerseOfPoem=None, **kwargs):
        """

        :param isVerseOfNovel:
        :param isVerseOfPoem:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Verse"

        self.isVerseOfNovel = IsVerseOfNovel(isVerseOfNovel)
        self.isVerseOfPoem = IsVerseOfPoem(isVerseOfPoem)
