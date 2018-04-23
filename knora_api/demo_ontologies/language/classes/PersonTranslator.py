#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Translator import Translator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:PersonTranslator

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class PersonTranslator(Translator):
    """
    Role of a person as translator.

    Labels: Person-Übersetzer (de) / person-translator (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PersonTranslator"
