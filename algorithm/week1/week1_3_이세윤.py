fileName = "phone_book.txt"
new_fileName = "new_phone_book.txt"
li = list()
newLi = list()

with open(fileName) as f:
    for line in f:
        li.append(line.rstrip('\n'))
    f.close()

for i in li:
    i = i.replace("-","")
    if not i.startswith("010"):
        del i
    else:
        a = int(i[3:7])
        b = int(i[7:])
        if a > b:
            newLi.append(i)
            
with open(new_fileName, 'w') as f:
    for i in newLi:
        f.write(i + '\n')
    f.close()