#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creating import Creating
from ...event.properties.hasStage import HasStage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Development

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Development(Creating):
    """
    Action wherein a person(s) creates text resulting in different
    manifestation, e.g. from notebook to manuscript to typescript to published print.

    Labels: Text-Entwicklung (de) / text development (en)
    """
    def __init__(self, hasStage=None, **kwargs):
        """

        :param hasStage:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Development"

        self.hasStage = HasStage(hasStage)
