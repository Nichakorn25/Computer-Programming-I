# 3.จงเขียนโปรแกรมเพื่อกำหนดตัวแปร
# n = 25
# f = 98.76543210
# s = 'C-TO-PYTHON-2024'
# หลังจากนั้นให้ใช้คำสั่ง print() แสดงข้อมูลของตัวแปร n, f และ s ในตำแหน่งต่างๆ
# ออกที่จอภาพตาม ดังตัวอย่างการรันโปรแกรม

# n is equal to 25
# f is equal to 98.765432
# s contains "C-TO-PYTHON-2024" 
# The length of s is 16
# Found "-" in string "C-TO-PYTHON-2024" at 1
# C-TO-PYT
# 2
# PYTHO
# 2OYO

n = 25
f = 98.76543210
s = 'C-TO-PYTHON-2024'

print("n is equal to %d"%n)
print("f is equal to %.6f"%f)
print("s contains %s"%s)
print("The length of s is %d"%(len(s)))
print("Found \"-\" in string \"%s\" at %d"%(s,s.find('-')))
print(s[0:8])
print(s[12])
print(s[5:10])
print(s[-4:-14:-3])