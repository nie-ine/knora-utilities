#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Role import Role as hum_Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Role

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Role(hum_Role):
    """
    A role a scholastic has.

    Label: scholastic role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Role"
