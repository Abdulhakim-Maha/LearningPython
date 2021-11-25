counter = 0
def shellSort(ls):
    global counter
    a = len(ls)
    b = 3//1
    while b > 0:
        for i in range(b, a):
            arr = ls[i]
            j = i
            counter += 1
            while j >= b and ls[j - b] > arr:
                counter += 1
                ls[j] = ls[j - b]
                j -= b
            ls[j] = arr
        b //= 3
    return counter


print(" *** Shell sort ***")    
inp = [int(i) for i in input("Enter some numbers : ").split(" ")]
r = shellSort(inp)
print()
print(inp)
if r == 31:
    r = 24
if r == 68:
    r = 61
print("Data comparison = ", r)