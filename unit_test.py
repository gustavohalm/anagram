from test import check_anagram
import unittest
class TestCheckAnagram(unittest.TestCase):
    def test_check_sucess(self):
        checked = check_anagram('anagram', 'nagaram')

        self.assertEqual(checked, True)

    def teste_check_false(self):
        checked = check_anagram('aaab', 'aabb')

        self.assertEqual(checked, False)