#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Publication import Publication
from ...information_carrier.classes.NachlassElement import NachlassElement
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:NachlassPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class NachlassPublication(Publication, NachlassElement):
    """
    Publication of a nachlass.

    Labels: Nachlassausgabe (de) / nachlass publication (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NachlassPublication"
