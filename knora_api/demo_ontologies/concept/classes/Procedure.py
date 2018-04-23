#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Information import Information
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:Procedure

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class Procedure(Information):
    """
    Plan to perform an action in one or more steps, in a certain manner to
    obtain a certain output under certain circumstances.

    Labels: Vorgehen (de) / procedure (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Procedure"
