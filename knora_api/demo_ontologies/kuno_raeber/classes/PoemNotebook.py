#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Manuscript import Manuscript
from .Convolute import Convolute
from ...information_carrier.classes.ArchiveElement import ArchiveElement
from ...information_carrier.classes.Notebook import Notebook
from ...information_carrier.properties.carrierHasDescription import CarrierHasDescription
from ..properties.containsEarlierStagesOfTypescriptConvolute import ContainsEarlierStagesOfTypescriptConvolute
from ..properties.containsEarlierStagesOfManuscriptConvolute import ContainsEarlierStagesOfManuscriptConvolute
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ...human.properties.hasCreating import HasCreating
from ...information_carrier.properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemNotebook

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemNotebook(Manuscript, Convolute, ArchiveElement, Notebook):
    """
    Notebook with poem drafts authored by Kuno Raeber.

    Labels: Gedichten-Notizbuch (de) / poem notebook (en)
    """
    def __init__(self, carrierHasDescription=None, containsEarlierStagesOfTypescriptConvolute=None, containsEarlierStagesOfManuscriptConvolute=None, hasArchiveSignature=None, hasCreating=None, convoluteHasSizeDescription=None, **kwargs):
        """

        :param carrierHasDescription:
        :param containsEarlierStagesOfTypescriptConvolute:
        :param containsEarlierStagesOfManuscriptConvolute:
        :param hasArchiveSignature:
        :param hasCreating:
        :param convoluteHasSizeDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemNotebook"

        self.carrierHasDescription = CarrierHasDescription(carrierHasDescription)
        self.containsEarlierStagesOfTypescriptConvolute = ContainsEarlierStagesOfTypescriptConvolute(containsEarlierStagesOfTypescriptConvolute)
        self.containsEarlierStagesOfManuscriptConvolute = ContainsEarlierStagesOfManuscriptConvolute(containsEarlierStagesOfManuscriptConvolute)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.hasCreating = HasCreating(hasCreating)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
