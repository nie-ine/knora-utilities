#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CommentaryForm import CommentaryForm
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:CommentaryAbbreviation

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class CommentaryAbbreviation(CommentaryForm):
    """
    Scholastic commentary on a text in the form of a shortened version.

    Labels: Kurzfassung (de) / abbreviation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CommentaryAbbreviation"
