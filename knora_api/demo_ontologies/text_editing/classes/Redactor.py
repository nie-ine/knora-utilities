#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creator import Creator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:Redactor

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class Redactor(Creator):
    """
    Role of a person assembling (pieces of) texts to a new coherent text.

    Labels: Redactor (de) / redactor (en) / redactor (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Redactor"
