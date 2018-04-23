#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Work import Work
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:IndividualWork

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class IndividualWork(Work):
    """
    Work as a complete whole realised in one self-contained expression.

    Labels: individuelles Werk (de) / individual work (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "IndividualWork"
