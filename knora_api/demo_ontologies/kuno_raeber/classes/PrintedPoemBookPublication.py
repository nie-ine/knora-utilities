#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Convolute import Convolute
from ...publishing.classes.PrintedPublication import PrintedPublication
from ...information_carrier.classes.Book import Book
from ..properties.containsLaterStagesOfTypescriptConvolute import ContainsLaterStagesOfTypescriptConvolute
from ...information_carrier.properties.carrierHasDescription import CarrierHasDescription
from ..properties.containsLaterStagesOfManuscriptConvolute import ContainsLaterStagesOfManuscriptConvolute
from ...publishing.properties.hasDate import HasDate
from ...publishing.properties.hasTitle import HasTitle
from ..properties.containsLaterStagesOfNotebook import ContainsLaterStagesOfNotebook
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PrintedPoemBookPublication

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PrintedPoemBookPublication(Convolute, PrintedPublication, Book):
    """
    Printed publication of a book with poems authored by Kuno Raeber.

    Labels: gedruckte Gedichtenbuchausgabe (de) / printed poem book publication (en)
    """
    def __init__(self, containsLaterStagesOfTypescriptConvolute=None, carrierHasDescription=None, containsLaterStagesOfManuscriptConvolute=None, hasDate=None, hasTitle=None, containsLaterStagesOfNotebook=None, **kwargs):
        """

        :param containsLaterStagesOfTypescriptConvolute:
        :param carrierHasDescription:
        :param containsLaterStagesOfManuscriptConvolute:
        :param hasDate:
        :param hasTitle:
        :param containsLaterStagesOfNotebook:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PrintedPoemBookPublication"

        self.containsLaterStagesOfTypescriptConvolute = ContainsLaterStagesOfTypescriptConvolute(containsLaterStagesOfTypescriptConvolute)
        self.carrierHasDescription = CarrierHasDescription(carrierHasDescription)
        self.containsLaterStagesOfManuscriptConvolute = ContainsLaterStagesOfManuscriptConvolute(containsLaterStagesOfManuscriptConvolute)
        self.hasDate = HasDate(hasDate)
        self.hasTitle = HasTitle(hasTitle)
        self.containsLaterStagesOfNotebook = ContainsLaterStagesOfNotebook(containsLaterStagesOfNotebook)
