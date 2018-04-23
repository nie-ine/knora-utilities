#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sascha KAUFMANN"
__copyright__ = "Copyright 2018, NIE-INE"
__credits__ = []
__license__ = "3-Clause BSD License"
__version__ = "0.0.1"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Beta"


def open_session(*args, **kwargs):
    """
    opens a session to the host that provides Knora;
    """
    from .session import Session
    return Session(*args, **kwargs)


open = Session = open_session


__all__ = ['connections', 'cache']
