#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CommentaryMethod import CommentaryMethod
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:LecturaRevisa

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class LecturaRevisa(CommentaryMethod):
    """
    Scholastic commentary on a text as revised by its author after its
    presentation in a lecture.

    Label: lectura revisa (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "LecturaRevisa"
