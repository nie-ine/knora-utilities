#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Ability

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Ability(Resource):
    """
    Possibility of a person to do something.

    Labels: menschliche Fähigkeit (de) / human ability (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Ability"
