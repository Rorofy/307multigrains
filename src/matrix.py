def matrixCreate(nTab, pTab):
    matrix = [
        [1, 0, 1, 0, 2],
        [1, 2, 0, 1, 0],
        [2, 1, 0, 1, 0],
        [0, 0, 3, 1, 2],
        list(map(lambda x:x * -1, pTab)) + ([0] * 5)
    ]
    for i in range(0, 4):
        for j in range(0, 4):
            matrix[i].append(1 if j == i else 0)
        matrix[i].append(nTab[i])
    return matrix