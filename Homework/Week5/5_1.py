# 1.จงเขียนโปรแกรมในการกำหนดตัวแปร location = '1234567890'
# ตัวแปร name = 'Anna' ตัวแปร sex = 'F' ตัวแปร age = 19 และตัวแปร gpa = 3.25
# แล้วแสดงผลของตัวแปรเหล่านั้นออกที่จอภาพโดยกำหนดจำนวนช่องที่ต้องการแสดงผลคู่กับเครื่องหมาย % ต่างๆ
# แสดง name , sex และ age ชิดซ้ายของหัวข้อ และแสดง gpa ชิดขวาของหัวข้อ ดังตัวอย่างการรันโปรแกรม

# 1234567890123456789012345678901234567890
# NAME           SEX       AGE         GPA
# Anna           F         19     3.250000

location = "1234567890"
name = "Anna"
sex = "F"
age = 19
gpa = 3.25

print("%s"%location*4)
print("NAME           ",end="")
print("SEX       ",end="")
print("AGE         ",end="")
print("GPA")
print("%0s%12s%11d%18.6f"%(name,sex,age,gpa))