#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.classes.Output import Output
from ...text.properties.hasIdentifier import HasIdentifier
from ...text.properties.hasName import HasName
from ...text.properties.hasTitle import HasTitle
from ..properties.hasCreationDate import HasCreationDate
from ...text.properties.hasPreferredName import HasPreferredName
from ...text.properties.hasAlias import HasAlias
from ..properties.hasCreating import HasCreating
from ..properties.hasModificationDate import HasModificationDate
from ...text.properties.hasDescription import HasDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Creation

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Creation(Output):
    """
    Something created by a person.

    Labels: Kreation einer Person (de) / person's creation (en)
    """
    def __init__(self, hasIdentifier=None, hasName=None, hasTitle=None, hasCreationDate=None, hasPreferredName=None, hasAlias=None, hasCreating=None, hasModificationDate=None, hasDescription=None, **kwargs):
        """

        :param hasIdentifier:
        :param hasName:
        :param hasTitle:
        :param hasCreationDate:
        :param hasPreferredName:
        :param hasAlias:
        :param hasCreating:
        :param hasModificationDate:
        :param hasDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Creation"

        self.hasIdentifier = HasIdentifier(hasIdentifier)
        self.hasName = HasName(hasName)
        self.hasTitle = HasTitle(hasTitle)
        self.hasCreationDate = HasCreationDate(hasCreationDate)
        self.hasPreferredName = HasPreferredName(hasPreferredName)
        self.hasAlias = HasAlias(hasAlias)
        self.hasCreating = HasCreating(hasCreating)
        self.hasModificationDate = HasModificationDate(hasModificationDate)
        self.hasDescription = HasDescription(hasDescription)
