# 1.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 2 ตัว แล้วทำการตรวจสอบว่าเลขคู่(Even number)หรือเลขคี่(Odd number)
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# A:4
# B:9
# A is equal to 4 and it is an even number.
# B is equal to 9 and it is an odd number.

# A:31
# B:80
# A is equal to 31 and it is an odd number.
# B is equal to 80 and it is an even number.

number1 = int(input("A:"))
number2 = int(input("B:"))

if (number1%2==0):
    print("A is equal to %d and it is an even number.")
else:
    print("A is equal to %d and it is an odd number.")

if (number2%2==0):
    print("B is equal to %d and it is an even number.")
else:
    print("B is equal to %d and it is an odd number.")