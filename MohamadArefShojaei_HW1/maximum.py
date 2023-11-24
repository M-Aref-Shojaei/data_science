# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

import sys

numbers = input('please insert 3 number and split them by spaces ').split()

numbers = [int(n) for n in numbers]

max = -sys.maxsize - 1

for i in numbers:
    if i > max:
        max = i

print(max)
