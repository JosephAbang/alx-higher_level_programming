import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_attributes(self):
        r = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)

    def test_rectangle_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_rectangle_str_representation(self):
        r = Rectangle(5, 10, 2, 3, 7)
        expected_str = "[Rectangle] (7) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_rectangle_update(self):
        r = Rectangle(5, 10)
        r.update(7, 20, 15, 3, 4)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_dictionary_representation(self):
        r = Rectangle(5, 10, 2, 3, 7)
        expected_dict = {'id': 7, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
