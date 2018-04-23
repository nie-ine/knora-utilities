#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ..properties.isOutputOf import IsOutputOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Output

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Output(Resource):
    """
    Consequence of a change in a process.

    Labels: Output (de) / output (en)
    """
    def __init__(self, isOutputOf=None, **kwargs):
        """

        :param isOutputOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Output"

        self.isOutputOf = IsOutputOf(isOutputOf)
