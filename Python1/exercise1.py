print('*** Rabbit & Turtle ***')
d,Vr,Vt,Vf = [int(i) for i in input('Enter Input : ').split()]
total = (d/(Vt-Vr))*Vf
print('{:.2f}'.format(total))