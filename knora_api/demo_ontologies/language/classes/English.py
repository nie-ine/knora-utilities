#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .HumanNaturalLanguage import HumanNaturalLanguage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:English

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class English(HumanNaturalLanguage):
    """
    .

    Labels: Englisch (de) / English (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "English"
