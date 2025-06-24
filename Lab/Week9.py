#แลปในสไลด์

# 9.1 เขียนโปรแกรมในการรับเลขจ านวนเต็ม 1 จ านวน แล้วตรวจสอบว่าเป็นเลขติด
# ลบหรือไม่ ถ้าเป็นเลขติดลบให้แสดงข้อความว่า “It is a negative number.”
# ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a number: -5 Enter a number: 30
# It is a negative number. End Program !!!
# End Program !!!

# number = int(input("Enter a number: "))
# if number < 0:
#     print("It is a negative number.")
# print("End Program !!!")


# =================================================================================


# 9.2 เขียนโปรแกรมในการรับเลขจ านวนเต็ม 1 จ านวน ถ้าเป็นเลขคู่ให้แสดงข้อความ
# ว่า “It is an even number.” ออกที่จอภาพ แต่ถ้าเป็นเลขคี่ให้แสดงข้อความ
# ว่า “It is an odd number.” แทน ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม ตัวอย่างการรันโปรแกรม
# Enter a number: 25 Enter a number: 30
# It is an odd number. It is an even number.
# End Program !!! End Program !!!

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("It is an even number.")
# else:
#     print("It is an odd number.")
# print("End Program !!!")


# =================================================================================


# 9.3 เขียนโปรแกรมในการรับเลขจ านวนเต็ม 1 จ านวนมีค่าตั้งแต่
# 100 ถึง 999 แล้วประมวลผลหาเลขที่มากที่สุดโดยใช้ if elif else
# แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter a number (100-999): 421
# The biggest number is 4.
# ตัวอย่างการรันโปรแกรม
# Enter a number (100-999): 374
# The biggest number is 7.
# ตัวอย่างการรันโปรแกรม
# Enter a number (100-999): 358
# The biggest number is 8.

# number = int(input("Enter a number (100-999): "))

# if 100 <= number <= 999:
#     hundreds = number // 100
#     tens = (number % 100) // 10
#     units = number % 10
    
#     if hundreds >= tens and hundreds >= units:
#         biggest = hundreds
#     elif tens >= hundreds and tens >= units:
#         biggest = tens
#     else:
#         biggest = units

#     print(f"The biggest number is {biggest}.")
# else:
#     print("Invalid input. Please enter a number between 100 and 999.")


# =================================================================================


# extra เขียนโปรแกรมควบคุมการขายบัตรส าหรับการเข้าชมฟุตบอล ซึ่งมีเงื่อนไขตามอายุของ
# ผู้เข้าชมคือ ผู้เข้าชมที่มีอายุตั้งแต่ 10 ปี แต่ไม่เกิน 80 ปี สามารถเข้าชมฟุตบอลได้
# มิฉะนั้นแล้วจะไม่อนุญาตให้เข้าชมฟุตบอล (No Permit !!!) ซึ่งราคาตั๋วเข้าชมฟุตบอล
# นั้น จะขึ้นอยู่กับอายุคือ
# 1. อายุน้อยกว่า 18 ปีหรืออายุตั้งแต่ 60 ปีขึ้นไปแต่ไม่เกิน 70 ปี จะได้ตั๋วเข้าชมฟรี
# 2. อายุตั้งแต่ 18 ปี และน้อยกว่า 45 ปี ราคาตั๋วใบละ 300 บาท
# 3. อายุตั้งแต่ 45 ปี และน้อยกว่า 60 ปี ราคาตั๋วใบละ 150 บาท
# 4. อายุ 70 ปีขึ้นไป ได้ตั๋วเข้าชมฟรีพร้อมเครื่องดื่ม


age = int(input("Enter your age: "))

if age < 10 or age > 80:
    print("No Permit !!!")
else:
    if age < 18 or (60 <= age < 70):
        print("Free ticket.")
    elif 18 <= age < 45:
        print("Ticket price: 300 baht.")
    elif 45 <= age < 60:
        print("Ticket price: 150 baht.")
    elif age >= 70:
        print("Free ticket with drink.")

