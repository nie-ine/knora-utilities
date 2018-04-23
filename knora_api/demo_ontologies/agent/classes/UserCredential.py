#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ...event.classes.Input import Input
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:UserCredential

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class UserCredential(Resource, Input):
    """
    Convincible information as input to get user access, e.g. to a digital
    multiuser computer system.

    Label: user credential (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "UserCredential"
