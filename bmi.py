weight = int(input('ป้อนน้ำหนักของคุณ (kg):'))
height = int(input('ป้อนส่วนสูงของคุณ (cm):'))/100
bmi = weight/height**2
print('ค่าดัชนีมวลกายของคุณคือ ' + str(bmi))
