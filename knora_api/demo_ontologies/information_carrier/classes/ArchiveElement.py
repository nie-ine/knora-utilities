#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ...physical_resource.properties.isPartOfArchive import IsPartOfArchive
from ..properties.hasArchiveSignature import HasArchiveSignature
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:ArchiveElement

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ArchiveElement(Carrier):
    """
    Element of an archive, which can be a single file or a file group.

    Labels: Archiv-Element (de) / archive element (en)
    """
    def __init__(self, isPartOfArchive=None, hasArchiveSignature=None, **kwargs):
        """

        :param isPartOfArchive:
        :param hasArchiveSignature:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ArchiveElement"

        self.isPartOfArchive = IsPartOfArchive(isPartOfArchive)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
