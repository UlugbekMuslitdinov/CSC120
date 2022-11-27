"""
    File: writer_bot.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: This program generates a text by analyzing a text file
"""

import random

SEED = 8   # SEED for random number generator
random.seed(SEED)

file = input() # file name
n = int(input()) # prefix size
number_of_words = int(input()) # number of words to generate

# Read the file and store the words in a list
all_words = []
stripped_words = []
file_content = open(file, "r").read().splitlines()
for line in file_content:
    for word in line.split():
        all_words.append(word)
        stripped_words.append(word)


# Create a dictionary of prefixes and suffixes
data = {}
for i in range(len(all_words) - n + 1):
    prefix = tuple(stripped_words[i:i+n])
    if i+n < len(all_words):
        suffix = all_words[i+n]
    else:
        suffix = ""
    if prefix in data:
        data[prefix].append(suffix)
    else:
        data[prefix] = [suffix]


# Generate the text
prefix = tuple(stripped_words[0:n])
new_text = stripped_words[0:n]
while len(new_text) < number_of_words:
    if len(data[prefix]) == 1:
        new_text.append(data[prefix][0])
    else:
        new_text.append(data[prefix][random.randint(0, len(data[prefix])-1)])
    prefix = prefix[1:] + (new_text[-1],)

# Print 10 words per line
for i in range(len(new_text)):
    if i % 10 == 0:
        print()
    print(new_text[i], end=" ")

