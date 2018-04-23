#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ...physical_resource.properties.isPartOfNachlass import IsPartOfNachlass
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:NachlassElement

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class NachlassElement(Carrier):
    """
    Element of a nachlass.

    Labels: Nachlass-Element (de) / nachlass element (en)
    """
    def __init__(self, isPartOfNachlass=None, **kwargs):
        """

        :param isPartOfNachlass:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NachlassElement"

        self.isPartOfNachlass = IsPartOfNachlass(isPartOfNachlass)
