#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Page import Page as inf_Page
from ...information_carrier.properties.pageHasNumber import PageHasNumber
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Page

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Page(inf_Page):
    """
    Page with a handwritten poem by Kuno Raeber.

    Labels: Seite (de) / page (en)
    """
    def __init__(self, pageHasNumber=None, **kwargs):
        """

        :param pageHasNumber:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Page"

        self.pageHasNumber = PageHasNumber(pageHasNumber)
