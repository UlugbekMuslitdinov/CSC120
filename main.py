x = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

summ = 0

for i in x:
    summ = summ + i[0]

print(summ)



grid = [[18, 25, 36], [23, 25, 18], [20, 54, 7]]

ttl = 0
for i in range(len(grid)):
    row = grid[i]
    ttl = ttl + row[0]


print(ttl)


text = "Bear Down, Arizona, Bear Down, Red and Blue"
words = text.split(", ")