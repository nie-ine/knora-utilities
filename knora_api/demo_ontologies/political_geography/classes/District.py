#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.classes.Place import Place
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:District

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class District(Place):
    """
    Part of a city with own administration.

    Labels: Stadtviertel (de) / district (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "District"
