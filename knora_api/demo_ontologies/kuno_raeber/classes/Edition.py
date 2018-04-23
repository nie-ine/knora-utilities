#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.classes.Edition import Edition as tex_Edition
from ...text.properties.hasContent import HasContent
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Edition

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Edition(tex_Edition):
    """
    Edition eines von Kuno Raeber verfassten Texts.

    Labels: edierte Text (de) / edited text (en)
    """
    def __init__(self, hasContent=None, **kwargs):
        """

        :param hasContent:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Edition"

        self.hasContent = HasContent(hasContent)
