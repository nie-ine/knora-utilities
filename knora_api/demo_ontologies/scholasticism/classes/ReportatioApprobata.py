#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CommentaryMethod import CommentaryMethod
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:ReportatioApprobata

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class ReportatioApprobata(CommentaryMethod):
    """
    Scholastic commentary on a text as student recordings approved by the
    master.

    Label: reportatio approbata (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ReportatioApprobata"
