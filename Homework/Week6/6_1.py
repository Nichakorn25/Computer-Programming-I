# 1.จงเขียนโปรแกรมเพื่อกำหนดตัวแปร
#             location = '1234567890'
#             n = 153
# หลังจากนั้นให้ใช้คำสั่ง print() เพื่อแสดงผลลัพธ์ต่างๆโดยผ่านตัวแปรออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# 1234567890123456789012345678901234567890
# 153 is equal to 0b10011001 Binary Base
# 153 is equal to 0o231 Octal Base
# 153 is equal to 0x99 Hexadecimal Base
# 1234567890123456789012345678901234567890

location = '1234567890'
n = 153

print(location*4)
print("%d is equal to %s Binary base"%(n,bin(n)))
print("%d is equal to %s Octal base"%(n,oct(n)))
print("%d is equal to %s Hexadecimal base"%(n,hex(n)))
print(location*4)
