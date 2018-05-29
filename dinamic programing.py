from random import randint
import pandas as pd


def dynamic_prog(array):
    Xsize = len(array[0])
    Ysize = len(array)
    path = []
    for i in range(Ysize):
        part = [0] * Xsize
        path.append(part)
    text = []
    for i in range(Ysize):
        part = ['-'] * Xsize
        text.append(part)
    path[0][Xsize-1] = array[0][Xsize-1]
    for index in range(Xsize-1):
        realIndex = index + 1
        revIndex = Xsize - 1 - realIndex
        path[0][revIndex] = path[0][revIndex+1] + array[0][revIndex]
    for index in range(Ysize - 1):
        realIndex = index + 1
        path[realIndex][Xsize-1] = path[realIndex-1][Xsize-1] + array[realIndex][Xsize-1]
    for i in range(Ysize-1):
        for j in range(Xsize-1):
            iReal = i + 1
            jReal = j + 1
            jReversed = Xsize - 1 - jReal
            path[iReal][jReversed] = max(path[iReal - 1][jReversed],
                                         path[iReal - 1][jReversed + 1],
                                         path[iReal][jReversed + 1]) + array[iReal][jReversed]
    notEnd = True
    x = 0
    y = Ysize - 1
    while notEnd:
        if x == Xsize - 1 and y == 0:
            notEnd == False
            break
        if x == Xsize - 1:
            y -= 1
            text[y][x] = '+'
            continue
        if y == 0:
            x += 1
            text[y][x] = '+'
            continue
        a = path[y - 1][x + 1]
        b = path[y - 1][x]
        c = path[y][x + 1]
        if a >= b and a >= c:
            text[y - 1][x + 1] = '+'
            x += 1
            y -= 1
        elif b >= c:
            text[y - 1][x] = '+'
            y -= 1
        else:
            text[y][x + 1] = '+'
            x += 1
    text[Ysize-1][0] = '+'
    text[0][Xsize-1] = '+'
    for i in range(Ysize):
        string = ''
        for j in range(Xsize):
            string += '  '
            string += text[i][j]
            string += '  '
        print(string)
    return path

myArray = [[randint(-100, 100) for j in range(5)] for i in range(5)]
print(pd.DataFrame(myArray), '\n')
print('\n', pd.DataFrame(dynamic_prog(myArray)))

