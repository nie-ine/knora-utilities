#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Stage

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Stage(Resource):
    """
    Extent of a process.

    Labels: Stufe (de) / stage (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Stage"
