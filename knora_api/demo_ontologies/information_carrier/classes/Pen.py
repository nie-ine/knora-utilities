#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .WritingUtensil import WritingUtensil
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Pen

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Pen(WritingUtensil):
    """
    Elongated cylindrical(-like) hollow object containing ink for writing or
    drawing.

    Labels: Tintenstift (de) / pen (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Pen"
