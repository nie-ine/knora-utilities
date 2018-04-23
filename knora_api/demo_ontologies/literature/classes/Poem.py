#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Lyric import Lyric
from ...text.classes.Expression import Expression
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Poem

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Poem(Lyric, Expression):
    """
    Poetic expression.

    Labels: Gedicht (de) / poem (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Poem"
