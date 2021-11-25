count = 0
def bubbleSort(array):
    global count
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            count += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

        if not swapped:
            break

print(" *** Bubble sort ***")
inp = list(map(int,input("Enter some numbers : ").split()))
bubbleSort(inp)
print()
print(inp)
print("Data comparison =", count)