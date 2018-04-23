#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.CreationVersion import CreationVersion
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Draft

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Draft(CreationVersion):
    """
    Developmental text expression.

    Labels: Entwurf (de) / draft (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Draft"
