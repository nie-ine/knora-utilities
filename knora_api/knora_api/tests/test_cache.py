import unittest
from ..cache import Cache


class KnoraApiCacheTest(unittest.TestCase):
    """

    """
    def test_empty_initialization(self):
        """

        :return:
        """

        cache = Cache('test')

#
#
# if __name__ == '__main__':
#     unittest.main()
# a = Cache('blub')
# #a.clear()
# #a.set('a', 'b')
# b = a.get('a')
# c = a.get('b')
# d = a.setnx('a', 'b')
# e = a.get('a')
# g = a.cache_dir
# f = 0