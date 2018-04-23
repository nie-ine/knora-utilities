#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .HumanNaturalLanguageExpression import HumanNaturalLanguageExpression
from ...event.classes.Output import Output
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:Translation

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class Translation(HumanNaturalLanguageExpression, Output):
    """
    Human natural language expression transferred in another natural language.

    Labels: Übersetzung (de) / translation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Translation"
