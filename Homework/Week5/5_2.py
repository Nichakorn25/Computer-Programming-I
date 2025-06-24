# 2.จงเขียนโปรแกรมรับชื่อ เพศ อายุ และเกรดเฉลี่ย แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม 
# (แสดงเลขหลังจุดทศนิยมของเกรดเฉลี่ย 4 ตำแหน่ง)

# Enter your name: Samart
# Enter your sex: M
# Enter your age: 19
# Enter your gpa: 3.45
# Hello... Samart!
# Your sex is M.
# You are 19 years old.
# Your gpa is 3.4500.

name = str(input("Enter your name: "))
sex = str(input("Enter your sex: "))
age = int(input("Enter your age: "))
gpa = float(input("Enter your gpa: "))

print("Hello... %s !"%name)
print("Your sex is %s ."%sex)
print("You are %d years old."%age)
print("Your gpa is %.4f ."%gpa)