#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Derivative import Derivative
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:Edition

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class Edition(Derivative):
    """
    Changed form of a text expression as a result of editing.

    Labels: Text-Edition (de) / text edition (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Edition"
