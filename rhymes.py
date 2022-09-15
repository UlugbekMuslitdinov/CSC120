def doc_to_dict(file):
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
    pronunciations = words_set[word]
    rhyme_words = []
    for pron in pronunciations:
        match_range = []
        for i in range(len(pron)):
            if '1' in pron[i]:
                match_range = pron[i-1:]
        for word in words_set:
            for sound in words_set[word]:
                if match_range[1:] == sound[len(sound)-len(match_range)+1:]:
                    if match_range[1:] == sound[len(sound) - len(match_range)+1:]:
                        if match_range[0] != sound[len(sound) - len(match_range)]:
                            rhyme_words.append(word)
    return rhyme_words


def main():
    file = str(input())
    wordset = doc_to_dict(file)
    word_to_find_rhyme = str(input()).upper()
    rhymes = find_rhyme(word_to_find_rhyme, wordset)
    for rhyme in sorted(rhymes):
        print(rhyme)


main()
