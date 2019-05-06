def root(r):
    if len(r) == 1:
        return r
    dev = [0 for i in range(len(r[0]) + 1)]

    for i in range(len(r[0])):
        for j in range(2):
            dev[i + j] += r[0][i] * r[1][j]
    return root([dev] + r[2:])


v = input().split(",")
v = [[1, int(i)] for i in v]
print(v)
print(root(v))

