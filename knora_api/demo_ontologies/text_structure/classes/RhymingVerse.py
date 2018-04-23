#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Verse import Verse
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:RhymingVerse

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class RhymingVerse(Verse):
    """
    Verse with a rhyme.

    Labels: gereimter Vers (de) / rhyming verse (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "RhymingVerse"
