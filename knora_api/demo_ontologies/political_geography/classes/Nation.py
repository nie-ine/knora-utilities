#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...organisation.classes.PoliticalOrganization import PoliticalOrganization
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:Nation

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class Nation(PoliticalOrganization):
    """
    Stable political organization with a commonality e.g. ethnicity, language,
    culture, .

    Labels: Nation (de) / nation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Nation"
