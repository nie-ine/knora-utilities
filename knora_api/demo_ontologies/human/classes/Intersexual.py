#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .BiologicalSex import BiologicalSex
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Intersexual

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Intersexual(BiologicalSex):
    """
    Being of a sex that is neither male nor female, with biological
    characteristics of both.

    Labels: menschlich intersexual (de) / human intersexual (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Intersexual"
