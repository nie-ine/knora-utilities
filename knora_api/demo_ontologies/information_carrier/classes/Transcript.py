#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Transcript

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Transcript(Carrier):
    """
    Carrier of a reproduced text by any method, e.g. handwriting, typewriting,
    machine copying, printing, digitizing.

    Labels: Abschrift (de) / transcript (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Transcript"
