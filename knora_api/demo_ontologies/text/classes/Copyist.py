#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creator import Creator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Copyist

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Copyist(Creator):
    """
    Role of a person copying text by handwriting.

    Labels: Kopist (de) / copyist (en) / scribes (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Copyist"
