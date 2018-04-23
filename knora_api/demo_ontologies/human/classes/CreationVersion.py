#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Creation import Creation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:CreationVersion

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class CreationVersion(Creation):
    """
    Person's creation differing in certain respects - e.g. time, extent - from
    onther e.g. earlier or standard one.

    Labels: Version einer Kreation (de) / creation version (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CreationVersion"
