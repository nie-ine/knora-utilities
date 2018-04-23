#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .HumanNaturalLanguage import HumanNaturalLanguage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:Dialect

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class Dialect(HumanNaturalLanguage):
    """
    Regional variant of a standard language.

    Labels: Mundart (de) / dialect (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Dialect"
