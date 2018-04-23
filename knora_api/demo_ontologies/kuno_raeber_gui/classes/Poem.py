#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ..properties.hasPublishingStateIndex import HasPublishingStateIndex
from ..properties.hasSameEditionAs import HasSameEditionAs
from ..properties.hasConvoluteTitle import HasConvoluteTitle
from ..properties.hasCreationYear import HasCreationYear
from ...knora_base.properties.seqnum import Seqnum
from ..properties.hasStrophe import HasStrophe
from ..properties.hasNachlassIndex import HasNachlassIndex
from ..properties.hasFictitiousCreationDate import HasFictitiousCreationDate
from ..properties.isOnPage import IsOnPage
from ..properties.hasPoemTitle import HasPoemTitle
from ..properties.isWrittenWith import IsWrittenWith
from ..properties.hasStructure import HasStructure
from ..properties.hasPoemCreationDate import HasPoemCreationDate
from ..properties.hasPoemText import HasPoemText
from ..properties.isPartOfCycle import IsPartOfCycle
from ..properties.hasPageNumber import HasPageNumber
from ..properties.hasConvoluteIRI import HasConvoluteIRI
from ..properties.hasSynopsisIRI import HasSynopsisIRI
from ..properties.isInDialect import IsInDialect
from ..properties.hasAlphabeticIndex import HasAlphabeticIndex
from ..properties.isFinalVersion import IsFinalVersion
from ..properties.hasRhyme import HasRhyme
from ..properties.hasPoemIRI import HasPoemIRI
from ..properties.hasSupersedingNumber import HasSupersedingNumber
from ..properties.hasSynopsisTitle import HasSynopsisTitle
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber-gui:Poem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-gui-ontology-knora.ttl
"""


class Poem(Resource):
    """
    Gedicht von Kuno Raeber.

    Labels: Gedicht (de) / poem (en)
    """
    def __init__(self, hasPublishingStateIndex=None, hasSameEditionAs=None, hasConvoluteTitle=None, hasCreationYear=None, seqnum=None, hasStrophe=None, hasNachlassIndex=None, hasFictitiousCreationDate=None, isOnPage=None, hasPoemTitle=None, isWrittenWith=None, hasStructure=None, hasPoemCreationDate=None, hasPoemText=None, isPartOfCycle=None, hasPageNumber=None, hasConvoluteIRI=None, hasSynopsisIRI=None, isInDialect=None, hasAlphabeticIndex=None, isFinalVersion=None, hasRhyme=None, hasPoemIRI=None, hasSupersedingNumber=None, hasSynopsisTitle=None, **kwargs):
        """

        :param hasPublishingStateIndex:
        :param hasSameEditionAs:
        :param hasConvoluteTitle:
        :param hasCreationYear:
        :param seqnum:
        :param hasStrophe:
        :param hasNachlassIndex:
        :param hasFictitiousCreationDate:
        :param isOnPage:
        :param hasPoemTitle:
        :param isWrittenWith:
        :param hasStructure:
        :param hasPoemCreationDate:
        :param hasPoemText:
        :param isPartOfCycle:
        :param hasPageNumber:
        :param hasConvoluteIRI:
        :param hasSynopsisIRI:
        :param isInDialect:
        :param hasAlphabeticIndex:
        :param isFinalVersion:
        :param hasRhyme:
        :param hasPoemIRI:
        :param hasSupersedingNumber:
        :param hasSynopsisTitle:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Poem"

        self.hasPublishingStateIndex = HasPublishingStateIndex(hasPublishingStateIndex)
        self.hasSameEditionAs = HasSameEditionAs(hasSameEditionAs)
        self.hasConvoluteTitle = HasConvoluteTitle(hasConvoluteTitle)
        self.hasCreationYear = HasCreationYear(hasCreationYear)
        self.seqnum = Seqnum(seqnum)
        self.hasStrophe = HasStrophe(hasStrophe)
        self.hasNachlassIndex = HasNachlassIndex(hasNachlassIndex)
        self.hasFictitiousCreationDate = HasFictitiousCreationDate(hasFictitiousCreationDate)
        self.isOnPage = IsOnPage(isOnPage)
        self.hasPoemTitle = HasPoemTitle(hasPoemTitle)
        self.isWrittenWith = IsWrittenWith(isWrittenWith)
        self.hasStructure = HasStructure(hasStructure)
        self.hasPoemCreationDate = HasPoemCreationDate(hasPoemCreationDate)
        self.hasPoemText = HasPoemText(hasPoemText)
        self.isPartOfCycle = IsPartOfCycle(isPartOfCycle)
        self.hasPageNumber = HasPageNumber(hasPageNumber)
        self.hasConvoluteIRI = HasConvoluteIRI(hasConvoluteIRI)
        self.hasSynopsisIRI = HasSynopsisIRI(hasSynopsisIRI)
        self.isInDialect = IsInDialect(isInDialect)
        self.hasAlphabeticIndex = HasAlphabeticIndex(hasAlphabeticIndex)
        self.isFinalVersion = IsFinalVersion(isFinalVersion)
        self.hasRhyme = HasRhyme(hasRhyme)
        self.hasPoemIRI = HasPoemIRI(hasPoemIRI)
        self.hasSupersedingNumber = HasSupersedingNumber(hasSupersedingNumber)
        self.hasSynopsisTitle = HasSynopsisTitle(hasSynopsisTitle)
