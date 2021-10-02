from calendar import calendar

import math
import random
import re
import os
import sys

# def raw_input():
#   pass


# if __name__ == '__main__':
#   n = int(raw_input().strip())

# if(n%2!=0):
#   print("Weird")
# elif(n%2==0 & n in range(2,5)):
#   print("not weird")
# elif(n%2==0 & n in range(6,20)):
#   print("weird")
# else:
#   print("Not Weird")

n = 3

# if n % 2 != 0:
#   print("Weird")
# if(n % 2 == 0 & (2 <= n <= 5)):
#   print("Not Weird")
# if(n % 2 == 0 & (5 < n < 21)):
#   print('Weird')
# else:
#   print("Not Weird")

if (n % 2 == 0):
    if (n in range(2, 5)):
        print("Not Weird")
    elif (n in range(6, 21)):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")

# a = int(input())
# b = int(input())
a = 6
b = 10
print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))

n = 5
i = 0
while i <= n - 1:
    print(i * i)
    i += 1

for j in range(n):
    print(j * j)

print(*[num ** 2 for num in range(n)], sep='\n')


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
            return leap
    else:
        leap = False
    return leap


year = 1992
print(is_leap(year))


def is_leap(year1):
    return year1 % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year1 = 1989
print(is_leap(year1))

# def is_leap1(year2): pass
# print(calendar.isleap1(int()))
# exit()

# year2 = 1992
# print(is_leap1(year2))
n = 5
for i in range(n):
    j = i + 1
    print(j, end="")

# without list comphresions
Cars = ["bmw", "skodu", "mahindra", "tata", "maruti"]
car_indian = []

for x in Cars:
    if 'a' in x:
        car_indian.append(x)
print(car_indian)

# with list comphresions :
car_a = [x for x in Cars if 'a' in x]
print(car_a)

# if we are not using list comphresions we need to use for loop

# expression-involving-loop-variable for loop-variable in sequence
listofnumber = [z for z in range(10)]
print(listofnumber)
# list comphresion can be nested
# expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence

# format as
# result = []
# for outer_loop_variable in outer_sequence:
#   for inner_loop_variable in inner_sequence:
#       results.append(expression invlovling loop_variable)

result = []
for x in range(3):
    for y in range(4, 6, 1):
        result.append([x, y])

print(result)

result1 = []
print([[x, y] for x in range(3) for y in range(4, 6, 1)])

# The final form of list comprehension involves creating a list and filtering it similar to using the filter() method.
# The filtering form of list comprehension takes the following form
# it will return a boolean value and will store only those value which meets True condition.
listofnumbers = [x for x in range(10) if x % 3 == 0]
print(listofnumbers)

# x,yand z are variable get all pc in 3d format with x+y+z != n
# print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

m = 5
arr = [2, 4, 6, 3, 8]
z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print(max(arr))


# An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
# Familiar examples of iterables include lists, tuples, and strings - any such sequence can be iterated over in a for-loop.

def addition(n):
    return n + n


print(addition(2))

number = [1, 2, 3, 4]
result = map(addition, number)
print(list(result))

string = 'vedved'
print(lambda string: string)
# to get the runner up score
n = [1, 2, 4, 7, 5, 6]
print(sorted(list(set(n)))[-2])

#n = [1, 2, 2, 2, 8]
print(set(n))
print(sorted(n))

m = list(dict.fromkeys(n))
print(m)
m.sort()
#m.reverse()
print(m[-2])




