from DictMissing import DictMissing


class Spelling:

    CHARACTERS_ALLOWED = 'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ'

    def __init__(self, content_source = None):
        self._words = DictMissing()
        self._total_words = 0
        self._content_source = content_source

    # read file and get content file
    def read_from_file(self):
        with open(self._content_source, 'r') as file:
            for line in file:
                for word in line.split(' '):
                    self.__append_word(word)
        file.close()

    # cleand a word by allowed characteres
    def __clean_word(self, word):
        lettersCleaned = [];
        for letter in word:
            if letter in self.CHARACTERS_ALLOWED:
                lettersCleaned.append(letter.lower())
        return ''.join(lettersCleaned)

    # append word into dictionary
    def __append_word(self, word):
        cleaned_word = self.__clean_word(word)
        if cleaned_word != '':
            self._words[cleaned_word] += 1.0
            self._total_words += 1.0

    # count the words by repetitions
    def _get_words_frecuency(self, word):
        return self._words[word]

    def get_probability_by_word(self, word):
        if self._words[word] != 0.0:
            return self._get_words_frecuency(word) / self._total_words
        else:
            return 0.0

    def get_probability(self):
        p = 0.0
        for value in self._words.values():
            p += value / self._total_words
        return p

    @property
    def words(self):
        return self._words

    @property
    def content_source(self):
        return self._content_source

    @content_source.setter
    def content_source(self, value):
        self._content_source = value