#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.CriticalThoughtMethod import CriticalThoughtMethod
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Scholasticism

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Scholasticism(CriticalThoughtMethod):
    """
    Method of critical thought dominating theological and philosophical study
    in Western Christianity and teaching by academics or scholastics (schoolmen)
    of universities in Europe from about 1100 to 1700.

    Labels: Scholastik (de) / scholasticism (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Scholasticism"
