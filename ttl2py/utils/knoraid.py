#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

  Taken the file
  https://github.com/dhlab-basel/Knora/blob/develop/webapi/src/main/scala/org/knora/webapi/util/KnoraIdUtil.scala
  as an inspiration to create KnoraIRIs in python

"""
import base64
from uuid import uuid4

import getopt
import os
import pathlib
import sys
from os.path import commonprefix, isfile, exists
from string import Template
from urllib.parse import urlsplit
from datetime import datetime
from rdflib import Graph, BNode, RDF, URIRef, OWL, RDFS
from rdflib.namespace import Namespace, NamespaceManager


__author__ = "Sascha KAUFMANN"
__copyright__ = "Copyright 2018, NIE-INE"
__credits__ = []
__license__ = "3-Clause BSD License"
__version__ = "0.0.1"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Development"


class KnoraId_(object):
    """

    """

    _CANONICAL_UUID_LENGTH = 36
    _BASE64_UUID_LENGTH = 22

    def __init__(self):
        """

        """
        self.iri_domain = "rdfh.ch"    # domain name to construct a Knora IRI


"""
  Converts SALSAH data IDs to Knora IRIs, generates random Knora IRIs for
  new data, and provides functions for manipulating Knora IRIs.
"""

class KnoraId(object):
    """
      Converts SALSAH data IDs to Knora IRIs, generates random Knora IRIs for
      new data, and provides functions for manipulating Knora IRIs.
    """

    def makeRandomBase64EncodedUuid(self):
        """

        :return:
        """
        f
        _b64Encoder = base64.encodebytes
        _b64Decoder = base64.decode
        return _b64Encoder(uuid4().bytes)__str__()

a = KnoraId()
b = a.makeRandomBase64EncodedUuid()
c = 0

