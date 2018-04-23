#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ..properties.isMemberOf import IsMemberOf
from ..properties.hasRole import HasRole
from ..properties.actsIn import ActsIn
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:Agent

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class Agent(Resource):
    """
    Something that performs an action.

    Labels: Agent (de) / agent (en)
    """
    def __init__(self, isMemberOf=None, hasRole=None, actsIn=None, **kwargs):
        """

        :param isMemberOf:
        :param hasRole:
        :param actsIn:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Agent"

        self.isMemberOf = IsMemberOf(isMemberOf)
        self.hasRole = HasRole(hasRole)
        self.actsIn = ActsIn(actsIn)
