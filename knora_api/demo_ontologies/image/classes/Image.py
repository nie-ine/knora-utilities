#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.Expression import Expression
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class image:Image

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class Image(Expression):
    """
    Visual representation of a resource.

    Labels: Bild (de) / image (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Image"
