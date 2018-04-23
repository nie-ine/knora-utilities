#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.classes.Place import Place
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:Village

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class Village(Place):
    """
    Small place with political boundaries but without an own government.

    Labels: Dorf (de) / village (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Village"
