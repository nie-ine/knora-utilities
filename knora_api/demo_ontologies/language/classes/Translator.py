#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:Translator

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class Translator(Role):
    """
    Role of an agent transferring a human natural language expression in
    another natural language.

    Labels: Übersetzer (de) / translator (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Translator"
