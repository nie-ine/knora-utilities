#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:Publishing

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class Publishing(Action):
    """
    Action of making an expression public.

    Labels: herausgeben (de) / publishing (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Publishing"
