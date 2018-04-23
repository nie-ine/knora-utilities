#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Organisation import Organisation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class organisation:Administration

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class Administration(Organisation):
    """
    Organisation administering a group of people on any level, e.g.
    international, national, regional or city level.

    Labels: Verwaltung (de) / administration (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Administration"
