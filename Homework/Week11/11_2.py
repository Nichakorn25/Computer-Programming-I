# 2.จงเขียนโปรแกรมเพื่อใช้ลูป while แสดงตัวอักษร z ถึง a โดยแสดงบรรทัดละ 7 ตัวอักษร
# แต่ละตัวอักษรให้แสดงเครื่องหมาย --- ยกเว้นตัวสุดท้ายของบรรทัด แล้วแสดงจำนวนของตัวอักษรทั้งหมด
# ที่ถูกแสดงออก ดังตัวอย่างการรันโปรแกรม

# Using while loop to print z to a (7 characters per line)
# z---y---x---w---v---u---t
# s---r---q---p---o---n---m
# l---k---j---i---h---g---f
# e---d---c---b---a 

# Total = 26


ch = 122 
count = 0
while ch >= 97:
    line_count = 0
    while line_count < 7 and ch >= 97:
        print(chr(ch), end='')
        count += 1
        line_count += 1
        ch -= 1
        if line_count < 7 and ch >= 97:
            print('---', end='')
    print() 

print("\nTotal =", count)
