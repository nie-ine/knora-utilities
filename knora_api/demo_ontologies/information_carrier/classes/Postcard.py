#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creation import Creation
from ..properties.hasReceiver import HasReceiver
from ..properties.hasSender import HasSender
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Postcard

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Postcard(Creation):
    """
    Card with one side, usually with a printed structure, used for writing a
    message, an address and applying a postage stamp, to be sent through a postal
    system.

    Labels: Postkarte (de) / postcard (en)
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
        self._name = "Postcard"

        self.hasReceiver = HasReceiver(hasReceiver)
        self.hasSender = HasSender(hasSender)
