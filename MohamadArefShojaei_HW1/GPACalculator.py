# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

grades = input('please insert grades and split them by spaces ').split()
grades_int = []

for i in grades:
    g=int(i)
    if g > 20:
        print('invalid grade')
        exit()
    grades_int.append(g)

avg = 0
sum = 0

for i in grades_int:
    sum += i

avg = sum/5

if avg >= 18 and avg < 20:
    print('A')
elif avg >= 15 and avg < 17.99:
    print('B')
elif avg >= 12 and avg < 14.99:
    print('C')
elif avg >= 0 and avg < 11.99:
    print('f')
