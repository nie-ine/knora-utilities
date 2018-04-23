#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Device import Device
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:Machine

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class Machine(Device):
    """
    Device having more than one part, each with a function, and transmitting a
    force or directing its application to perform a task.

    Labels: Maschine (de) / machine (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Machine"
