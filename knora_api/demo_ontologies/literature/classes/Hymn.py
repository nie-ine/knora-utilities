#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .VersePoem import VersePoem
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Hymn

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Hymn(VersePoem):
    """
    Poetic expression of adoration for a deity or prominent person.

    Labels: Hymne (de) / hymn (en) / hymnus (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Hymn"
