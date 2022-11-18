def nod(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        # a = b * q + r
        r = a % b
        return nod(b, r)


print(nod(2, 7))
print(nod(36, 6))