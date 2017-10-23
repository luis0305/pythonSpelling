# extends from dict
class DictMissing(dict):
    # override method missing for new behavior #
    def __missing__(self, key):
        return 0.0
