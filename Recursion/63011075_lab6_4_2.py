def perket(ls,index,size,binary,i,total):

    if index == len(binary):
        return 1, 0 , total

    sour, bitter , total = perket(ls,index+1,size,bin(i).replace('0b','').zfill(size),i,total)

    if binary[index] == '1':
        s, b = map(int, ls[index].split())
        sour = sour * s
        bitter = bitter + b   

    if i < 2 ** size:
        if( abs(sour - bitter) < total):            
            total =  abs(sour - bitter)
        i += 1
        perket(ls,0,size,bin(i).replace('0b','').zfill(size),i,total)

    if(i == 2 ** size):
        print(total)
        quit()

    return sour , bitter , total
        

inp = input("Enter Input : ").split(',')
size = len(inp)

perket(inp,0,size,bin(1).replace('0b','').zfill(size),1,999)