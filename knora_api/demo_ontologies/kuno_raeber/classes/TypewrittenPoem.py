#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Poem import Poem
from ...text.classes.TypewrittenText import TypewrittenText
from ...information_carrier.properties.hasPageNumberDescription import HasPageNumberDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:TypewrittenPoem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class TypewrittenPoem(Poem, TypewrittenText):
    """
    Maschinengeschriebenes Gedicht von Kuno Raeber.

    Labels: maschinengeschriebenes Gedicht (de) / typewritten poem (en)
    """
    def __init__(self, hasPageNumberDescription=None, **kwargs):
        """

        :param hasPageNumberDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "TypewrittenPoem"

        self.hasPageNumberDescription = HasPageNumberDescription(hasPageNumberDescription)
