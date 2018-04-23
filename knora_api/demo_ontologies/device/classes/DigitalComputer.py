#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ElectronicMachine import ElectronicMachine
from ...information_carrier.classes.DigitalCarrier import DigitalCarrier
from .Computer import Computer
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:DigitalComputer

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class DigitalComputer(ElectronicMachine, DigitalCarrier, Computer):
    """
    Electronic computer using digital software and data to perform a task.

    Labels: digitale Rechner (de) / digital computer (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DigitalComputer"
