# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

def indexLocation(nums: int, target: int) -> int:
    loc = 0

    for i in range(len(nums)):
        if nums[i] == target:
            loc = i
            break
        elif nums[i] < target:
            loc = i+1
        
    return loc


numlist = input("please enter the list of numbers: ").split()
target = int(input("please enter the target number: "))

nums = list(map(int, numlist))


print(indexLocation(nums, target))
