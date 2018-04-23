#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.classes.Place import Place
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:City

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class City(Place):
    """
    Large town.

    Labels: Stadt (de) / city (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "City"
