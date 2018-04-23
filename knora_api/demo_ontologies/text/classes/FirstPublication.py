#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...publishing.classes.Publication import Publication
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:FirstPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class FirstPublication(Publication):
    """
    Earliest publication of a tex expression.

    Labels: Erstausgabe (de) / first publication (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "FirstPublication"
