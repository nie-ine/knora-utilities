#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Organisation import Organisation as age_Organisation
from ...human.classes.Group import Group
from ..properties.hasRole import HasRole
from ..properties.actsIn import ActsIn
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class organisation:Organisation

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class Organisation(age_Organisation, Group):
    """
    Organized group of persons.

    Labels: Personensorganisation (de) / person organisation (en)
    """
    def __init__(self, hasRole=None, actsIn=None, **kwargs):
        """

        :param hasRole:
        :param actsIn:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Organisation"

        self.hasRole = HasRole(hasRole)
        self.actsIn = ActsIn(actsIn)
