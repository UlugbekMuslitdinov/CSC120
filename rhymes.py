"""
    File: rhymes.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Finds rhymes for a given word in the Dictionary of words and sounds.
"""


def doc_to_dict(file):
    """
    Reads the file and extracts the data into the dictionary of sets.

    Args:
        file (str): The name of the file with words and sounds.

    Returns:
        dict: A dictionary of sets that contains the data of the sounds to words.

    Pre-condition:
        The file exists.

    Post-condition:
        The data is extracted into the dictionary of sets.
    """
    return_dict = dict()
    contents = open(file, "r").read().splitlines()
    lines = []
    for i in contents:
        lines.append(i.split(","))
    words_and_sounds = []
    for line in lines:
        words_and_sounds.append(line[0].split())
    for lst in words_and_sounds:
        if lst[0] not in return_dict:
            return_dict[lst[0]] = []
        soundlist = []
        for i in range(1, len(lst)):
            soundlist.append(lst[i])
        return_dict[lst[0]].append(soundlist)
    return return_dict


def find_rhyme(word, words_set):
    """
    Finds rhymes for a given word in the Dictionary of words and sounds.

    Args:
        word (str): The word to find rhymes for.
        words_set (dict): The dictionary of sets that contains the data of the sounds to words.

    Returns:
        set: A set of rhymes for the given word.

    Pre-condition:
        The word exists in the dictionary.

    Post-condition:
        The rhymes are found for the given word.
    """
    pronunciations = words_set[word]
    rhyme_words = []
    for pron in pronunciations:
        match_range = []
        for i in range(len(pron)):
            if "1" in pron[i]:
                match_range = pron[i - 1:]
        for word in words_set:
            for sound in words_set[word]:
                if match_range[1:] == sound[len(sound) - len(match_range) + 1:]:   # Checks if the sounds after the primary stress match.
                    if match_range[0] != sound[len(sound) - len(match_range)]:  # Checks if the sounds before the primary stress don't match.
                        rhyme_words.append(word)
    return rhyme_words


def main():
    """
    The main function of the program.
    Prompts the user for a word and prints the rhymes for the given word.
    """
    file = str(input())
    wordset = doc_to_dict(file)
    word_to_find_rhyme = str(input()).upper()
    rhymes = find_rhyme(word_to_find_rhyme, wordset)
    for rhyme in sorted(rhymes):
        print(rhyme)


main()
