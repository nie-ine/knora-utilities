#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.Information import Information
from ..properties.expressedInDialect import ExpressedInDialect
from ..properties.translatedIn import TranslatedIn
from ..properties.translatedInNaturalLanguage import TranslatedInNaturalLanguage
from ..properties.expressedInNaturalLanguage import ExpressedInNaturalLanguage
from ..properties.hasTranslator import HasTranslator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:HumanNaturalLanguageExpression

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HumanNaturalLanguageExpression(Information):
    """
    Expression in a human natural language.

    Labels: menschliche naturliche sprachliche Äusserung (de) / human natural language expression (en)
    """
    def __init__(self, expressedInDialect=None, translatedIn=None, translatedInNaturalLanguage=None, expressedInNaturalLanguage=None, hasTranslator=None, **kwargs):
        """

        :param expressedInDialect:
        :param translatedIn:
        :param translatedInNaturalLanguage:
        :param expressedInNaturalLanguage:
        :param hasTranslator:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "HumanNaturalLanguageExpression"

        self.expressedInDialect = ExpressedInDialect(expressedInDialect)
        self.translatedIn = TranslatedIn(translatedIn)
        self.translatedInNaturalLanguage = TranslatedInNaturalLanguage(translatedInNaturalLanguage)
        self.expressedInNaturalLanguage = ExpressedInNaturalLanguage(expressedInNaturalLanguage)
        self.hasTranslator = HasTranslator(hasTranslator)
