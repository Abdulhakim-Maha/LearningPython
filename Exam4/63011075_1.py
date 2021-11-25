def bi_search(index, lastIndex, array, y):
    if index > lastIndex:   
        return "Not found"

    middle = (index+lastIndex)//2     

    if y == array[middle]:           
        return "Found"
    elif y < array[middle]:                             
        return bi_search(index, middle-1, array, y)        
    elif y > array[middle]:                             
        return bi_search(middle+1, lastIndex, array, y)    

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))