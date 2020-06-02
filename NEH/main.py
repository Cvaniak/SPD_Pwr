import os
import glob
import itertools
from copy import deepcopy
from copy import copy
# import numpy as np
lenT = 0

def load_pwd(nazwa):
    global lenT
    file_handler = open(os.getcwd()+"\\"+ nazwa, 'r')
    file_data = file_handler.readlines()
    PWD = list()
    i = 0
    # lenT = int(file_data[0].split()[1])
    lenT = int(file_data[1].split()[1])
    # print(lenT, type(lenT))
    for index, line in enumerate(file_data[1:]):
    # for index, line in enumerate(file_data[1:]):
        # print(" ".join(line.split()))
        newline = list(map(int, line.split()[1::2]))
        # print(newline)
        if( len(newline) != lenT):
            continue
        PWD.append(newline)


    file_handler = open(os.getcwd()+"\\"+ "opt.txt", 'r')
    file_data = file_handler.readlines()

    return PWD, file_data[0].split()[1]
file_t = ["ta001.txt"]

# def Cmax(listT):
#     global lenT
#     sumT = 0
#     timeT = [0]*lenT
#     for i in range(len(listT)):
#         timeT[0] = timeT[0] + listT[i][0]
#         for k in range(1,lenT):
#             timeT[k] = max(timeT[k-1], timeT[k]) + listT[i][k]
#     return timeT[lenT-1]

# def Cmax(listT):
#     global lenT
#     sumT = 0
#     timeT = [[0 for x in range(lenT+1)] for y in range(len(listT)+1)]
#
#
#     for j in range(1, lenT + 1):
#         timeT[0][j] = timeT[0][j - 1] + listT[0][j-1]
#     #     timeT[0][j] = timeT[j - 1][0] + listT[0][j-1]
#
#     for i in range(1, len(listT)):
#         timeT[i][0] = timeT[i-1][0] + listT[i][0]
#         for k in range(1, lenT+1):
#             timeT[i][k] = max(timeT[i][k-1], timeT[i-1][k]) + listT[i][k-1]
#
#     # print(timeT)
#     return timeT[len(listT)-1][lenT-1]

def Cmax(listT):
    global lenT
    sumT = 0
    timeT = [0]*lenT

    for i in range(lenT):
        timeT[i] = sumT + listT[0][i]
        sumT = timeT[i]

    for i in listT[1:]:
        sumT = 0
        for k in range(lenT):
            timeT[k] = max(sumT, timeT[k]) + i[k]
            sumT = timeT[k]
    return sumT


def NEH(file_t):
    global lenT
    dane,  resultT = load_pwd(file_t)
    # print(dane)
    result = 0

    # Disctionary index: sum
    W = list(zip(range(len(dane)), [sum(i) for i in dane]))
    W.sort(key=lambda x: x[1])
    print(W, W[7])
    # cos1 = copy(W[7])
    # W[7] = copy(W[6])
    # W[6] = cos1
    # cos1 = copy(W[9])
    # W[9] = W[8]
    # W[8] = cos1
    cos1 = copy(W[11])
    W[11] = W[12]
    W[12] = cos1


    print(W, W[7])
    Pi = []
    PiT = []
    # j = W.pop()[0]
    # Pi.append(dane[j])
    # Pi.copy().insert(0, dane[0])
    # print(Pi)
    k = 1

    while len(W):
        j = W.pop()[0]
        PiT.append(dane[j])
        for l in range(k):
            Pi.insert(l, dane[j])
            if Cmax(Pi) < Cmax(PiT):
                PiT =copy(Pi)
            del Pi[l]
        Pi = copy(PiT)
        k += 1


    # while len(W):
    #     j = W.pop()[0]
    #     # print(j,dane[j], Pi.copy())
    #     # PiT.insert(0, dane[j])
    #
    #     for i in range(1, len(Pi)+1):
    #         PiTT = Pi.copy()
    #         PiTT.insert(i, dane[j])
    #         PiT.append(PiTT)
    #     PiT.sort(key=Cmax)
    #     # for i in PiT:
    #     #     print(Cmax(i), end=" ")
    #     # print()
    #     Pi = PiT[0]
    #     PiT = []

        # for i in Pi:
        #     print(dane.index(i)+1, end=" ")
        # print()

    result = Cmax(Pi)
    print(file_t, result)
    # for i in Pi:
    #     print(dane.index(i)+1, end=" ")

    # print()

# NEH("ta003.txt")
os.chdir("./")
ind = 0
for file in glob.glob("ta*.txt"):
    NEH(file)
    ind += 1
    if(ind == 8):
        break

#  1286
#  1365
#  1159
#  1325
#  1305
#  1228
#  1278
#  1223

# ta001.txt 1286
# ta002.txt 1365
# ta003.txt 1140
# ta004.txt 1340
# ta005.txt 1305
# ta006.txt 1228
# ta007.txt 1279
# ta008.txt 1235

# ta001.txt 1204
# ta002.txt 1362
# ta003.txt 1132
# ta004.txt 1268
# ta005.txt 1149
# ta006.txt 1195
# ta007.txt 1283
# ta008.txt 1220

# 7 12
# 7 12 5
# 18 7 12 5
# 20 18 7 12 5
# 20 18 7 12 5 9
# 20 18 7 12 5 9 17
# 20 18 7 12 5 9 17 6
# 20 18 7 1 12 5 9 17 6
# 20 18 7 1 12 5 9 17 6 11
# 16 20 18 7 1 12 5 9 17 6 11
# 16 20 18 7 1 12 5 9 14 17 6 11
# 16 20 18 7 1 12 5 9 14 17 6 11 8
# 16 20 18 7 1 12 5 9 19 14 17 6 11 8
# 16 3 20 18 7 1 12 5 9 19 14 17 6 11 8
# 16 3 20 18 7 1 12 10 5 9 19 14 17 6 11 8
# 16   3  20  18   7   1  12  10   5   9  19  14  17   6  11   8
#
# 16 4 3 20 18 7 1 12 10 5 9 19 14 17 6 11 8
# 16   3  20  18   7   1  12  10   5   2   9  19  14  17   6  11   8

# 16 4 3 20 18 7 1 12 10 5 9 19 14 17 6 2 11 8
# 16 4 3 20 18 7 1 12 10 5 9 19 14 17 6 2 11 13 8
# 16 4 3 20 18 7 1 12 10 5 9 19 14 15 17 6 2 11 13 8