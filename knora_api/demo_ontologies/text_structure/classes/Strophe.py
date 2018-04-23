#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Paragraph import Paragraph
from ..properties.isStropheOf import IsStropheOf
from ..properties.structureHasUnit import StructureHasUnit
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Strophe

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Strophe(Paragraph):
    """
    Paragraph of verses as part of a poem.

    Labels: Strophe (de) / strophe (en)
    """
    def __init__(self, isStropheOf=None, structureHasUnit=None, **kwargs):
        """

        :param isStropheOf:
        :param structureHasUnit:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Strophe"

        self.isStropheOf = IsStropheOf(isStropheOf)
        self.structureHasUnit = StructureHasUnit(structureHasUnit)
