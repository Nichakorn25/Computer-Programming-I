# 3.จงเขียนโปรแกรมเพื่อรับข้อมูลที่เป็นชื่อ 1 ชื่อ รับข้อมูลเพศ (ตัวอักษรตัว 1 ตัว คือ M แทนผู้ชายหรือ F แทนผู้หญิง)
# รับข้อมูลเกรดเฉลี่ย 1 จำนวน แล้วแสดงชนิดข้อมูลของตัวแปรเหล่านั้นออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# NAME: Somsak
# SEX (M/F): M
# NUMBER (1000-9999): 1234
# GPA: 2.90
# Type of name is -> <class 'str'>
# Type of sex is -> <class 'str'>
# Type of number is -> <class 'int'>
# Type of gpa is -> <class 'float'>

name = input("NAME: ")
sex = input("SEX (M/F): ")
number = int(input("NUMBER (1000-9999): "))
gpa = float(input("GPA: "))
print("Type of name is -> %s>"%type(name))
print("Type of sex is -> %s>"%type(sex))
print("Type of number is -> %s>"%type(number))
print("Type of gpa is -> %s>"%type(gpa))