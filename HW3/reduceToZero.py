# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

count = 0

num = int(input('please enter a number : '))

while num != 0:
    if num % 2 == 0:
        num /= 2
        count += 1
    elif num % 2 == 1:
        num -= 1
        count += 1

print(count)
