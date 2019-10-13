import math


def vectorDifference(Vx, Vy, Vx1, Vy1):
    try:
        UVX = Vx / math.sqrt(Vx * Vx + Vy * Vy)
        UVY = Vy / math.sqrt(Vx * Vx + Vy * Vy)
        UVX1 = Vx1 / math.sqrt(Vx1 * Vx1 + Vy1 * Vy1)
        UVY1 = Vy1 / math.sqrt(Vx1 * Vx1 + Vy1 * Vy1)
        differencex = abs((UVX - UVX1) / UVX)
        differencey = abs((UVY - UVY1) / UVY)
        return (differencex + differencey) / 4
    except:
        return 0


def averageError(frame, person1, person2):
    v1 = []
    v2 = []

    v1x1 = person1[frame][2] - person1[frame][0]
    v1.append(v1x1)
    v1y1 = person1[frame][3] - person1[frame][1]
    v1.append(v1y1)
    v1x2 = person1[frame][4] - person1[frame][2]
    v1.append(v1x2)
    v1y2 = person1[frame][5] - person1[frame][3]
    v1.append(v1y2)
    v1x3 = person1[frame][16] - person1[frame][2]
    v1.append(v1x3)
    v1y3 = person1[frame][17] - person1[frame][3]
    v1.append(v1y3)
    v1x4 = person1[frame][22] - person1[frame][2]
    v1.append(v1x4)
    v1y4 = person1[frame][23] - person1[frame][3]
    v1.append(v1y4)
    v1x5 = person1[frame][10] - person1[frame][2]
    v1.append(v1x5)
    v1y5 = person1[frame][11] - person1[frame][3]
    v1.append(v1y5)
    v1x6 = person1[frame][6] - person1[frame][4]
    v1.append(v1x6)
    v1y6 = person1[frame][7] - person1[frame][5]
    v1.append(v1y6)
    v1x7 = person1[frame][8] - person1[frame][6]
    v1.append(v1x7)
    v1y7 = person1[frame][9] - person1[frame][7]
    v1.append(v1y7)
    v1x8 = person1[frame][12] - person1[frame][10]
    v1.append(v1x8)
    v1y8 = person1[frame][13] - person1[frame][11]
    v1.append(v1y8)
    v1x9 = person1[frame][14] - person1[frame][12]
    v1.append(v1x9)
    v1y9 = person1[frame][15] - person1[frame][13]
    v1.append(v1y9)
    v1x10 = person1[frame][18] - person1[frame][16]
    v1.append(v1x10)
    v1y10 = person1[frame][19] - person1[frame][17]
    v1.append(v1y10)
    v1x11 = person1[frame][20] - person1[frame][18]
    v1.append(v1x11)
    v1y11 = person1[frame][21] - person1[frame][19]
    v1.append(v1y11)
    v1x12 = person1[frame][24] - person1[frame][22]
    v1.append(v1x12)
    v1y12 = person1[frame][25] - person1[frame][23]
    v1.append(v1y12)
    v1x13 = person1[frame][26] - person1[frame][24]
    v1.append(v1x13)
    v1y13 = person1[frame][27] - person1[frame][25]
    v1.append(v1y13)

    v2x1 = person2[frame][2] - person2[frame][0]
    v2.append(v2x1)
    v2y1 = person2[frame][3] - person2[frame][1]
    v2.append(v2y1)
    v2x2 = person2[frame][4] - person2[frame][2]
    v2.append(v2x2)
    v2y2 = person2[frame][5] - person2[frame][3]
    v2.append(v2y2)
    v2x3 = person2[frame][16] - person2[frame][2]
    v2.append(v2x3)
    v2y3 = person2[frame][17] - person2[frame][3]
    v2.append(v2y3)
    v2x4 = person2[frame][22] - person2[frame][2]
    v2.append(v2x4)
    v2y4 = person2[frame][23] - person2[frame][3]
    v2.append(v2y4)
    v2x5 = person2[frame][10] - person2[frame][2]
    v2.append(v2x5)
    v2y5 = person2[frame][11] - person2[frame][3]
    v2.append(v2y5)
    v2x6 = person2[frame][6] - person2[frame][4]
    v2.append(v2x6)
    v2y6 = person2[frame][7] - person2[frame][5]
    v2.append(v2y6)
    v2x7 = person2[frame][8] - person2[frame][6]
    v2.append(v2x7)
    v2y7 = person2[frame][9] - person2[frame][7]
    v2.append(v2y7)
    v2x8 = person2[frame][12] - person2[frame][10]
    v2.append(v2x8)
    v2y8 = person2[frame][13] - person2[frame][11]
    v2.append(v2y8)
    v2x9 = person2[frame][14] - person2[frame][12]
    v2.append(v2x9)
    v2y9 = person2[frame][15] - person2[frame][13]
    v2.append(v2y9)
    v2x10 = person2[frame][18] - person2[frame][16]
    v2.append(v2x10)
    v2y10 = person2[frame][19] - person2[frame][17]
    v2.append(v2y10)
    v2x11 = person2[frame][20] - person2[frame][18]
    v2.append(v2x11)
    v2y11 = person2[frame][21] - person2[frame][19]
    v2.append(v2y11)
    v2x12 = person2[frame][24] - person2[frame][22]
    v2.append(v2x12)
    v2y12 = person2[frame][25] - person2[frame][23]
    v2.append(v2y12)
    v2x13 = person2[frame][26] - person2[frame][24]
    v2.append(v2x13)
    v2y13 = person2[frame][27] - person2[frame][25]
    v2.append(v2y13)

    sum = 0.0
    count = 0

    for i in range(0, int(len(v1)/2)):
        sum += vectorDifference(v1[count], v1[count+1], v2[count], v2[count+1])
        count += 2

    avg = sum/(len(v1))

    return avg