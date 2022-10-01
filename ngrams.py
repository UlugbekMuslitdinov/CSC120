"""
    File: ngrams.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Find the most frequent n-grams in the text.
"""


class Input:
    """
    This class is used to get the file name from the user and
    read the file and clean the content of the file by storing each word in the list.

    Attributes:
        f (str): The file name.
        clean_content (list): The list of words in the file.

    Methods:
        wordlist(): Returns the list of words in the file.
    """

    def __init__(self):
        self.f = open(input(), 'r').read()
        self.clean_content = []

    def wordlist(self):
        raw_words = self.f.split()
        for word in raw_words:
            clean = word.strip(".-,!?:;#$&()'\"`").lower()
            if clean != "":
                self.clean_content.append(clean)
        return self.clean_content


class Ngrams:
    """
    This class is used to find the most frequent n-grams in the text.

    Attributes:
        n (int): The number of words in the n-gram.
        grams (dict): The dictionary of n-grams and their frequencies.

    Methods:
        update(ngram): Updates the dictionary of n-grams and their frequencies.
        process_wordlist(wordlist): Processes the list of words in the file.
        print_max_ngrams(): Prints the most frequent n-grams in the text.
    """

    def __init__(self):
        self.n = int(input())
        self.grams = {}

    def update(self, ngram):
        if ngram in self.grams:
            self.grams[ngram] += 1
        else:
            self.grams[ngram] = 1

    def process_wordlist(self, wordlist):
        if len(wordlist) > self.n:
            for i in range(len(wordlist) - self.n + 1):
                slice_to_unite = " ".join(wordlist[i:i+self.n])
                self.update(slice_to_unite)

    def print_max_ngrams(self):
        max_times = 0
        strs = []
        for gram in self.grams:
            if self.grams[gram] > max_times:
                max_times = self.grams[gram]
                strs = [gram]
            elif self.grams[gram] == max_times:
                strs.append(gram)
        return strs, max_times


def main():
    """
    This function is used to call the Input class and Ngrams class
    and print the most frequent n-grams in the text.
    """
    wordlst = Input()
    result = Ngrams()
    words = wordlst.wordlist()
    result.process_wordlist(words)
    grams, times = result.print_max_ngrams()
    for gram in sorted(grams):
        print("{:d} -- {}".format(times, gram))


main()
