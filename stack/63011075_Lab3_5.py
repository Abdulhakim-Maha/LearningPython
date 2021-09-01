class Stack:
	def __init__(self):
		self.stack =[]
	def push(self,i):
		self.stack.append(i)
	def pop(self):
		return self.stack.pop()
	def isEmpty(self):
		return True if len(self.stack) == 0 else False
	def get_items(self):
		return self.stack
	def get_lenght(self):
		return len(self.stack)
	def find_car(self,n):
		try:
			return self.stack.index(n)
		except ValueError:
			return -1
	def depart(self,n):
		self.stack.remove(n)

		
print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
s = [int(e) for e in s.split(',')]
st = Stack()
for i in s:
	if i == 0:
		continue
	st.push(i)

if o == 'arrive':
	if st.get_lenght() < m and st.find_car(n) == -1:
		st.push(n)
		print('car',n,'arrive! : Add Car',n)
	elif st.get_lenght() == m:
		print('car',n,'cannot arrive : Soi Full')
	elif st.get_lenght() < m and st.find_car(n) != -1:
		print('car',n,'already in soi')

elif o == 'depart':
	if st.get_lenght() == 0:
		print('car',n,'cannot depart : Soi Empty')
	elif st.find_car(n) != -1:
		st.depart(n)
		print('car',n,'depart ! : Car',n,'was remove')
	elif st.find_car(n) == -1:
		print('car',n,'cannot depart : Dont Have Car',n)
		
print(st.get_items())

