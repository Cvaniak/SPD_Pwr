import os
import itertools
import numpy as np
def load_pwd(nazwa):
    file_handler = open(os.getcwd()+"\\"+ nazwa, 'r')
    file_data = file_handler.readlines()
    PWD = list()
    i = 0
    for index, line in enumerate(file_data):
        newline = list(map(int, line.split()))
        newline.insert(0, index)
        if( len(newline) != 4):
            continue
        PWD.append(newline)
    return PWD

def foox(tablica):
    C=0
    F=0
    for i in tablica:
        C = C + i[1]
        T = max(C - i[3],0)
        K = T*i[2]
        F = F + K

    return F

def all_permutation(data):
    min_value = float('inf')
    for i in itertools.permutations(data):
        min_value = min(foox(i), min_value)
    return min_value

def all_permutation_3(data):
    min_value = float('inf')
    for i in itertools.permutations(data):
        min_value = min(foox(i), min_value)
    return min_value


def kolejnosc(lista):
    y = []
    for item in lista:
        y.append(item[0])
    return y



def zad1(file_t):
    for j in file_t:
        dane = load_pwd(j)
        n = len(dane)
        wynik = foox(dane)
        print("-------------------------------")
        print("Plik: ", j)
        print("Wynik nieposo:", wynik)
        dane.sort(key=lambda x: x[3])
        wynik = foox(dane)
        print("Wynik poso:", wynik)
        print("-------------------------------")
        print(kolejnosc(dane))

def zad2(file_t):
    dane = load_pwd(file_t)
    wynik = all_permutation(dane)
    print("Plik: ", file_t)
    print("Wynik: ", wynik)



def filt(a):
    if(a == 0):
        return 0
    else:
        return 1

def zad3(file_t):
    for j in file_t[:1]:
        dane = load_pwd(j)
        # print(dane)
        dane.sort(reverse=True)
        # print(dane)
        result = {}
        n = len(dane)
        result[bin(0)[2:].zfill(n)] = 0
        for i in range(2**(len(dane))):
            bin_a = bin(i)[2:].zfill(len(dane))
            bin_list = list(map(int, bin_a))
            # print("bin", bin_list)
            # print(list(   [val for i, val in enumerate(dane[:len(bin_list)]) if bin_list[i]]    ))
            res_list = list(   [val for i, val in enumerate(dane[:len(bin_list)]) if bin_list[i]])
            min_val = float('inf')

            if not len(res_list):
                continue

            p_sum = np.sum(res_list, 0)[1]
            # print("psum", p_sum)
            for index, item in enumerate(res_list):
                # print(item, index, bin_a, ("".join( (bin_a[:-item[0]],"0",bin_a[-item[0]+1:]) ))[:n])
                # print(result)
                min_val = min(min_val, max(p_sum - item[3], 0)*item[2] + result[ "".join( (bin_a[:-item[0]],"0",bin_a[-item[0]+1:]) )[:n] ])# str( list(bin_list[:i[0]] + "0" + bin_list[i[0]+1:]) )
            result[bin_a] = min_val
            if(bin_a.count("1")==1):
                print(min_val, bin_a)
        print("result", min_val)
        # print(result)



result_4 = {}
dane_4 = 0

def rep(a, b, c):
    a = list(a)
    a[b-1] = c
    # print(a, b, c)
    return "".join(a)

def foo(dane):
    global dane_4
    global result_4
    result = float('inf')
    x = 0
    bin_a = bin(0)[2:].zfill(dane_4)
    for item in dane:
        bin_a = rep(bin_a,item[0],"1")
    p_sum = np.sum(dane, 0)[1]
    for i in dane:
        bin_i = rep(bin_a, i[0], "0")
        if(bin_i.count("1") ==0):
            return max(p_sum - i[3], 0) * i[2]
        if(result_4[bin_i] == -1):
            dane1 = dane[:]
            dane1.remove(i)
            result_4[ bin_i] = foo(dane1)

        x = max(p_sum - i[3], 0) * i[2]
        result = min(result, x + result_4[bin_i])

    return result


def zad4(file_t):
    dane = load_pwd(file_t[0])
    global dane_4
    global result_4
    dane.sort(reverse=True)
    dane_4 = len(dane)
    print(dane_4)
    for i in range(2**dane_4):
        bin_a = bin(i)[2:].zfill(dane_4)
        result_4[bin_a] = -1

    result = foo(dane)
    print("hej", result)

file_t = ["data10.txt", "data11.txt", "data12.txt", "data13.txt", "data14.txt", "data15.txt", "data16.txt", "data17.txt",
         "data18.txt", "data19.txt", "data20.txt"]

# a = load_pwd("data10.txt")
# zad1(file_t)
# zad2(file_t[0])
zad3(file_t)
zad4(file_t)
# p = [[1,2,3], [1,2,3], [1,2,3],[1,2,3]]
# print("lel")
# bin_a = "123456789"
# index = 1
# print("".join( (bin_a[:-index-1],"0",bin_a[-index:])))

# 81 3 187
# 71 7 26
# 68 5 462
# 80 2 257
# 92 7 322
# 58 9 455