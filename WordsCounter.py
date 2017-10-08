#extends dictionary
class WordsCounter(dict):
    #override method missing
    def __missing__(self, key):
        return 0