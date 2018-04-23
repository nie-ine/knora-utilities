#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...philosophy.classes.Metaphysics import Metaphysics
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class philosophies:Nominalism

created at: 2018-04-19 14:07:12
created from: philosophies-ontology-knora.ttl
"""


class Nominalism(Metaphysics):
    """
    Phylosophy stating that only individual things exist, denying the existence
    of universals and abstract objects.

    Label: Nominalism (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Nominalism"
