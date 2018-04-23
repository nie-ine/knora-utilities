#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Edition import Edition
from ..properties.hasApparatus import HasApparatus
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:CriticalEdition

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class CriticalEdition(Edition):
    """
    Edition to which an editor added evidence and interpretation of a text
    creation and historical transmission, allowing readers to assess the editor's
    choice.

    Labels: kritische Textedition (de) / critical text edition (en)
    """
    def __init__(self, hasApparatus=None, **kwargs):
        """

        :param hasApparatus:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CriticalEdition"

        self.hasApparatus = HasApparatus(hasApparatus)
