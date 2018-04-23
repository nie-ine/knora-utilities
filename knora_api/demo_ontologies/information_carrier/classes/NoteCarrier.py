#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:NoteCarrier

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class NoteCarrier(Carrier):
    """
    Carrier whereon notes are written, e.g. a first registration of thoughts.

    Labels: Notizträger (de) / note carrier (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NoteCarrier"
