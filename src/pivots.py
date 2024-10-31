def pivotIndexGetter(matrix):
    maxY = len(matrix)
    maxX = len(matrix[0])
    a = matrix[maxY - 1][:5]
    mini = min(a)
    pY = -1
    pX = -1
    if mini >= 0:
        return -1, -1
    else:
        pX = a.index(mini)
    mini = 99999999999999
    for i in range(0, maxY - 1):
        if matrix[i][maxX - 1]:
            if matrix[i][pX] > 0 and (mini > matrix[i][maxX - 1] / matrix[i][pX] > 0):
                pY = i
                mini = matrix[i][maxX - 1] / matrix[i][pX]
        elif mini > matrix[i][pX] > 0:
            pY = i
            mini = matrix[i][maxX - 1] / matrix[i][pX]
    return pY, pX

def doPivot(matrix, pY, pX):
    pValue = matrix[pY][pX]
    matrix[pY] = list(map(lambda x: x / pValue, matrix[pY]))
    maxY = len(matrix)
    maxX = len(matrix[0])
    for i in range(0, maxY):
        if i == pY:
            continue
        b = matrix[i][pX]
        for j in range(0, maxX):
            matrix[i][j] -= b * matrix[pY][j]

def doSimplex(matrix):
    res = [-1] * 4
    while True:
        pY, pX = pivotIndexGetter(matrix)
        if pY == -1 or pX == -1:
            break
        doPivot(matrix, pY, pX)
        res[pY] = pX
    return res