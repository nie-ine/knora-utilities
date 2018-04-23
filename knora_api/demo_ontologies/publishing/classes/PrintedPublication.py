#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Publication import Publication
from ...information_carrier.classes.Print import Print
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:PrintedPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class PrintedPublication(Publication, Print):
    """
    Publication as print.

    Labels: gedruckte Publikation (de) / printed publication (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PrintedPublication"
