# 4.จงเขียนโปรแกรมรับข้อมูลอายุ แล้วเปรียบเทียบหา Generation โดยกำหนด Generation ต่างๆ
# ในสังคมไทยตามช่วงอายุดังต่อไปนี้
# 1.The Giver (Silent Gen) อายุ 77-94 ปี
# 2.The Loyalist (Baby Boomer) อายุ 58-76 ปี
# 3.The Life Maker (Gen X) อายุ 42-57 ปี
# 4.The New Driver (Gen Y) อายุ 26-41 ปี
# 5.The Digital Native (Gen Z) อายุ 12-25 ปี
# 6.The AI Kids (Gen Alpha) อายุน้อยกว่า 12 ปี
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Check your generation here !!!
# Enter your age: 61
# You are 61 years old.
# You generation is "The Loyalist (Baby Boomer)" .

# Check your generation here !!!
# Enter your age: 19
# You are 19 years old.
# You generation is "The Digital Native (Gen Z)" .

print("Check your generation here !!!")
age = int(input("Enter your age: "))

print(f"You are {age} years old.")

if 77 <= age <= 94:
    print('You generation is "The Giver (Silent Gen)".')
elif 58 <= age <= 76:
    print('You generation is "The Loyalist (Baby Boomer)".')
elif 42 <= age <= 57:
    print('You generation is "The Life Maker (Gen X)".')
elif 26 <= age <= 41:
    print('You generation is "The New Driver (Gen Y)".')
elif 12 <= age <= 25:
    print('You generation is "The Digital Native (Gen Z)".')
elif age < 12:
    print('You generation is "The AI Kids (Gen Alpha)".')
else:
    print("Your age is out of the defined generation range.")
