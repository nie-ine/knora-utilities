#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...organisation.classes.ReligiousOrganisation import ReligiousOrganisation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class catholic-organisation:Organisation

created at: 2018-04-19 14:07:12
created from: catholic-organisation-ontology-knora.ttl
"""


class Organisation(ReligiousOrganisation):
    """
    Organisation following a catholic belief.

    Label: catholic organisation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Organisation"
