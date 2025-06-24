#แลปในสไลด์

# 11.1 เขียนโปรแกรมโดยใช้ลูปในการพิมพ์เลขจ านวนเต็มจาก 1 ถึง 50 ออกที่จอภาพ
# โดยพิมพ์เฉพาะเลขที่หารด้วย 3 ลงตัวและผลบวกของเลขที่พิมพ์ออกรวมกัน
# จะต้องไม่เกิน 50 ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Using "break" ...
# 3 6 9 12 15
# Sum of all numbers is 45.
# End Program !!!

# print('Using "break" ...')

# total = 0 
# i = 1    

# while i <= 50:
#     if i % 3 == 0:
#         if total + i > 50:
#             break
#         print(i, end=" ")
#         total += i
#     i += 1

# print(f"\nSum of all numbers is {total}.")
# print("End Program !!!")


# =================================================================================


# 11.2 เขียนโปรแกรมโดยใช้ลูป while ในการวนรับข้อมูลที่เป็นเลขจ านวนเต็ม 6 จ านวน
# แล้วแสดงผลบวกของเลขที่ไม่ติดลบออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Using while loop to add only positive number from 6 input...
# Number 1: 3
# Number 2: -5
# Number 3: -2
# Number 4: 7
# Number 5: -20
# Number 6: 6
# Sum of all positive numbers is 16.

# print("Using while loop to add only positive number from 6 input...")

# count = 1
# total = 0

# while count <= 6:
#     num = int(input(f"Number {count}: "))
#     if num >= 0:
#         total += num
#     count += 1

# print(f"Sum of all positive numbers is {total}.")


# =================================================================================


# 11.3 เขียนโปรแกรมโดยใช้ลูป for ในการพิมพ์เลขจ านวนเต็มจาก 1 ถึง 9 ออกที่จอภาพ ถ้าเลข
# นั้นมีค่ามากกว่า 5 และเป็นเลขคี่ให้ใช้ค าสั่ง pass ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Printing 1 to 9 using for loop ...
# Using "pass", if the number is odd and greater than 5
# 1 2 3 4 5 6 8
# End Program !!!

# print("Printing 1 to 9 using for loop ...")
# print('Using "pass", if the number is odd and greater than 5')

# for i in range(1, 10):
#     if i > 5 and i % 2 == 1:
#         pass  
#     else:
#         print(i, end=" ")
# print("\nEnd Program !!!")


# =================================================================================


# 11.4 เขียนโปรแกรมเพื่อรับสตริง 1 สตริงเก็บไว้ที่ตัวแปร st หลังจากนั้นให้ใช้ลูป for ในการพิมพ์ข้อมูลที่อยู่ใน
# ตัวแปร st ออกที่จอภาพโดยพิมพ์เฉพาะตัวอักษรที่เป็นสระเท่านั้นพร้อมกับแสดงค่า ascii ของตัวอักษรนั้น
# เมื่อหลุดออกจากลูป for ให้แสดงผลรวมของค่า ascii ของตัวอักษรทั้งหมดที่ถูกแสดงออก
# ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a string: Korat Eagle Enter a string: Under Water
# Output ...                  Output ...
# o ==> 111                   U ==> 85
# a ==> 97                    e ==> 101
# E ==> 69                    a ==> 97
# a ==> 97                    e ==> 101
# e ==> 101                   Sum of all ascii values = 384
# Sum of all ascii values = 475

# st = input("Enter a string: ")
# print("Output ...")
# vowels = "aeiouAEIOU"
# total_ascii = 0

# for ch in st:
#     if ch in vowels:
#         ascii_value = ord(ch)
#         print(f"{ch} ==> {ascii_value}")
#         total_ascii += ascii_value
# print(f"Sum of all ascii values = {total_ascii}")


# =================================================================================


# 11.5 เขียนโปรแกรมในการวนลูปเพื่อรับเงินบริจาค ซึ่ง
# จะหยุดรับเงินบริจาคเมื่อยอดรวมเกิน 1000 บาท
# ในการรับเงินบริจาคแต่ละครั้งจะต้องไม่น้อยกว่า
# 1 บาทหรือไม่เกิน 1000 บาท โดยโปรแกรมจะ
# แสดงยอดรวมให้เห็นทุกครั้งที่มีการบริจาค และ
# เมื่อหยุดรับเงินบริจาคแล้วก็จะแสดงยอดจ านวน
# คนที่บริจาค ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Donation amount (1-1000): -20
# Invalid Amount!
# Donation amount (1-1000): 2000
# Invalid Amount!
# Donation amount (1-1000): 300
# Total donation = 300
# Donation amount (1-1000): 500
# Total donation = 800
# Donation amount (1-1000): 500
# Total donation = 1300
# There are 3 donators.

total_donation = 0
donator_count = 0

while total_donation <= 1000:
    amount = int(input("Donation amount (1-1000): "))
    
    if amount < 1 or amount > 1000:
        print("Invalid Amount!")
        continue
    
    total_donation += amount
    donator_count += 1
    print(f"Total donation = {total_donation}")

print(f"There are {donator_count} donators.")

