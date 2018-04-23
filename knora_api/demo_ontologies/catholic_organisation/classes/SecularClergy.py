#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Organisation import Organisation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class catholic-organisation:SecularClergy

created at: 2018-04-19 14:07:12
created from: catholic-organisation-ontology-knora.ttl
"""


class SecularClergy(Organisation):
    """
    Catholic organisation whose member does not belong to a catholic order.

    Label: secular clergy (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "SecularClergy"
