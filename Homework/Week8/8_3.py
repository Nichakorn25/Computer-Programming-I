# 3.จงเขียนโปรแกรมการรับสตริงที่เป็นเลขฐานสอง 12 บิต 1 จำนวน ทำการประมวลผลค่าที่รับเข้ามให้เป็นเลขฐานสิบหก 
# แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# (Note:ใช้ฟังก์ชัน hex() ช่วยในการแปลงเลขฐาน 10 เป็นฐาน 16 เช่น hex(14) ผลที่ได้คือ 0xe)

# Conver 12-bit binary to hexadecimal...
# Enter a 12-bit binary number: 111110101001
# 111110101001 = 1111 1010 1001
# 1111 = 1*(2**3)+1*(2**2)+1*(2**1)+1*(2**0) = 15 = 0xf
# 1010 = 1*(2**3)+0*(2**2)+1*(2**1)+0*(2**0) = 10 = 0xa
# 1001 = 1*(2**3)+0*(2**2)+0*(2**1)+1*(2**0) = 9 = 0x9
# 111110101001 = fa9

print("Convert 12-bit binary to hexadecimal...")
binary = input("Enter a 12-bit binary number: ")

if len(binary) != 12 or not set(binary).issubset({'0', '1'}):
    print("Invalid input! Please enter exactly 12 binary digits (0 or 1).")
else:
    group1 = binary[0:4]
    group2 = binary[4:8]
    group3 = binary[8:12]

    print(f"{binary} = {group1} {group2} {group3}")

    hex_string = ""
    for group in [group1, group2, group3]:
        decimal = int(group, 2)
        binary_expression = " + ".join(
            [f"{int(bit)}*(2**{3 - i})" for i, bit in enumerate(group)]
        )
        print(f"{group} = {binary_expression} = {decimal} = {hex(decimal)}")
        hex_string += hex(decimal)[2:] 

    print(f"{binary} = {hex_string}")
