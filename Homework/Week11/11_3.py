# 3.จงเขียนโปรแกรมเพื่อใช้ลูป for ในการแสดงตัวอักษร 'X' ออกที่จอภาพ (ในบรรทัดที่ 1
# และบรรทัดสุดท้ายให้แดสงตัวอักษร '-' จำนวน 7 ตัว) ดังตัวอย่างการรันโปรแกรม
    
# Using for loop to draw a character 'X'
# -------
# x     x
#  x   x
#   x x
#    x
#   x x
#  x   x
# x     x
# -------


size = 9
print('-' * 7)  

for i in range(size):
    if i == 0 or i == size - 1:
        continue 
    for j in range(size):
        if j == i or j == size - i - 1:
            print('x', end='')
        else:
            print(' ', end='')
    print()
print('-' * 7) 

