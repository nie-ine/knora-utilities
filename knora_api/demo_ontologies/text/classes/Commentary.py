#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Expression import Expression
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Commentary

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Commentary(Expression):
    """
    Text expression in the form of a series of comments as analysis,
    interpretation or explanation of something, especially another textual expression.

    Labels: Kommentar (de) / commentary (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Commentary"
