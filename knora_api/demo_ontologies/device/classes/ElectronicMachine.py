#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ElectricMachine import ElectricMachine
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:ElectronicMachine

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class ElectronicMachine(ElectricMachine):
    """
    Electric machine manipulating the motion of electrons in an electrical
    current in ways that add meaningful information to the current, to perform a
    task.

    Labels: elektronische Maschine (de) / electronic machine (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ElectronicMachine"
