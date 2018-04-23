#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Typescript

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Typescript(Carrier):
    """
    Carrier of a typewritten text expression.

    Labels: Typoskript (de) / typescript (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Typescript"
