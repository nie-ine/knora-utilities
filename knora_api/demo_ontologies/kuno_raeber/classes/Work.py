#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.IndividualWork import IndividualWork
from ...concept.properties.isExpressedIn import IsExpressedIn
from ...text.properties.hasTitle import HasTitle
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Work

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Work(IndividualWork):
    """
    Work by Kuno Raeber.

    Labels: Werk (de) / work (en)
    """
    def __init__(self, isExpressedIn=None, hasTitle=None, **kwargs):
        """

        :param isExpressedIn:
        :param hasTitle:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Work"

        self.isExpressedIn = IsExpressedIn(isExpressedIn)
        self.hasTitle = HasTitle(hasTitle)
