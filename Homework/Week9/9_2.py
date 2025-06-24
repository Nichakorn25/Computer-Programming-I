# 2.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 2 หลัก จำนวน 2 ตัว แล้วทำการตรวจสอบว่าเลขเหล่านั้นเป็นเลขเบิ้ล
# (11,22,33,44,55,66,77,88,99)หรือไม่ แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# A:38
# B:77
# A is equal to 38 and it is not a double-number.
# B is equal to 77 and it is a double-number of 7.

# A:22
# B:99
# A is equal to 22 and it is a double-number of 2.
# B is equal to 99 and it is a double-number of 9.

str1 = str(input("A:"))
str2 = str(input("B:"))

if len(str1) == 2 and str1[0] == str1[1]:
    print("A is equal to %s and it is a double-number of %s." %(str1, str1[0]))
else:
    print("A is equal to %s and it is not a double-number." %str1)

if len(str2) == 2 and str2[0] == str2[1]:
    print("B is equal to %s and it is a double-number of %s." %(str2, str2[0]))
else:
    print("B is equal to %s and it is not a double-number." %str2)