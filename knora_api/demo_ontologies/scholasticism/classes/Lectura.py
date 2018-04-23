#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CommentaryMethod import CommentaryMethod
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Lectura

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Lectura(CommentaryMethod):
    """
    Scholastic commentary on a text as presented by its author in an actual
    lecture.

    Label: lectura (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Lectura"
