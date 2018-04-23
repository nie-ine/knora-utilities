#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...scholasticism.classes.Commentary import Commentary as sch_Commentary
from ..properties.hasStegmuellerCommentaryDescription import HasStegmuellerCommentaryDescription
from ..properties.hasStegmuellerCode import HasStegmuellerCode
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class drcs:Commentary

created at: 2018-04-19 14:07:12
created from: drcs-ontology-knora.ttl
"""


class Commentary(sch_Commentary):
    """
    Commentary on Petrus Lombardus' Sentences.

    Labels: Kommentar (de) / commentary (en) / commentarius (la)
    """
    def __init__(self, hasStegmuellerCommentaryDescription=None, hasStegmuellerCode=None, **kwargs):
        """

        :param hasStegmuellerCommentaryDescription:
        :param hasStegmuellerCode:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Commentary"

        self.hasStegmuellerCommentaryDescription = HasStegmuellerCommentaryDescription(hasStegmuellerCommentaryDescription)
        self.hasStegmuellerCode = HasStegmuellerCode(hasStegmuellerCode)
