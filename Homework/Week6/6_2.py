# 2.จงเขียนโปรแกรมเพื่อกำหนดให้ตัวแปร
# upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# location = '1234567890'
# หลังจากนั้นให้ใช้คำสั่ง print()แสดงข้อมูลของตัวแปร location และ upper ในตำแหน่งต่างๆออกที่จอภาพตาม
# ดังตัวอย่างการรันโปรแกรม

# 1234567890123456789012345678901234567890
# Variable upper contains "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
# The length of upper is 26.
# H 
# KLMNOPQRSTUVWXYZ
# FGHIJKLM
# ACEGIKMOQSUWY
# ZXVTRPNLJHFDB
# 1234567890123456789012345678901234567890

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
location = '1234567890'

print(location*4)
print("Variable upper contains \"%s\"."%upper)
print("The length of upper is %d ."%len(upper))
print(upper[7])
print(upper[10:26])
print(upper[5:13])
print(upper[0:25:2])
print(upper[-1:-26:-2])
print(location*4)