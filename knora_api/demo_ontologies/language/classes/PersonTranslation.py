#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.CreationDerivative import CreationDerivative
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class language:PersonTranslation

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class PersonTranslation(CreationDerivative):
    """
    Translation done by a person.

    Labels: Übersetzung einer Person (de) / person's translation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PersonTranslation"
