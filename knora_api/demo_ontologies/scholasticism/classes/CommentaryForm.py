#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.Information import Information
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:CommentaryForm

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class CommentaryForm(Information):
    """
    Form to represent a scholastic commentary.

    Labels: scholastische Kommentarform (de) / scholastic commentary form (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CommentaryForm"
