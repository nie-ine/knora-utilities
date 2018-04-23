#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Commentary import Commentary as tex_Commentary
from ..properties.hasCommentaryMethod import HasCommentaryMethod
from ..properties.hasCommentaryForm import HasCommentaryForm
from ..properties.hasReportator import HasReportator
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Commentary

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Commentary(tex_Commentary):
    """
    Commentary made by a person with a scholastic role.

    Labels: scholastischer Kommentar (de) / scholastic commentary (en) / commentarius scholasticus (la)
    """
    def __init__(self, hasCommentaryMethod=None, hasCommentaryForm=None, hasReportator=None, **kwargs):
        """

        :param hasCommentaryMethod:
        :param hasCommentaryForm:
        :param hasReportator:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Commentary"

        self.hasCommentaryMethod = HasCommentaryMethod(hasCommentaryMethod)
        self.hasCommentaryForm = HasCommentaryForm(hasCommentaryForm)
        self.hasReportator = HasReportator(hasReportator)
