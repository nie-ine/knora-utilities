#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Machine import Machine
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:Computer

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class Computer(Machine):
    """
    Machine using programmed instructions to perform arithmetic and logic
    operations automatically, to perform a task.

    Labels: Rechner (de) / computer (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Computer"
