#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...language.classes.HumanNaturalLanguageExpression import HumanNaturalLanguageExpression
from ...concept.classes.Expression import Expression as con_Expression
from ..properties.hasRevisor import HasRevisor
from ..properties.hasContent import HasContent
from ...text_editing.properties.hasDiplomaticTranscription import HasDiplomaticTranscription
from ...text_editing.properties.hasCriticalEdition import HasCriticalEdition
from ..properties.hasReferenceText import HasReferenceText
from ...text_editing.properties.hasRedactor import HasRedactor
from ..properties.hasAbbreviator import HasAbbreviator
from ...text_editing.properties.hasSameEditionAs import HasSameEditionAs
from ...text_editing.properties.hasEditor import HasEditor
from ...text_editing.properties.hasEdition import HasEdition
from ...text_structure.properties.hasStructure import HasStructure
from ..properties.hasIncipit import HasIncipit
from ..properties.hasVersionIndicator import HasVersionIndicator
from ..properties.hasAuthor import HasAuthor
from ..properties.hasGlossator import HasGlossator
from ...text_structure.properties.hasLineNumber import HasLineNumber
from ..properties.hasCopyist import HasCopyist
from ..properties.hasExplicit import HasExplicit
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Expression

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Expression(HumanNaturalLanguageExpression, con_Expression):
    """
    Text as a human luinguistic expression.

    Labels: Text-Expression (de) / text expression (en)
    """
    def __init__(self, hasRevisor=None, hasContent=None, hasDiplomaticTranscription=None, hasCriticalEdition=None, hasReferenceText=None, hasRedactor=None, hasAbbreviator=None, hasSameEditionAs=None, hasEditor=None, hasEdition=None, hasStructure=None, hasIncipit=None, hasVersionIndicator=None, hasAuthor=None, hasGlossator=None, hasLineNumber=None, hasCopyist=None, hasExplicit=None, **kwargs):
        """

        :param hasRevisor:
        :param hasContent:
        :param hasDiplomaticTranscription:
        :param hasCriticalEdition:
        :param hasReferenceText:
        :param hasRedactor:
        :param hasAbbreviator:
        :param hasSameEditionAs:
        :param hasEditor:
        :param hasEdition:
        :param hasStructure:
        :param hasIncipit:
        :param hasVersionIndicator:
        :param hasAuthor:
        :param hasGlossator:
        :param hasLineNumber:
        :param hasCopyist:
        :param hasExplicit:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Expression"

        self.hasRevisor = HasRevisor(hasRevisor)
        self.hasContent = HasContent(hasContent)
        self.hasDiplomaticTranscription = HasDiplomaticTranscription(hasDiplomaticTranscription)
        self.hasCriticalEdition = HasCriticalEdition(hasCriticalEdition)
        self.hasReferenceText = HasReferenceText(hasReferenceText)
        self.hasRedactor = HasRedactor(hasRedactor)
        self.hasAbbreviator = HasAbbreviator(hasAbbreviator)
        self.hasSameEditionAs = HasSameEditionAs(hasSameEditionAs)
        self.hasEditor = HasEditor(hasEditor)
        self.hasEdition = HasEdition(hasEdition)
        self.hasStructure = HasStructure(hasStructure)
        self.hasIncipit = HasIncipit(hasIncipit)
        self.hasVersionIndicator = HasVersionIndicator(hasVersionIndicator)
        self.hasAuthor = HasAuthor(hasAuthor)
        self.hasGlossator = HasGlossator(hasGlossator)
        self.hasLineNumber = HasLineNumber(hasLineNumber)
        self.hasCopyist = HasCopyist(hasCopyist)
        self.hasExplicit = HasExplicit(hasExplicit)
