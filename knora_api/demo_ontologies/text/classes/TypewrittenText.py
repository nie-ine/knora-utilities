#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .WrittenText import WrittenText
from ...information_carrier.properties.isInTypescript import IsInTypescript
from ...information_carrier.properties.isWrittenWith import IsWrittenWith
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:TypewrittenText

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class TypewrittenText(WrittenText):
    """
    Text written with a typewriter.

    Labels: maschinengeschriebener Text (de) / typewritten text (en)
    """
    def __init__(self, isInTypescript=None, isWrittenWith=None, **kwargs):
        """

        :param isInTypescript:
        :param isWrittenWith:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "TypewrittenText"

        self.isInTypescript = IsInTypescript(isInTypescript)
        self.isWrittenWith = IsWrittenWith(isWrittenWith)
