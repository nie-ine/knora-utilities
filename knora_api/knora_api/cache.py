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

import os
import pathlib
import sqlite3


class Cache(object):
    """
    Provides a key-value data storage that will be used as a kind of 'cache'
    to 'optimize' reading and writing operations
    """

    def __init__(self, name=None):
        """

        """
        self._connection = None

        self.open(name)

    def open(self, name):
        """
        opens the database
        :param name: name of the database
        :return:
        """
        try:
            self.create_cache_dir()
            self._connection = sqlite3.connect('{}{}{}.sqlite'.format(self.cache_dir, os.sep, name), uri=True)
            cur = self._connection.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Cache';")
            if cur.fetchone() is None:
                self.initialize()
            return True
        except TypeError as e:
            print(e)
            self._connection = None
        return self._connection

    def close(self):
        """
        closes the database

        :return:
        """
        self._connection = None

    def initialize(self):
        """
        initializes/clears the database
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("DROP TABLE IF EXISTS Cache;")
            cur.execute("CREATE TABLE Cache(client_id text PRIMARY KEY , value text NOT NULL, checksum text NULL);")
            cur.close()
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
            self._connection.rollback()
        return False

    def get(self, client_id):
        """
        gets the key's value

        :param client_id:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("SELECT value, checksum FROM Cache WHERE client_id=:client_id;", {'client_id': client_id})
            record = cur.fetchone()
            return record[0] if record else None
        except Exception as e:
            print(e)
        return None

    def get_value(self, client_id):
        """
        gets the client_id's value

        :param client_id:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("SELECT value FROM Cache WHERE client_id=:client_id;", {'client_id': client_id})
            record = cur.fetchone()
            return record[0] if record else None
        except Exception as e:
            print(e)
        return None

    def set(self, client_id, value, checksum=None):
        """
        set a client_id, its value and checksum

        :param client_id:
        :param value:
        :param checksum: (optional)
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("INSERT INTO Cache VALUES (:client_id, :value, :checksum);", {'client_id': client_id,
                                                                                      'value': value,
                                                                                      'checksum': checksum})
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
        return False

    def setnx(self, client_id, value, checksum=None):
        """
        sets a client_id, its value and checksum, only if the client_id does not exists
        :param key:
        :param value:
        :param checksum: (optional)
        :return:
        """

        if self.get(client_id):
            return False
        return self.set(client_id, value, checksum)

    @property
    def cache_dir(self):
        """
        'calculates' the location of the data directory

        :return: path as a string
        """

        home_dir = os.path.dirname(os.path.realpath(__file__))
        return "{}{}cache".format(home_dir, os.sep)

    def create_cache_dir(self):
        """
        creates the cache directory, if it doesn't exist

        :return:
        """

        return pathlib.Path(self.cache_dir).mkdir(parents=True, exist_ok=True)
