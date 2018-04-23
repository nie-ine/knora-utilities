#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Author import Author
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Poet

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Poet(Author):
    """
    Author of a poem.

    Labels: Dichter (de) / poet (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Poet"
