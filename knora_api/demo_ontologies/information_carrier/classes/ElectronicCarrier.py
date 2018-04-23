#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...device.classes.ElectronicMachine import ElectronicMachine
from .Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:ElectronicCarrier

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ElectronicCarrier(ElectronicMachine, Carrier):
    """
    Electronic device carrying information.

    Labels: elektronischer Informationsträger (de) / electronic information carrier (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ElectronicCarrier"
