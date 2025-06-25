# 1.จงเขียนโปรแกรมเพื่อใช้ลูป for แสดงตัวอักษร A ถึง Z โดยแสดงบรรทัดละ 5 ตัวอักษร
# แล้วแสดงจำนวนของตัวอักษรทั้งหมดที่ถูกแสดงออก ดังตัวอย่างการรันโปรแกรม

# Using for loop to print A to Z (5 characters per line)
# A B C D E 
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y 
# Z 
# Total = 26


count = 0 
for i in range(65, 91):  
    print(chr(i), end=' ')
    count += 1

    if count % 5 == 0:
        print() 

print("\nTotal =", count)
