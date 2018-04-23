#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:Language

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class Language(Resource):
    """
     to express meaning using carriers (e.g. a symbol, sign, word) along rules
    or grammar model, e.g. syntax for serialization.

    Labels: Sprache (de) / language (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Language"
