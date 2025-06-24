# 3.จงเขียนโปรแกรมเพื่อแสดงค่าแอสกีของตัวอักษร A,K,T,Z,a,m,z 
# หลังจากนั้นให้แสดงตัวอักษรที่มีค่าแอสกี 72, 88 และ 118 ออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# The ASCII value of 'A' is 65
# The ASCII value of 'K' is 75
# The ASCII value of 'T' is 84
# The ASCII value of 'Z' is 90
# The ASCII value of 'a' is 97
# The ASCII value of 'm' is 109
# The ASCII value of 'z' is 122
# 72 is the ASCII value of character H
# 88 is the ASCII value of character X
# 118 is the ASCII value of character v

# character = ["A","K","T","Z","a","m","z"]
# number = [72,88,118]

# for c in character:
#     print("The ASCII value of %s is %d"%(c,ord(c)))
# for n in number:
#     print("%d is the ASCII value of character %s"%(n,chr(n)))

# =================================================================================

print("The ASCII value of 'A' is %d"%ord("A"))
print("The ASCII value of 'K' is %d"%ord("K"))
print("The ASCII value of 'T' is %d"%ord("T"))
print("The ASCII value of 'Z' is %d"%ord("Z"))
print("The ASCII value of 'a' is %d"%ord("a"))
print("The ASCII value of 'm' is %d"%ord("m"))
print("The ASCII value of 'z' is %d"%ord("z"))
print("72 is the ASCII value of character %s"%chr(72))
print("88 is the ASCII value of character %s"%chr(88))
print("118 is the ASCII value of character %s"%chr(118))