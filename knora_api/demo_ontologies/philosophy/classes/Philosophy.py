#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.ThoughtBody import ThoughtBody
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class philosophy:Philosophy

created at: 2018-04-19 14:07:12
created from: philosophy-ontology-knora.ttl
"""


class Philosophy(ThoughtBody):
    """
    .

    Labels: Philosophie (de) / philosophy (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Philosophy"
