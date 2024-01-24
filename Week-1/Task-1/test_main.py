import unittest
from main import categorize_age

class TestCategorizeAge(unittest.TestCase):

    def test_child_category(self):
        result = categorize_age(5)
        self.assertEqual(result, "Child")

    def test_teenager_category(self):
        result = categorize_age(16)
        self.assertEqual(result, "Teenager")

    def test_adult_category(self):
        result = categorize_age(25)
        self.assertEqual(result, "Adult")

if __name__ == '__main__':
    unittest.main()
