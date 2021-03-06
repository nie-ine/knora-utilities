#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sascha KAUFMANN"
__copyright__ = "Copyright 2018, NIE-INE"
__credits__ = []
__license__ = "3-Clause BSD License"
__version__ = "0.0.2"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Beta"

import sys
import traceback

import requests

from datetime import datetime
from json import dumps
from urllib.parse import quote_plus
from requests.adapters import HTTPAdapter

from .constants import SESSION
from .constants import KNORA_V1

DEBUG = False


class Session(object):
    """
    Representation of a socket with a knora server.

    The proper way to get an instance of this class is to call
    connect().

    Establishes a 'connection' to the Knora-API.

    :param host: Host where the Knora server is located
    :param user: Username to log in as
    :param password: Password to use.
    :param port: Knora port to use, default is usually OK. (default: 3333)
    :param charset: Charset you want to use.
    :param connect_timeout: Timeout before throwing an exception when connecting.
        (default: 10, min: 1, max: 31536000)
    """

    def __init__(self, host=None, port=None, user=None, password=None,
                 charset='utf-8', connect_timeout=3.25, response_timeout=27,
                 max_retries=3, cache=None):
        """

        :param host:
        :param port:
        :param user:
        :param password:
        :param charset:
        :param connect_timeout:
        :param response_timeout:
        :param max_retries:
        :param cache:
        """

        self.host = host or SESSION.DEFAULT_HOST   # Standard Knora Host
        self.port = port
        self.user = 'root@example.com' #user or SESSION.DEFAULT_USER
        self.password = 'test' #password or SESSION.DEFAULT_PASSWORD
        self.charset = charset or SESSION.DEFAULT_CHARSET
        self.connect_timeout = connect_timeout or SESSION.DEFAULT_TIMEOUT_CONNECT
        self.response_timeout = None    #response_timeout or SESSION.DEFAULT_TIMEOUT_RESPONSE
        self.max_retries = max_retries or SESSION.DEFAULT_RETRIES
        self._cache = None
        self._session = None

        if self.host == SESSION.DEFAULT_HOST and not self.port:
            self.port = SESSION.DEFAULT_PORT

        if self.port:
            self.knora_server = "http://{}:{}".format(self.host, self.port)
        else:
            self.knora_server = "http://{}".format(self.host)

        if cache:
            try:
                from .cache import Cache
                self._cache = Cache(cache)
            except Exception as e:
                print(e)
                self._cache = None

        self.open()

    def open(self):
        self.close()
        try:
            self._session = requests.Session()
            if self.user is not None and self.password is not None:
                self._session.auth = (self.user, self.password)
            self._session.mount(self.host, HTTPAdapter(max_retries=self.max_retries))
            self._session.timeout = (self.connect_timeout, self.response_timeout)
        except Exception as e:
            print(e)
            self.close()

    def close(self):
        self._session = None

    # core functions
    def _get(self, url, params=None, **kwargs):
        """

        :param url:
        :param params:
        :param kwargs:
        :return:
        """

        r = None
        try:
            r = self._session.get(url=url, params=params, **kwargs)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            print(e)
            if DEBUG:
                print(r.content.decode('utf-8'))
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def _post(self, url, data=None, json=None, **kwargs):
        """

        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """

        r = None
        try:
            r = self._session.post(url=url, data=data, json=json, **kwargs)
            if r.status_code != 200:
                print(r)
                print("Post failed: {}".format(r.content.decode('utf-8')))
            r.raise_for_status()
            return r.json()
        except Exception as e:
            print(e)
            if DEBUG:
                print(r.content.decode('utf-8'))
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    # knora version depending functions

    def get_v1_projects(self):
        """
        get all projects the current user is allowed to access

        :return: information about all accessible projects, stored in knora
        """

        url = "{}{}".format(self.knora_server, KNORA_V1.V1_PROJECTS)
        response = self._get(url=url)
        return response.json() if response else None

    def get_v1_properties(self, resource_id):
        """
        get the resource's properties' data out of Knora that are accessible
        by the given resource_id

        :param resource_id: resource_identifier
        :return: properties' data, if resource exists and the user is allowed
                                   to access it
                 None, else
        """

        try:
            url = "{}{}/{}".format(self.knora_server,
                                   KNORA_V1.V1_PROPERTIES,
                                   quote_plus(resource_id))
            response = self._get(url=url)
            return response.json() if response else None
        except (TypeError, Exception) as e:
            print(e)
            if DEBUG:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def get_v1_resource(self, resource_id):
        """
        get the resource data out of Knora that are accessible
        by the given resource_id

        :param resource_id: resource_identifier
        :return: resource's data, if resource exists and the user is allowed
                                  to access it
                 None, else
        """

        try:
            url = "{}{}/{}".format(self.knora_server,
                                   KNORA_V1.V1_RESOURCES,
                                   quote_plus(resource_id))
            response = self._get(url=url)
            return response
        except (TypeError, Exception) as e:
            print(e)
            if DEBUG:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def get_v1_resourcetypes(self, resource_class_iri):
        """
        get information about a resource class given its IRI

        :param resource_class_iri: resource_class_identifier
        :return: resource class information, if iri exists
                 None, else
        """

        try:
            url = "{}{}/{}".format(self.knora_server,
                                   KNORA_V1.V1_RESOURCETYPES,
                                   quote_plus(resource_class_iri))
            response = self._get(url=url)
            return response
        except (TypeError, Exception) as e:
            print(e)
            if DEBUG:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def get_v1_vocabularies(self):
        """
        get a list of all available vocabularies

        :return: information about all accessible vocabularies, stored in knora
        """

        url = "{}{}".format(self.knora_server, KNORA_V1.V1_VOCABULARIES)
        response = self._get(url=url)
        return response

    def post_v1_resource(self, json, file_name=None, client_id=None):
        """
        store information in Knora

        :param json: data that should be stored in json
                 (list & dict) structure
        :param file_name: name of the image that might be part of the data
        :param client_id: use the client_id to avoid unnecessary operations
        :return: resource_id, if the information was successfully stored
                 None,        otherwise
        """

        try:
            if self._cache and client_id:
                value = self._cache.get(client_id=client_id)
                if value:
                    return value

            url = "{}{}".format(self.knora_server, KNORA_V1.V1_RESOURCES)

            if file_name:
                data = {'json': dumps(json).encode('utf-8')}
                file_type = file_name.split('.')[-1]
                mime_type = self.get_mime_type(file_type)
                files = {'file': (file_name, open(file_name, 'rb'), mime_type)}
                response = self._post(url=url, data=data, files=files)
            else:
                response = self._post(url=url, json=json)

            resource_id = response.get('res_id') if response and response['status'] == 0 else None
            if self._cache and resource_id:
                self._cache.set(key=client_id, value=resource_id)
            return resource_id
        except Exception as e:
            print(e)
            if DEBUG:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def get_v1_resource_xmlimportschemas(self, ontology_iri, **kwargs):
        """

        :param ontology_iri: the ontology IRI, for which we want the schema for
        :param kwargs:
        :return: name of the generated file that holds the schema
        """

        try:
            timestamp_utc = datetime.utcnow().strftime("%Y%m%d%H%M%S")
            filename = 'xmlimportschemas_{}.zip'.format(timestamp_utc)
            url = "{}{}/xmlimportschemas/{}".format(self.knora_server,
                                                    KNORA_V1.V1_RESOURCES,
                                                    ontology_iri)
            r = requests.get(url=url, )
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)

            return filename
        except Exception as e:
            print(e)
            if DEBUG:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

    def post_v1_resources_xmlimport(self, project_iri, data=None, file_name=None, **kwargs):
        """
        imports the given data/file as a bulk-import

        :param project_iri:
        :param data:
        :param file_name:
        :param kwargs:
        :return:
        """

        headers = {'content-type': "application/xml; charset=UTF-8",
                   'cache-control': "no-cache"}

        url = "{}{}/xmlimport/{}".format(self.knora_server,
                                         KNORA_V1.V1_RESOURCES,
                                         project_iri)

        if file_name:
            file_type = file_name.split('.')[-1]
            mime_type = self.get_mime_type(file_type)
            files = {'file': (file_name, open(file_name, 'rb'), mime_type)}
            response = self._post(url=url, files=files, headers=headers)
        else:
            response = self._post(url=url, data=data)

        # write result into the 'cache' if possible
        if self._cache and response:
            try:
                resources = response['createdResources']
                for resource in resources:
                    try:
                        self._cache.set(client_id=resource['clientResourceID'],
                                        value=resource['resourceIri'])
                    except KeyError as ke:
                        print(ke)
            except KeyError as ke:
                print(ke)

        return response

    # wrappers for existing functions to make the live plus facile

    def get_projects(self):
        """
        just a wrapper of 'get_v1_projects'

        :return:
        """

        return self. get_v1_projects()

    def get_resource(self, resource_id):
        """
        just a wrapper for 'get_v1_resource'

        :param resource_id:
        :return:
        """

        return self.get_v1_resource(resource_id=resource_id)

    def get_resourcetypes(self, resource_class_iri):
        """
        just a wrapper for 'get_v1_resourcetypes'

        :param resource_class_iri:
        :return:
        """

        return self.get_v1_resourcetypes(resource_class_iri=resource_class_iri)

    def get_properties(self, resource_id):
        """
        just a wrapper for 'get_v1_properties'

        :param resource_id:
        :return:
        """

        return self.get_v1_properties(resource_id=resource_id)

    def get_vocabularies(self):
        """

        just a wrapper of 'get_v1_vocabularies'
        :return:
        """

        return self. get_v1_vocabularies()

    def post_resource(self, json, file_name=None, **kwargs):
        """
        just a wrapper for the 'post_v1_resource'

        :param json:
        :param file_name:
        :return:
        """

        return self.post_v1_resource(json, file_name, **kwargs)

    def post_xmlimport(self, project_iri, data=None, file_name=None, **kwargs):
        """
        just a wrapper for 'post_v1_resources_xmlimport()'

        :param project_iri:
        :param data:
        :param file_name:
        :param kwargs:
        :return:
        """

        try:
            encoded_project_iri = quote_plus(project_iri)
        except TypeError:
            "Error - Please enter a valid project IRI!"
            return None

        return self.post_v1_resources_xmlimport(encoded_project_iri, data, file_name, **kwargs)

    def get_xmlimportschemas(self, ontology_iri, **kwargs):
        """

        :param ontology_iri: the IRI of the choosen ontology (e.g. 'http://www.knora.org/ontology/0802/biblio)
        :return: a zip archive containing information about the onology and other ontologies it depends on.
        """

        try:
            encoded_ontology_iri = quote_plus(ontology_iri)
        except TypeError:
            "Error - Please enter a valid URL!"
            return None

        return self.get_v1_resource_xmlimportschemas(ontology_iri=encoded_ontology_iri, **kwargs)

    # some utility functions ...

    @staticmethod
    def get_mime_type(file_extension):
        """
        tries to determine the correct mime-type from
        a given extension
        (supports knora accepted image types by now)

        :param file_extension: the file's extension
        :return: (str) mime-type, if extension is known
                None, else
        """

        try:
            extension = file_extension.lower()
            if extension in ['jfif', 'jfif-tbnl', 'jpe', 'jpeg', 'jpg']:
                return 'image/jpeg'     # 'image/pjpeg'
            elif extension == 'png':
                return 'image/png'
            elif extension in ['tif', 'tiff']:
                return 'image/tiff'     # 'image/x-tiff'
            elif extension == 'xml':
                return 'application/xml'
        except AttributeError:
            pass

        return None

    def get_cached_record(self, client_id):
        """
        gets the record for a given client id (key) from the cache, if available

        :param client_id: the records's identifier
        :return: a triple with (client_id, IRI, checksum) if the record exists,
                 None, otherwise.
        """

        return self._cache.get(client_id=client_id)

    def set_cached_record(self, client_id, iri, checksum=None):
        """
        write a record (client_id, iri, checksum) into the cache
        
        :param client_id: the record's identifier/label/key
        :param iri: the IRI that represents the resource inside the triplestore
        :param checksum: the resource's checksum
        :return: True, in case of success; false otherwise
        """""

        return self._cache.set(client_id=client_id, value=iri, checksum=checksum)

    def get_cached_iri(self, client_id):
        """
        gets the resource's IRI from the cache that is represent by the given identifier/label
        :param client_id: the resource's identifier (record key)
        :return: the stored IRI in case of success, None otherwise
        """

        return self._cache.get_iri(client_id=client_id)
