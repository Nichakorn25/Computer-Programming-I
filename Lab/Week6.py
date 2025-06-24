#แลปในสไลด์

# 6.1 เขียนโปรแกรมเพื่อรับเลขจ ำนวนเต็มเก็บไว้ที่ตัวแปร n แล้วแสดงออกเป็น
# เลขฐำนสอง ฐำนแปด และ ฐำนสิบหก ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Enter a number: 21
# Type of n = <class 'int'>
# Decimal number 21 = Binary number 0b10101
# Decimal number 21 = Octal number 0o25
# Decimal number 21 = Hexadecimal number 0x15

# n = int(input("Enter a number: "))

# print(f"Type of n = {type(n)}")
# print(f"Decimal number {n} = Binary number {bin(n)}")
# print(f"Decimal number {n} = Octal number {oct(n)}")
# print(f"Decimal number {n} = Hexadecimal number {hex(n)}")


# =================================================================================


# 6.2 เขียนโปรแกรมเพื่อรับสตริงเก็บไว้ที่ตัวแปร s แล้วแสดงออกที่จอภำพ
# ในรูปแบบต่ำง ๆ โดยกำรระบุล ำดับที่ ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Enter a string: Suranaree
# You entered "Suranaree"
# There are 9 characters.
# The first character is 'S'.
# The last character is 'e'.
# The first five-character is 'Suran'.
# "Suranaree" is reversed to "eeranaruS".

# s = input("Enter a string: ")

# print(f'You entered "{s}"')
# print(f"There are {len(s)} characters.")
# print(f"The first character is '{s[0]}'.")
# print(f"The last character is '{s[-1]}'.")
# print(f"The first five-character is '{s[:5]}'.")
# print(f'"{s}" is reversed to "{s[::-1]}".')


# =================================================================================


# 6.3 เขียนโปรแกรมเพื่อรับสตริงเก็บไว้ที่ตัวแปร s แล้วแสดงกำรใช้เมธอดต่ำง ๆ เพื่อแสดงผล
# ให้ได้ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Enter a string: you are smart
# You entered a string "you are smart".
# Capital only first character of each word ==> You Are Smart
# All Uppercase ==> YOU ARE SMART
# All Lowercase ==> you are smart
# Replace a space with "---" ==> you---are---smart

# s = input("Enter a string: ")

# print(f'You entered a string "{s}".')
# print("Capital only first character of each word ==> " + s.title())
# print("All Uppercase ==> " + s.upper())
# print("All Lowercase ==> " + s.lower())
# print("Replace a space with \"---\" ==> " + s.replace(" ", "---"))


# =================================================================================


# 6.4 เขียนโปรแกรมเพื่อรับสตริง รับอินเด็กซ์ จุดเริ่มต้น จุดสิ้นสุด ล ำดับขั้น
# ในกำรเลื่อน แล้วแสดงผลออกที่จอภำพดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Enter a string: 12345678901234567890
# Display data at index: -3
# Data at index -3 is '8'
# Start display data at index: -2
# Stop display data at index: -16
# Step to move: -3
# Data from index -2 to -16 is '96307'

s = input("Enter a string: ")

index = int(input("Display data at index: "))
print(f"Data at index {index} is '{s[index]}'")

start = int(input("Start display data at index: "))
stop = int(input("Stop display data at index: "))
step = int(input("Step to move: "))

sliced = s[start:stop:step]
print(f"Data from index {start} to {stop} is '{sliced}'")
