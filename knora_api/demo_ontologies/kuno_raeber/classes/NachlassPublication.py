#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...publishing.classes.NachlassPublication import NachlassPublication as pub_NachlassPublication
from ...publishing.classes.PrintedPublication import PrintedPublication
from ...information_carrier.classes.Volume import Volume
from ...publishing.properties.hasTitle import HasTitle
from ...publishing.properties.hasPublisherDescription import HasPublisherDescription
from ...information_carrier.properties.volumeHasNumber import VolumeHasNumber
from ...publishing.properties.hasDate import HasDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:NachlassPublication

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class NachlassPublication(pub_NachlassPublication, PrintedPublication, Volume):
    """
    Publication of a Nachlass of Kuno Raeber.

    Labels: Nachlass-Publication (de) / nachlass publication (en)
    """
    def __init__(self, hasTitle=None, hasPublisherDescription=None, volumeHasNumber=None, hasDate=None, **kwargs):
        """

        :param hasTitle:
        :param hasPublisherDescription:
        :param volumeHasNumber:
        :param hasDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NachlassPublication"

        self.hasTitle = HasTitle(hasTitle)
        self.hasPublisherDescription = HasPublisherDescription(hasPublisherDescription)
        self.volumeHasNumber = VolumeHasNumber(volumeHasNumber)
        self.hasDate = HasDate(hasDate)
