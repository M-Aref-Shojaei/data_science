# this code has been programmed by Aref
# github.com/M-Aref-Shojaei


def thePursuitofHappyness(num: int) -> bool:
    result = False

    for i in range(1, 200):
        if num % 10 == 1:
            result = True
            break
        num = findHappy(num)
    return result


def findHappy(num: int) -> int:

    sum = 0
    while (True):
        smallPart = (num % 10)
        sum += (smallPart)**2
        num = int(num / 10)
        if (num % 10 == num):
            sum += num**2
            break
    return sum


num = int(input("Enter a number: "))

print(thePursuitofHappyness(num))
