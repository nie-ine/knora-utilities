import unittest
import knora_api
import knora_api.constants.SESSION as SESSION


class KnoraApiTest(unittest.TestCase):
    def test_empty_initialization(self):
        """

        :return:
        """

        connection = knora_api.open()
        self.assertEqual(connection.host, SESSION.DEFAULT_HOST)
        self.assertEqual(connection.port, SESSION.DEFAULT_PORT)
        self.assertEqual(connection.user, SESSION.DEFAULT_USER)
        self.assertEqual(connection.password, SESSION.DEFAULT_PASSWORD)
        self.assertEqual(connection.charset, SESSION.DEFAULT_CHARSET)
        self.assertEqual(connection.connect_timeout, SESSION.DEFAULT_TIMEOUT_CONNECT)
        self.assertEqual(connection.response_timeout, SESSION.DEFAULT_TIMEOUT_RESPONSE)
        self.assertEqual(connection.max_retries, SESSION.DEFAULT_RETRIES)

    def test_user_initialization(self):
        """

        :return:
        """

        my_host = '192.168.1.1'
        my_port = 4444
        my_user = 'my_user'
        my_password = 'my_password',
        my_charset = 'unicode'
        my_connect_timeout = 42
        my_response_timeout = 43
        my_max_retries = 44
        connection = knora_api.open(host=my_host,
                                       port=my_port,
                                       user=my_user,
                                       password=my_password,
                                       charset=my_charset,
                                       connect_timeout=my_connect_timeout,
                                       response_timeout=my_response_timeout,
                                       max_retries=my_max_retries)
        self.assertEqual(connection.host, my_host)
        self.assertEqual(connection.port, my_port)
        self.assertEqual(connection.user, my_user)
        self.assertEqual(connection.password, my_password)
        self.assertEqual(connection.charset, my_charset)
        self.assertEqual(connection.connect_timeout, my_connect_timeout)
        self.assertEqual(connection.response_timeout, my_response_timeout)
        self.assertEqual(connection.max_retries, my_max_retries)

        #self.assertIsNotNone(connection.host)

#        self.assertIsNotNone(knora_api.port)

    def test_mime_type_detection(self):
        """

        :return:
        """
        connection = knora_api.open()

        input_data = {'image/jpeg': ['jfif', 'jfif-tbnl', 'jpe', 'jpeg', 'jpg'],
                      'image/png': ['png', 'PNG'],
                      'image/tiff': ['tif', 'tiff'],
                      None: ['txt', 42, None, ['test']]}
        for mime_type, value_list in input_data.items():
            for value in value_list:
                self.assertEqual(connection.get_mime_type(value), mime_type)

# def main():
#     """
#     """
#
#     conn = knora_api.connect(host='localhost', port=3306, user='root', passwd='')
#
#
# if __name__ == '__main__':
#     unittest.main()