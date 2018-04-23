#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


"""
RichtextValue: definition of a datatype to handle Knora Base Ontology (KBO) text
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
RichtextValue: definition of a datatype to handle Knora Base Ontology (KBO) text
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class TextValue(HasValue):  # Subclass string to get handy functions
    """

    """

    def __init__(self, text):
        """

        :param text:
        """
        super(TextValue, self).__init__(text)
        self._name = "TextValue"
        self._property_type = 'richtext_value'
        self._value_type = 'utf8str'

#    def __repr__(self):
#        return """[{{'{:s}': {{'utf8str': "{:s}"}}}]""".format(self._json_type, super().__repr__())

#    def __str__(self):
#        return """[{{'{:s}': {{'utf8str': "{:s}"}}}]""".format(self._json_type, super().__str__())

#    def json(self):
#        return [{self._json_type: {'utf8str': self._value}}]

    def __json_struct__(self):
        """

        :return:
        """
        if self._value:
            return [{self._property_type: {self._value_type: self._value}}]