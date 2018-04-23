#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ..properties.hasReceiver import HasReceiver
from ..properties.hasSender import HasSender
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Letter

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Letter(Carrier):
    """
    Written text on a leaf intended to be sent from (a) person(s) or (an)
    Organisation(s) to another one, e.g. through a postal system.

    Labels: Brief (de) / letter (en)
    """
    def __init__(self, hasReceiver=None, hasSender=None, **kwargs):
        """

        :param hasReceiver:
        :param hasSender:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Letter"

        self.hasReceiver = HasReceiver(hasReceiver)
        self.hasSender = HasSender(hasSender)
