#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .HandwrittenPoem import HandwrittenPoem
from ...human.classes.FirstVersion import FirstVersion
from ..properties.isInNotebook import IsInNotebook
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemNote

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemNote(HandwrittenPoem, FirstVersion):
    """
    Poem note authored by Kuno Raeber.

    Labels: Gedichtnotiz (de) / poem note (en)
    """
    def __init__(self, isInNotebook=None, **kwargs):
        """

        :param isInNotebook:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemNote"

        self.isInNotebook = IsInNotebook(isInNotebook)
