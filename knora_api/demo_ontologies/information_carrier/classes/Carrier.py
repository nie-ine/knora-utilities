#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.PhysicalCreation import PhysicalCreation
from ..properties.carrierHasDescription import CarrierHasDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Carrier

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Carrier(PhysicalCreation):
    """
    Carrier of information created by a person.

    Labels: Informationsträger (de) / information carrier (en)
    """
    def __init__(self, carrierHasDescription=None, **kwargs):
        """

        :param carrierHasDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Carrier"

        self.carrierHasDescription = CarrierHasDescription(carrierHasDescription)
