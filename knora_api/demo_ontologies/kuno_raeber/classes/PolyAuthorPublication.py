#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...publishing.classes.PolyAuthorPublication import PolyAuthorPublication as pub_PolyAuthorPublication
from ..properties.hasContentPartInPolyAuthorPublicationConvolute import HasContentPartInPolyAuthorPublicationConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PolyAuthorPublication

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PolyAuthorPublication(pub_PolyAuthorPublication):
    """
    Publication of a poem authored by Kuno Raeber among expressions by other
    authors.

    Labels: Mehrautorenpublikationen (de) / poly-author publication (en)
    """
    def __init__(self, hasContentPartInPolyAuthorPublicationConvolute=None, **kwargs):
        """

        :param hasContentPartInPolyAuthorPublicationConvolute:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PolyAuthorPublication"

        self.hasContentPartInPolyAuthorPublicationConvolute = HasContentPartInPolyAuthorPublicationConvolute(hasContentPartInPolyAuthorPublicationConvolute)
