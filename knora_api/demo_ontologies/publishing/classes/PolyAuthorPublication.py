#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Publication import Publication
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:PolyAuthorPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class PolyAuthorPublication(Publication):
    """
    Publication of different expressions by different authors.

    Labels: Mehrautorenpublikation (de) / poly-author publication (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PolyAuthorPublication"
