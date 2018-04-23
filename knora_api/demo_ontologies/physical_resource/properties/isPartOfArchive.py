#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isPartOf import IsPartOf

"""
definition of property physical-resource:IsPartOfArchive

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsPartOfArchive(IsPartOf):
    """
    Relating an element of an archive to the archive.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "isPartOfArchive"
