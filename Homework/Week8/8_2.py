# 2.จงเขียนโปรแกรมในการหาความยาวของเส้นรอบรูปของส่วนที่แรเงาที่อยู่ภายในสี่เหลี่ยมด้านเท่า
# จากข้อมูลความยาวของด้านๆหนึ่งของสี่เหลี่ยมด้านเท่าที่ผู้ใช้ป้อนเข้ามา ดังตัวอย่างการรันโปรแกรม

# Enter the width of the square (centimeter): 5
# Total length of shaded circumference is 31.43 centimeter.

# Enter the width of the square (centimeter): 7
# Total length of shaded circumference is 44.00 centimeter.

pi = 3.143
width = int(input("Enter the width of the square (centimeter): "))
shaded_circumference = 2 * pi * width
print("Total length of shaded circumference is %.2f centimeter." % shaded_circumference)

