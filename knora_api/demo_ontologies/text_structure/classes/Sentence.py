#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .SyntacticStructure import SyntacticStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Sentence

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Sentence(SyntacticStructure):
    """
    Syntactic structure unit as one or more linked words, typically a subject
    and predicate.

    Labels: Satz (de) / sentence (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Sentence"
