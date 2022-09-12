def words_ending_with(wordlist, tail):
    returns = []
    for word in wordlist:
        if word[len(word)-len(tail):] == tail:
            returns.append(word)
    return returns


def words_beginning_with(wordlist, head):
    returns = []
    for word in wordlist:
        if word[:len(head)] == head:
            returns.append(word)
    return returns


def primary_stress_position(phoneme_list):
    for i in range(len(phoneme_list)):
        if '1' in phoneme_list[i]:
            return i
