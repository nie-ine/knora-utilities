#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Publisher import Publisher
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:NewspaperPublisher

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class NewspaperPublisher(Publisher):
    """
    Publisher of a newspaper.

    Labels: Zeitungsverleger (de) / newspaper publisher (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NewspaperPublisher"
