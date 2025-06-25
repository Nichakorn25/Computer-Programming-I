# 4.จงเขียนโปรแกรมในการสร้างตารางยูนิโค้ด เฉพาะช่วงข้อมูลที่มีค่าตั้งแต่ 97 ถึง 122 ซึ่ง
# แสดงเลขฐานหลักสิบ (Decimal) เลขฐานสิบหก (Hexadecimal) เลขฐานแปด(Octal) และ
# ตัวอักษร ดังตัวอย่างการรันโปรแกรม

# Dec   Hex   Oct   Chr 
#  97    61   141     a 
#  98    62   142     b


print("Dec   Hex   Oct   Chr")

for i in range(97, 123):
    decimal = i                  # ค่าเลขฐานสิบ
    hexa = format(i, 'x')        # แปลงเป็นเลขฐานสิบหก 
    octal = format(i, 'o')       # แปลงเป็นเลขฐานแปด
    character = chr(i)           # แปลงเป็นตัวอักษร
    
    print("{:>3}   {:>3}   {:>3}    {}".format(decimal, hexa, octal, character))

