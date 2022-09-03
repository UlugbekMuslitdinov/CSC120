diagonals = []

file = open("grid.txt", "r")
lines = file.read().splitlines()
letter_sets = [i.split() for i in lines]
i = len(letter_sets)
max_horizontal = len(letter_sets) - 1
max_vertical = len(letter_sets) - 1
horizontal_start = 0
while i >= 0:
    horizontal_now = horizontal_start
    vertical_now = 0
    str_now = ""
    while horizontal_now <= max_horizontal and vertical_now <= max_vertical:
        str_now += letter_sets[horizontal_now][vertical_now]
        vertical_now += 1
        horizontal_now += 1
    horizontal_start += 1
    diagonals.append(str_now)
    i -= 1
i = len(letter_sets) - 1
vertical_start = 1
while i >= 0:
    horizontal_now = 0
    vertical_now = vertical_start
    str_now = ""
    while horizontal_now <= max_horizontal and vertical_now <= max_vertical:
        str_now += letter_sets[horizontal_now][vertical_now]
        vertical_now += 1
        horizontal_now += 1
    vertical_start += 1
    diagonals.append(str_now)
    i -= 1
for i in range(len(diagonals) - 1):
    if diagonals[i] == "":
        diagonals.pop(i)
