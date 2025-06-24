# 3.จงเขียนโปรแกรมในการรับข้อมูลเลขจำนวนเต็มสี่หลัก 1 จำนวน(1000-9999)แล้ว
# แสดงผลออกทางจอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter a number (1000-9999): 4927
# You entered number 4927.
# Number 4927 is seperated to be 4, 9, 2 and 7.
# The smallest number is 2.

# Enter a number (1000-9999): 6896
# You entered number 6896.
# Number 4927 is seperated to be 6, 8, 9 and 6.
# The smallest number is 6.

number = int(input("Enter a number (1000-9999): "))

if 1000 <= number <= 9999:
    print(f"You entered number {number}.")
    digits = [int(d) for d in str(number)]
    print(f"Number {number} is seperated to be {digits[0]}, {digits[1]}, {digits[2]} and {digits[3]}.")

    smallest = min(digits)
    print(f"The smallest number is {smallest}.")
else:
    print("Invalid input. Please enter a number between 1000 and 9999.")


