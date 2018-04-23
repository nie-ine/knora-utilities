#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Machine import Machine
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:ElectricMachine

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class ElectricMachine(Machine):
    """
    Machine using electric potential energy to convert it via electrical
    current to kinetic energy to perform a task.

    Labels: elektrische Maschine (de) / electric machine (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ElectricMachine"
