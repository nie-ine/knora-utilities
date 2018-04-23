#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Publication import Publication
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:Newspaper

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class Newspaper(Publication):
    """
    Periodical publication with most recent event descriptions as core content.

    Labels: Zeitung (de) / newspaper (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Newspaper"
