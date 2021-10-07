inp = [int(x) for x in input("Enter number end with (-1) : ").split()]
if not -1 in inp:
    print("Invalid INPUT !!!")
    quit()
number = []
for i in inp:
    if i == -1:
        break
    else:
        number.append(i)
average = len(number)/2

for i in number:
    if number.count(i) > average:
        print(i)
        quit()
print("Not found")
