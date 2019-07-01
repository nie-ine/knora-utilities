#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Resource import Resource

"""
definition of class knora-base:DocumentRepresentation
"""


class DocumentRepresentation(Resource):
    """

    """

    _ontology = "http://www.knora.org/ontology"
    _project_prefix = "http://rdfh.ch/projects"

    def __init__(self, label, seqnum=None, file=None):
        self._namespace = "http://www.knora.org/ontology/knora-base"
        self._project_id = None
        self._name = "DocumentRepresentation"
        self._label = label
        self._file = file
        self.seqnum = seqnum
