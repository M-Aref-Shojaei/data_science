# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

inserted_word = input("please enter a word : ").lower()

if inserted_word == '':
    print('The input is empty please run program again!')
    exit()


length = inserted_word.__len__()-1
palindrome = True

for i in range(length):
    if inserted_word[i] != inserted_word[length-i]:
        palindrome = False
        break

if palindrome:
    print("Yes")
else:
    print("No")
