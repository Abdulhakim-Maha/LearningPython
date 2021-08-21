print('*** Rabbit & Turtle ***')
d,Vr,Vt,Vf = [int(i) for i in input('Enter Input : ').split()]
t = d / Vt
Sf = Vf * t * 2
print('{:.2f}'.format(Sf))