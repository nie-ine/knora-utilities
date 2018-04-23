#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from ...information_carrier.classes.Letter import Letter as inf_Letter
from ..properties.isPartOfLetterConvolute import IsPartOfLetterConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Letter

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Letter(ArchiveElement, inf_Letter):
    """
    Letter written by or to Kuno Raeber.

    Labels: Brief (de) / letter (en)
    """
    def __init__(self, isPartOfLetterConvolute=None, **kwargs):
        """

        :param isPartOfLetterConvolute:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Letter"

        self.isPartOfLetterConvolute = IsPartOfLetterConvolute(isPartOfLetterConvolute)
