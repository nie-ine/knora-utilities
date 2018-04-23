#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Diary

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Diary(Carrier):
    """
    information carrier with periodically, usually daily, described personal
    experiences and observations.

    Labels: Tagebuch (de) / diary (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Diary"
