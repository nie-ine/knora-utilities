#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.WrittenText import WrittenText
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Literature

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Literature(WrittenText):
    """
    Written text as art.

    Labels: Literatur (de) / literature (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Literature"
