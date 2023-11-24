# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

# list approuch

text = input("Please enter the text : ").split()
word = input("Please enter the specific word you looking for it : ")
count = 0

for w in text:
    if w == word:
        count += 1


print(count)


# string methods approuch
#this method has a tiny bug. the bug is that it could not be 100% accurate as previous approuch so it count all the words which has the word in them 
# for example if the text is : 'the dogs barked' and the word is : 'dog' then the count will be 1


text = input("Please enter the text : ")
word = input("Please enter the specific word you looking for it : ")
count = 0

word_len = word.__len__()-1
while True:
    index = text.find(word)
    if index == -1:
        break
    count += 1
    text = text[:index+word_len]


print(count)
