#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Language import Language
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:HumanLanguage

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HumanLanguage(Language):
    """
    Language of a human.

    Labels: menschliche Sprache (de) / human language (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "HumanLanguage"
