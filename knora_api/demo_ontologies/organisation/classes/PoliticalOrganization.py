#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Organisation import Organisation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class organisation:PoliticalOrganization

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class PoliticalOrganization(Organisation):
    """
    .

    Labels: politische Organisation (de) / political organization (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoliticalOrganization"
