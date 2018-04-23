#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ElectronicData import ElectronicData
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:ElectronicDocument

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ElectronicDocument(ElectronicData):
    """
    Document stored as electronic information.

    Labels: elektronisches Dokument (de) / electronic document (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ElectronicDocument"
