class Vector:
	def __init__(self,d) -> None:
		self.coor = [0] * d
		print(type(self.coor))
	def __len__(self):
		return len(self.coor)
	def __getitem__(self,j):
		return self.coor[j]
	def __setitem__(self,j,val):
		self.coor[j] = val
	def __str__(self) -> str:
		return '<' + str(self.coor)[1:-1] + '>'
	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError('dimension invalid!')
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = self[i] + other[i]
		return result

if __name__ == '__main__':
	v = Vector(3)
	v[0] = 3
	u = Vector(3)
	u[2] = 5
	print(v,u)
	r = u + v
	print(r) 
	print(type(r),r[1])
	print(isinstance(r,Vector))
	
