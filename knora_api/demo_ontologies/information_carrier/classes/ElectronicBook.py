#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ElectronicDocument import ElectronicDocument
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:ElectronicBook

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ElectronicBook(ElectronicDocument):
    """
    Electronic document with a text structure as in a book.

    Labels: elektronisches Buch (de) / electronic book (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ElectronicBook"
