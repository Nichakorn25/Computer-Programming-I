# 1.จงเขียนโปรแกรมเพื่อใช้ลูป while แสดงเลขจำนวนเต็มจาก 1-30 ถ้าเป็นเลขหลักเดียว (1-9)
# ให้แสดงเลข 0 นำหน้า โดยแสดงออกบรรทัดละ 10 จำนวน ดังตัวอย่างการรันโปรแกรม

# Using while loop to print 1-30 !!!
# 01 02 03 04 05 06 07 08 09 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30


print("Using while loop to print 1-30 !!!")

i = 1 
count = 0 

while i <= 30:
    if i < 10:
        print(f"0{i}", end=' ')
    else:
        print(i, end=' ')
    
    count += 1
    if count % 10 == 0:
        print() 

    i += 1
