#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creator import Creator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Glossator

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Glossator(Creator):
    """
    Role of a person adding texts or glosses to a text.

    Labels: Glossator (de) / glossator (en) / glossator (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Glossator"
