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

print(*[num**2 for num in range(n)], sep='\n')