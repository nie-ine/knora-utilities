#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ElectronicPublication import ElectronicPublication
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:WebPage

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class WebPage(ElectronicPublication):
    """
    Electronically published page on the World Wide Web.

    Labels: Webseite (de) / web page (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "WebPage"
