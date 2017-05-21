from collections import deque

def min_lexographical_string(string1,string2):
    min_string = ''
    i1 = 0
    i2 = 0
    len1 = len(string1)
    len2 = len(string2)
    while i1 < len1 and i2 < len2:
        if string1[i1] < string2[i2]:
            min_string = min_string + string1[i1]
            i1 += 1
        elif string1[i1] > string2[i2]:
            min_string = min_string + string2[i2]
            i2 += 1
        else:
            j = 1
            while i1+ j < len1 and i2 + j < len2 and string1[i1+j] == string2[i2+j] and string1[i1+j] <= string1[i1]:
                j+= 1
            if  i1+ j == len1:
                min_string = min_string + string2[i2:i2+j]
                i2 += j
            elif i2 + j == len2 :
                min_string = min_string + string1[i1:i1+j]
                i1 += j
            elif string1[i1+j] < string2[i2+j]:
                min_string = min_string + string1[i1:i1+j+1]
                i1 += j + 1
            elif string1[i1+j] > string2[i2+j]:
                min_string = min_string + string2[i2:i2+j+1]
                i2 += j + 1
            else:
                min_string = min_string + string1[i1:i1+j] + string2[i2:i2+j]
                i1 += j
                i2 += j
    if i1 < len1:
        min_string = min_string + string1[i1:]
    else:
        min_string = min_string + string2[i2:]
    return min_string

def min_lexographical_string_v2(string1,string2,check_string):
    min_string = ''
    i1 = 0
    i2 = 0
    i_check = 0
    len1 = len(string1)
    len2 = len(string2)
    while i1 < len1 and i2 < len2:
        if string1[i1] < string2[i2]:
            min_string = min_string + string1[i1]
            if string1[i1] != check_string[i_check]:
                print('C0')
            i1 += 1
            i_check += 1
        elif string1[i1] > string2[i2]:
            min_string = min_string + string2[i2]
            if string2[i2] != check_string[i_check]:
                print('C1',string1[i1] , string2[i2])
            i2 += 1
            i_check += 1
        else:
            j = 1
            while i1+ j < len1 and i2 + j < len2 and string1[i1+j] == string2[i2+j] and string1[i1+j] <= string1[i1]:
                j+= 1
            if  i1+ j == len1:
                min_string = min_string + string2[i2:i2+j]
                if string2[i2:i2+j] != check_string[i_check: i_check +j]:
                    print('C1.5')
                i2 += j
                i_check += j
            elif i2 + j == len2 :
                min_string = min_string + string1[i1:i1+j]
                if string1[i1:i1+j] != check_string[i_check: i_check +j]:
                    print('C2')
                i1 += j
                i_check += j
            elif string1[i1+j] < string2[i2+j]:
                min_string = min_string + string1[i1:i1+j+1]
                if string1[i1:i1+j+1] != check_string[i_check: i_check +j+1]:
                    print('C3')
                i1 += j + 1
                i_check += j+1
            elif string1[i1+j] > string2[i2+j]:
                min_string = min_string + string2[i2:i2+j+1]
                if string2[i2:i2+j+1] != check_string[i_check: i_check +j+1]:
                    print('C4')
                i2 += j + 1
                i_check += j+1
            else:
                min_string = min_string + string1[i1:i1+j] + string2[i2:i2+j]
                if string1[i1:i1+j] + string2[i2:i2+j] != check_string[i_check: i_check +j+j]:
                    print('C5')
                i1 += j
                i2 += j
                i_check += 2*j
    if i1 < len1:
        min_string = min_string + string1[i1:]
        if string1[i1:] != check_string[i_check: ]:
            print('C6',len1,len2,string1[1:] == string2[:])
            print(min_string[i_check:i_check+3] , check_string[i_check:i_check+3])
            print(string1[:3],string1[-3:],string2[:3],string2[-3:])
            print(check_string[:3],check_string[-3:])
    else:
        min_string = min_string + string2[i2:]
        if string2[i2:] != check_string[i_check: ]:
            print('C7', i1,len1,i2,len2)
    return min_string

def morgan_and_string():
    n = int(input())
    for _ in range(n):
        string1 = input()
        string2 = input()
        print(min_lexographical_string(string1,string2))
    return None

def morgan_and_string_v2():
    with open('morgan_input.txt') as input_file, open('morgan_check.txt') as check_file:
        check_strings = [line.strip() for line in check_file]
        input_strings = [line.strip() for line in input_file]
        for i in range(len(check_strings)):
            string1 = input_strings[2*i+1]
            string2 = input_strings[2*i+2]
            check_string = check_strings[i]
            a = min_lexographical_string_v2(string1,string2,check_string)
            if a != check_string:
                print('False', i)
            else:
                print('True')


    # return None

morgan_and_string_v2()
