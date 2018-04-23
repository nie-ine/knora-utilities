#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.classes.Space import Space
from ...physical_resource.classes.Time import Time
from ..properties.hasName import HasName
from ..properties.hasStartDate import HasStartDate
from ..properties.hasEndDate import HasEndDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Event

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Event(Space, Time):
    """
    Occurrence as a space-time thing.

    Labels: Ereignis (de) / event (en)
    """
    def __init__(self, hasName=None, hasStartDate=None, hasEndDate=None, **kwargs):
        """

        :param hasName:
        :param hasStartDate:
        :param hasEndDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Event"

        self.hasName = HasName(hasName)
        self.hasStartDate = HasStartDate(hasStartDate)
        self.hasEndDate = HasEndDate(hasEndDate)
