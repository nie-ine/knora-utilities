#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Machine import Machine
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:MechanicalMachine

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class MechanicalMachine(Machine):
    """
    Machine using kinetic energy to perform a task.

    Labels: mechanische Maschine (de) / mechanical machine (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "MechanicalMachine"
