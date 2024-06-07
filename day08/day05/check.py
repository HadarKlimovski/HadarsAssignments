import unittest
from df_dict import count_characters, count_lines, count_words

class TestTextCounter(unittest.TestCase):
    def test_count_characters(self):
        self.assertEqual(count_characters("hello world"), 11)

    def test_count_lines(self):
        self.assertEqual(count_lines("hello\nworld"), 2)
        self.assertEqual(count_lines("hello\nworld\n"), 3)

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("  hello   world  "), 2)
        self.assertEqual(count_words(""), 0)

if __name__ == '__main__':
    unittest.main()
