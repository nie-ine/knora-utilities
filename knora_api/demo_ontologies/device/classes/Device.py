#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.PhysicalCreation import PhysicalCreation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class device:Device

created at: 2018-04-19 14:07:12
created from: device-ontology-knora.ttl
"""


class Device(PhysicalCreation):
    """
    Physical creation serving a particular purpose.

    Labels: Gerät (de) / device (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Device"
