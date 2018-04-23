#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ..properties.isPageOf import IsPageOf
from ..properties.isPageOfBook import IsPageOfBook
from ..properties.pageHasNumber import PageHasNumber
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Page

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Page(Carrier):
    """
    One of the 2 surfaces of a leaf, e.g. a manuscript, or of a leaf of a book.

    Labels: Seite (de) / page (en)
    """
    def __init__(self, isPageOf=None, isPageOfBook=None, pageHasNumber=None, **kwargs):
        """

        :param isPageOf:
        :param isPageOfBook:
        :param pageHasNumber:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Page"

        self.isPageOf = IsPageOf(isPageOf)
        self.isPageOfBook = IsPageOfBook(isPageOfBook)
        self.pageHasNumber = PageHasNumber(pageHasNumber)
