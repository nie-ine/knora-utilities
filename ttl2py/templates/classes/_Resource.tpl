#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

$module_import
from .. import ONTOLOGY_NS, PROJECT_ID

"""
$general_comment
"""


class $class_name($sub_class_of):
    """
$class_comment
    """
    def __init__(self,$argument **kwargs):
        """
$argument_comment
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "$class_name"
$class_internal_vars
$class_properties_types
$class_properties