__author__ = 'Luis'

import unittest
from Spelling import Spelling


class SpellingTesting(unittest.TestCase):

    def __init__(self, spelling):
        self.spelling = spelling

    def test_word(self, word):
        words = self.spelling.words;
        self.assertEquals(words.get(word), word, 'La palabra no se encuentra')

spelling = Spelling()
spelling.content_source = 'Asimov.txt'
spelling.read_from_file()
print(spelling.get_probability_by_word('la'))
print(spelling.get_probability_by_word('vamos'))