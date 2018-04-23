#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...language.classes.HumanNaturalLanguageExpression import HumanNaturalLanguageExpression
from ...information_carrier.properties.isWrittenWith import IsWrittenWith
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:WrittenText

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class WrittenText(HumanNaturalLanguageExpression):
    """
    Text written by any method, e.g. manually, with an analogue or digital
    typewriter, or on a computer, abstracted from its carrier.

    Labels: geschriebener Text (de) / written text (en)
    """
    def __init__(self, isWrittenWith=None, **kwargs):
        """

        :param isWrittenWith:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "WrittenText"

        self.isWrittenWith = IsWrittenWith(isWrittenWith)
