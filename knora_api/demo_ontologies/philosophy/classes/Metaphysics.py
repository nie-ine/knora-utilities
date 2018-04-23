#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Philosophy import Philosophy
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class philosophy:Metaphysics

created at: 2018-04-19 14:07:12
created from: philosophy-ontology-knora.ttl
"""


class Metaphysics(Philosophy):
    """
    .

    Labels: Metaphysik (de) / metaphysics (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Metaphysics"
