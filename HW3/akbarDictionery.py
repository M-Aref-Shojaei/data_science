# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

dictionery = []
line_num = int(input("Enter the number of lines: "))

for i in range(line_num):
    line = input("Enter a line(please splite words with space): ").split()
    dictionery.append({line[0]: line[1]})


original_line = input(
    'please enter the original line which you want to translate : ').split()

translated = ''
for word in original_line:
    for tran in dictionery:
        if word in tran:
            translated += tran[word] + ' '
            break
    else:
        translated += word + ' '
print(translated)
