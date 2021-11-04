def Max(lst,i,max):
    value = int(lst[i])
    if(value <= max):
        max = value
    i += 1
    if(i < len(lst)):
        Max(lst,i,max)
    if(i == len(lst)):
        print("Min : " + str(max))

lst = [e for e in input("Enter Input : ").split(" ")]
Max(lst,0,+99999)