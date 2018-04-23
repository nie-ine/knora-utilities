#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Human import Human
from ..properties.hasFloruit import HasFloruit
from ..properties.hasBirthDate import HasBirthDate
from ..properties.adheringToThought import AdheringToThought
from ..properties.hasName import HasName
from ..properties.isMemberOfGroup import IsMemberOfGroup
from ..properties.personHasRole import PersonHasRole
from ..properties.hasFamilyName import HasFamilyName
from ..properties.hasPreferredName import HasPreferredName
from ...organisation.properties.isMemberOfOrganisation import IsMemberOfOrganisation
from ..properties.hasGivenName import HasGivenName
from ..properties.hasDescription import HasDescription
from ..properties.hasAlias import HasAlias
from ..properties.personHasLife import PersonHasLife
from ..properties.hasDeathDate import HasDeathDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Person

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Person(Human):
    """
    A real born living human.

    Labels: Person (de) / person (en) / personne (fr) / persona (it)
    """
    def __init__(self, hasFloruit=None, hasBirthDate=None, adheringToThought=None, hasName=None, isMemberOfGroup=None, personHasRole=None, hasFamilyName=None, hasPreferredName=None, isMemberOfOrganisation=None, hasGivenName=None, hasDescription=None, hasAlias=None, personHasLife=None, hasDeathDate=None, **kwargs):
        """

        :param hasFloruit:
        :param hasBirthDate:
        :param adheringToThought:
        :param hasName:
        :param isMemberOfGroup:
        :param personHasRole:
        :param hasFamilyName:
        :param hasPreferredName:
        :param isMemberOfOrganisation:
        :param hasGivenName:
        :param hasDescription:
        :param hasAlias:
        :param personHasLife:
        :param hasDeathDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Person"

        self.hasFloruit = HasFloruit(hasFloruit)
        self.hasBirthDate = HasBirthDate(hasBirthDate)
        self.adheringToThought = AdheringToThought(adheringToThought)
        self.hasName = HasName(hasName)
        self.isMemberOfGroup = IsMemberOfGroup(isMemberOfGroup)
        self.personHasRole = PersonHasRole(personHasRole)
        self.hasFamilyName = HasFamilyName(hasFamilyName)
        self.hasPreferredName = HasPreferredName(hasPreferredName)
        self.isMemberOfOrganisation = IsMemberOfOrganisation(isMemberOfOrganisation)
        self.hasGivenName = HasGivenName(hasGivenName)
        self.hasDescription = HasDescription(hasDescription)
        self.hasAlias = HasAlias(hasAlias)
        self.personHasLife = PersonHasLife(personHasLife)
        self.hasDeathDate = HasDeathDate(hasDeathDate)
