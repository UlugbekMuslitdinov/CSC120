class Word:

    def __init__(self, word):
        self._word = word

    def __str__(self):
        return self._word.lower()

    def __eq__(self, other):
        if len(self._word) == len(other._word):
            for i in self._word.lower():
                if i not in other._word.lower():
                    return False
            return True
        else:
            return False
