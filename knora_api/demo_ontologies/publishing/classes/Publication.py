#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Carrier import Carrier
from ..properties.hasPublisher import HasPublisher
from ..properties.hasDescription import HasDescription
from ..properties.hasPublisherDescription import HasPublisherDescription
from ..properties.hasDate import HasDate
from ..properties.hasTitle import HasTitle
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:Publication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class Publication(Carrier):
    """
    An expression published on a carrier.

    Labels: Publikation (de) / publication (en)
    """
    def __init__(self, hasPublisher=None, hasDescription=None, hasPublisherDescription=None, hasDate=None, hasTitle=None, **kwargs):
        """

        :param hasPublisher:
        :param hasDescription:
        :param hasPublisherDescription:
        :param hasDate:
        :param hasTitle:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Publication"

        self.hasPublisher = HasPublisher(hasPublisher)
        self.hasDescription = HasDescription(hasDescription)
        self.hasPublisherDescription = HasPublisherDescription(hasPublisherDescription)
        self.hasDate = HasDate(hasDate)
        self.hasTitle = HasTitle(hasTitle)
