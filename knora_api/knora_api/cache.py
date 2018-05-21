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
            cur.execute("CREATE TABLE Cache(key text PRIMARY KEY , value text NOT NULL, checksum text NULL);")
            cur.close()
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
            self._connection.rollback()
        return False

    def get(self, key):
        """
        gets the key's value

        :param key:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("SELECT value, checksum FROM Cache WHERE key=:key;", {'key': key})
            record = cur.fetchone()
            return record[0] if record else (None, None)
        except Exception as e:
            print(e)
        return None

    def get_value(self, key):
        """
        gets the key's value

        :param key:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("SELECT value FROM Cache WHERE key=:key;", {'key': key})
            record = cur.fetchone()
            return record[0] if record else None
        except Exception as e:
            print(e)
        return None

    def set(self, key, value, checksum=None):
        """
        set a key and its value

        :param key:
        :param value:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute("INSERT INTO Cache VALUES (:key, :value, :checksum);", {'key': key, 'value': value, 'checksum': checksum})
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
        return False

    def setnx(self, key, value, checksum=None):
        """
        sets a key and its value, only if the key does not exists
        :param key:
        :param value:
        :return:
        """

        if self.get(key):
            return False
        return self.set(key, value, checksum)

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
