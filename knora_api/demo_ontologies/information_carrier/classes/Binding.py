#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ..properties.isBindingOf import IsBindingOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Binding

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Binding(Carrier):
    """
    Material holding the leafs and covers of a book together.

    Labels: Einband (de) / binding (en)
    """
    def __init__(self, isBindingOf=None, **kwargs):
        """

        :param isBindingOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Binding"

        self.isBindingOf = IsBindingOf(isBindingOf)
