#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Expression import Expression
from ...human.classes.CreationDerivative import CreationDerivative
from ..properties.hasColumnIndicator import HasColumnIndicator
from ..properties.hasDiacriticalSign import HasDiacriticalSign
from ..properties.hasPageNumberIndicator import HasPageNumberIndicator
from ..properties.hasPageIndicator import HasPageIndicator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:Derivative

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class Derivative(Expression, CreationDerivative):
    """
    Text expression derived from another text expression.

    Labels: abgeleitete Text (de) / text derivative (en)
    """
    def __init__(self, hasColumnIndicator=None, hasDiacriticalSign=None, hasPageNumberIndicator=None, hasPageIndicator=None, **kwargs):
        """

        :param hasColumnIndicator:
        :param hasDiacriticalSign:
        :param hasPageNumberIndicator:
        :param hasPageIndicator:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Derivative"

        self.hasColumnIndicator = HasColumnIndicator(hasColumnIndicator)
        self.hasDiacriticalSign = HasDiacriticalSign(hasDiacriticalSign)
        self.hasPageNumberIndicator = HasPageNumberIndicator(hasPageNumberIndicator)
        self.hasPageIndicator = HasPageIndicator(hasPageIndicator)
