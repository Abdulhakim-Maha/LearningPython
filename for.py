List = [1,2,3]
List2 = [3,4,5]
print([i*j for i in List for j in List2])

# while loop
sum = 0;
x = 0;

while x != -1 :
	x = int(input('Enter number to sum (-1 to end):')) 
	if(x == -1) :
		break
	sum += x
print(sum)

arr = [1,2,3,4]
print(arr[-1:0:-1])

