#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...language.classes.Translator import Translator as lan_Translator
from ...human.classes.Creator import Creator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Translator

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Translator(lan_Translator, Creator):
    """
    Role of a person translating text by writing.

    Labels: Übersetzer (de) / translator (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Translator"
