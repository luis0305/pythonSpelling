from WordsCounter import WordsCounter

class Spelling:

    CHARACTERS_ALLOWED = 'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ'

    def __init__(self):
        self._wordsSet = []
        self._words = WordsCounter()

    # read file and get content file
    def read(self, pathFile):
        with open(pathFile, 'r') as file:
            for line in file:
                for word in line.split(' '):
                    self._wordsSet.append(self.__clean_word(word))
        file.close()
        self.__countWordsRepetions()

    # cleand a word by allouth characteres
    def __clean_word(self, word):
        lettersCleaned = [];
        for letter in word:
            if letter in self.CHARACTERS_ALLOWED:
                lettersCleaned.append(letter.lower())
        return ''.join(lettersCleaned)

    # count the words repetions
    def __countWordsRepetions(self):
        for word in self._wordsSet:
            self._words[word] +=1

    @property
    def words(self):
        return self._words


spelling = Spelling()
spelling.read('Content')
words = spelling.words

print(words.get('mí'))