#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Teacher import Teacher
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class teaching:Lecturer

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class Lecturer(Teacher):
    """
    Role of a person who lectures.

    Labels: VorleserIn (de) / lecturer (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Lecturer"
