#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creator import Creator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Abbreviator

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Abbreviator(Creator):
    """
    Role of a person being responsible for a shortened version of a text.

    Labels: Abkürzer (de) / abbreviator (en) / abbreviator (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Abbreviator"
