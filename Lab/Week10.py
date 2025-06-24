#แลปในสไลด์

# 10.1 เขียนโปรแกรมโดยใช้ลูป for ในการพิมพ์เลขจ านวนเต็มจาก 1 ถึง 9
# ออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Printing 1 to 9 using for loop ...
# 1, 2, 3, 4, 5, 6, 7, 8 and 9.
# End Program !!!

# print("Printing 1 to 9 using for loop ...")

# for i in range(1, 10):
#     if i < 9:
#         print(i, end=", ")
#     else:
#         print("and", i + ".", sep=" ")
# print("End Program !!!")


# =================================================================================

# 10.2 เขียนโปรแกรมโดยใช้ลูป while ในการวนลูปรับเลขจ านวน
# เต็ม 1 ถึง 10 เท่านั้น ถ้าไม่อยู่ในพิสัยให้วนลูปรับข้อมูลใหม่
# จนกว่าจะได้ข้อมูลที่ต้องการ หลังจากนั้น ให้ใช้ลูป while
# เพื่อพิมพ์เลขจ านวนนั้นมาจนถึง 1 โดยพิมพ์เฉพาะเลขคึ่
# เท่านั้น พร้อมกับบอกผลรวมของเลขเหล่านั้นออกที่จอภาพ
# ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Using while loop ...
# Enter a number (1-10): 30
# Enter a number (1-10): -5
# Enter a number (1-10): 8
# 7 5 3 1
# Sum = 16

# print("Using while loop ...")
# num = 0
# while num < 1 or num > 10:
#     num = int(input("Enter a number (1-10): "))

# i = num
# total = 0
# while i >= 1:
#     if i % 2 == 1:
#         print(i, end=" ")
#         total += i
#     i -= 1
# print(f"\nSum = {total}")


# =================================================================================


# extra เขียนโปรแกรมรับเลขจ านวนเต็ม 1 ถึง 9 เท่านั้น
# จ านวน 3 ตัว เก็บไว้ที่ตัวแปร a, b และ c ตามล าดับ
# โดยแต่ละตัวจะต้องไม่ซ้ ากัน ถ้าไม่อยู่ในพิสัยหรือ
# ซ้ ากันให้วนลูปรับข้อมูลใหม่จนกว่าจะได้ข้อมูลที่
# ต้องการ แล้วแสดงค่าทั้ง 3 ออกที่จอภาพ
# ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter number 1 (1-9): 20
# Enter number 1 (1-9): -5
# Enter number 1 (1-9): 6
# -----------------------
# Enter number 2 (1-9): 0
# Enter number 2 (1-9): 6
# 6 is the same as the first number.
# Enter number 2 (1-9): 15
# Enter number 2 (1-9): 9
# -----------------------
# Enter number 3 (1-9): 0
# Enter number 3 (1-9): 11
# Enter number 3 (1-9): 9
# 9 is the same as the second number.
# Enter number 3 (1-9): 6
# 6 is the same as the first number.
# Enter number 3 (1-9): 3
# -----------------------
# a = 6, b = 9 and c = 3

# # รับค่า a
# while True:
#     a = int(input("Enter number 1 (1-9): "))
#     if 1 <= a <= 9:
#         break
# print("-----------------------")

# # รับค่า b
# while True:
#     b = int(input("Enter number 2 (1-9): "))
#     if b == a:
#         print(f"{b} is the same as the first number.")
#     elif 1 <= b <= 9:
#         break
# print("-----------------------")

# # รับค่า c
# while True:
#     c = int(input("Enter number 3 (1-9): "))
#     if c == a:
#         print(f"{c} is the same as the first number.")
#     elif c == b:
#         print(f"{c} is the same as the second number.")
#     elif 1 <= c <= 9:
#         break
# print("-----------------------")
# print(f"a = {a}, b = {b} and c = {c}")


# =================================================================================

# extra จากคลิปที่ผ่านมานั้น (คลิป ปัญหาพิเศษ การใช้ลูป while) เมื่อได้เลขจ านวนเต็ม
# ทั้ง 3 ตัวแล้ว โดยที่แต่ละตัวไม่ซ้ ากันคือ ตัวแปร a = 6, b = 9 และ c = 3
# ให้เขียนโปรแกรมในการเปรียบเทียบ (โดยใช้ if, if else หรือ if elif) เพื่อหาค่า
# ที่น้อยที่สุดและค่าที่มากที่สุด แล้วแสดงเลขจ านวนเต็มตั้งแต่ค่าที่น้อยที่สุดไปจนถึง
# ค่าที่มากที่สุดออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# a = 6, b = 9 and c = 3
# min = 3
# max = 9
# Printing from 3 to 9: 3 4 5 6 7 8 9

# รับ a
while True:
    a = int(input("Enter number 1 (1-9): "))
    if 1 <= a <= 9:
        break
print("-----------------------")

# รับ b
while True:
    b = int(input("Enter number 2 (1-9): "))
    if b == a:
        print(f"{b} is the same as the first number.")
    elif 1 <= b <= 9:
        break
print("-----------------------")

# รับ c
while True:
    c = int(input("Enter number 3 (1-9): "))
    if c == a:
        print(f"{c} is the same as the first number.")
    elif c == b:
        print(f"{c} is the same as the second number.")
    elif 1 <= c <= 9:
        break
print("-----------------------")

print(f"a = {a}, b = {b} and c = {c}")

# หาค่าต่ำสุด
if a <= b and a <= c:
    min_val = a
elif b <= a and b <= c:
    min_val = b
else:
    min_val = c

# หาค่าสูงสุด
if a >= b and a >= c:
    max_val = a
elif b >= a and b >= c:
    max_val = b
else:
    max_val = c

print(f"min = {min_val}")
print(f"max = {max_val}")
print(f"Printing from {min_val} to {max_val}:", end=" ")
for i in range(min_val, max_val + 1):
    print(i, end=" ")

