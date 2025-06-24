#แลปในสไลด์

# 8.1 เขียนโปรแกรมในการรับเลขจ านวนเต็ม 1 จ านวนมีค่าตั้งแต่
# 100 ถึง 999 แล้วท าการแยกหลักพร้อมกับหาผลบวกของหลักต่าง ๆ
# แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter a number 100-999: 123
# 123 is separated to 1, 2 and 3.
# Sum of 1, 2 and 3 is 6.

# number = int(input("Enter a number 100-999: "))

# if 100 <= number <= 999:
#     hundreds = number // 100
#     tens = (number % 100) // 10
#     units = number % 10

#     total = hundreds + tens + units

#     print(f"{number} is separated to {hundreds}, {tens} and {units}.")
#     print(f"Sum of {hundreds}, {tens} and {units} is {total}.")
# else:
#     print("Invalid input. Please enter a number between 100 and 999.")

# =================================================================================


# 8.2 เขียนโปรแกรมในการรับเลขจ านวนเต็ม 3 จ านวนเก็บไว้ที่ตัวแปร a, b และ c
# แล้วแสดงผลในการเปรียบเทียบค่าของตัวแปรทั้ง 3 ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# a = 5
# b = 4
# c = 9
# a = 5, b = 4 and c = 9
# 5>4 ==> True
# 9 is an odd number ==> True
# 5>4 and 5 is an even number ==> False

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# print(f"a = {a}, b = {b} and c = {c}")

# print(f"{a}>{b} ==> {a > b}")

# print(f"{c} is an odd number ==> {c % 2 == 1}")

# print(f"{a}>{b} and {a} is an even number ==> {a > b and a % 2 == 0}")


# =================================================================================


# 8.3 เขียนโปรแกรมในการรับสตริง 1 จ านวน ซึ่งจะสตริงที่ประกอบไปด้วยตัวอักษรจาก a – z เก็บไว่ที่ตัวแปร str
# หลังจากนั้นให้ท าการตรวจสอบดูว่าสตริงที่รับเข้ามานั้นมีสระ ซึ่งก็คือ a, e, i, o, หรือ u หรือไม่ ดังตัวอย่างการ
# รันโปรแกรม
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a string: ant Enter a string: red
# "ant" contains vowel ==> True "red" contains vowel ==> True
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a string: ink Enter a string: boy
# "ink" contains vowel ==> True "boy" contains vowel ==> True
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a string: study Enter a string: bcdxyz
# "study" contains vowel ==> True "bcdxyz" contains vowel ==> False

str_input = input("Enter a string: ")
vowels = "aeiou"
contains_vowel = any(char in vowels for char in str_input)
print(f'"{str_input}" contains vowel ==> {contains_vowel}')
