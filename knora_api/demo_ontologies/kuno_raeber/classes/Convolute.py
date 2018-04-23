#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Convolute import Convolute as inf_Convolute
from ...information_carrier.properties.convoluteHasTitle import ConvoluteHasTitle
from ...text.properties.hasComment import HasComment
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Convolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Convolute(inf_Convolute):
    """
    Convolute of which the elements are authored by Kuno Raeber.

    Labels: Konvolut (de) / convolute (en)
    """
    def __init__(self, convoluteHasTitle=None, hasComment=None, **kwargs):
        """

        :param convoluteHasTitle:
        :param hasComment:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Convolute"

        self.convoluteHasTitle = ConvoluteHasTitle(convoluteHasTitle)
        self.hasComment = HasComment(hasComment)
