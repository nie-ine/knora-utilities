#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .HumanLanguage import HumanLanguage
from ..properties.hasCode import HasCode
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:HumanNaturalLanguage

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HumanNaturalLanguage(HumanLanguage):
    """
    Language naturally evolved in humans.

    Labels: menschliche naturliche Sprache (de) / human natural language (en)
    """
    def __init__(self, hasCode=None, **kwargs):
        """

        :param hasCode:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "HumanNaturalLanguage"

        self.hasCode = HasCode(hasCode)
