#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Person import Person
from ..properties.hasRole import HasRole
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Scholastic

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Scholastic(Person):
    """
    An adherent of Scholasticism.

    Labels: ScholastikerIn (de) / scholastic (en)
    """
    def __init__(self, hasRole=None, **kwargs):
        """

        :param hasRole:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Scholastic"

        self.hasRole = HasRole(hasRole)
