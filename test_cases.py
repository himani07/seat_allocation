import unittest
from seating import allocate_seat


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_allocate_seat(self):
        data = 4
        res = allocate_seat(data)
        self.assertEqual(res, '1c,1d,1e,1f')
        data = 3
        res = allocate_seat(data)
        self.assertEqual(res, '2c,2d,2e')
        data = 3
        res = allocate_seat(data)
        self.assertEqual(res, '3c,3d,3e')
        data = 2
        res = allocate_seat(data)
        self.assertEqual(res, '1a,1b')
        data = 3
        res = allocate_seat(data)
        self.assertEqual(res, '3c,3d,3e')


if __name__ == '__main__':
    unittest.main()