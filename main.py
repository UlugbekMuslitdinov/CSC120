"""
POTATO
"""

class Word:

    def __init__(self, word):
        self._word = word.strip(".!:;?-").lower()

    def __str__(self):
        return "Word(" + self._word + ")"

    def clean_word(self, word):
        return word.strip(".!:;?-").lower()

# 2) No, reference does not contain a list. It only refers to the object's unique id
# 3) 1 - Create a list of numbers
#    2 - Assign the list's id to x variable
