# this code has been programmed by Aref
# github.com/M-Aref-Shojaei


numLine = input("Enter the number of numbers: ").split()
nums = list(map(int, numLine))

maxNum = max(nums)
minNum = min(nums)

normilized_list = []

for num in nums:
    normilized_list.append((num-minNum)/(maxNum-minNum))

print(normilized_list)
