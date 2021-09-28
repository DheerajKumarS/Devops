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



#def is_leap1(year2): pass
#print(calendar.isleap1(int()))
#exit()

#year2 = 1992
#print(is_leap1(year2))
n=5
for i in range(n):
    j=i+1
    print(j, end="")
