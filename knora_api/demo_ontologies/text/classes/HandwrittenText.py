#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .WrittenText import WrittenText
from ...information_carrier.properties.isInManuscript import IsInManuscript
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:HandwrittenText

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HandwrittenText(WrittenText):
    """
    Text written by hand.

    Labels: handgeschriebener Text (de) / handwritten text (en)
    """
    def __init__(self, isInManuscript=None, **kwargs):
        """

        :param isInManuscript:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "HandwrittenText"

        self.isInManuscript = IsInManuscript(isInManuscript)
