#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .FinalVersion import FinalVersion
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:IntendedFinalVersion

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class IntendedFinalVersion(FinalVersion):
    """
    Person's creation as intended last version, e.g. of a development.

    Labels: beabsichtigte Endversion (de) / intended final version (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "IntendedFinalVersion"
