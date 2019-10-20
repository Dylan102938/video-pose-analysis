import math


def vectorDifference(Vx, Vy, Vx1, Vy1):
    try:
        differences = [-1, -1]
        UVX = Vx / math.sqrt(Vx * Vx + Vy * Vy)
        UVY = Vy / math.sqrt(Vx * Vx + Vy * Vy)
        UVX1 = Vx1 / math.sqrt(Vx1 * Vx1 + Vy1 * Vy1)
        UVY1 = Vy1 / math.sqrt(Vx1 * Vx1 + Vy1 * Vy1)
        differencex = abs(UVX - UVX1) 
        differencey = abs(UVY - UVY1)
        differences[0] = differencex
        differences[1] = differencey
        return differences
    except:
        return [0, 0]


def averageError(frame, person1, person2):
    order = [2,0,3,1,4,2,5,3,16,2,17,3,22,2,23,3,10,2,11,3,6,4,7,5,8,6,9,7,12,10,
             13,11,14,12,15,13,18,16,19,17,20,18,21,19,24,22,25,23,26,24,27,25]
    v1 = []
    v2 = []
    count = 0
    for i in range(0, len(order), 2):
        if (person1[frame][order[i]] != -1) and (person2[frame][order[i]] != -1):
            v1.append(person1[frame][order[i]] - person1[frame][order[i + 1]])
            v2.append(person2[frame][order[i]] - person2[frame][order[i + 1]])

    sum = 0.0
    numwrong = 0

    for i in range(0, int(len(v1)/2)):
        if vectorDifference(v1[count], v1[count+1], v2[count], v2[count+1])[0] > 0.2 or vectorDifference(v1[count], v1[count+1], v2[count], v2[count+1])[1] > 0.2:
            numwrong += 1


        count += 2
    error = numwrong/(int(len(v1)/2))
    return error
