import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def test_square_attributes(self):
        s = Square(5, 2, 1, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_str_representation(self):
        s = Square(5, 2, 3, 7)
        expected_str = "[Square] (7) 2/3 - 5"
        self.assertEqual(str(s), expected_str)

    def test_square_update(self):
        s = Square(5)
        s.update(7, 10, 3, 4)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_dictionary_representation(self):
        s = Square(5, 2, 3, 7)
        expected_dict = {'id': 7, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
