#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...organisation.classes.PoliticalOrganization import PoliticalOrganization
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:Empire

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class Empire(PoliticalOrganization):
    """
    Group of nations with an overarching government.

    Labels: Imperium (de) / empire (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Empire"
