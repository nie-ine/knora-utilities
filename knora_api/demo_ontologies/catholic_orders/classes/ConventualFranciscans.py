#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...catholic_organisation.classes.Franciscans import Franciscans
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class catholic-orders:ConventualFranciscans

created at: 2018-04-19 14:07:12
created from: catholic-orders-ontology-knora.ttl
"""


class ConventualFranciscans(Franciscans):
    """
    .

    Labels: Order of Conventual Franciscans (en) / Ordo Fratrum Minorum Conventualium (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ConventualFranciscans"
