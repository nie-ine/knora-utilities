#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Resource import Resource
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Time

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Time(Resource):
    """
    .

    Labels: Zeit (de) / time (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Time"
