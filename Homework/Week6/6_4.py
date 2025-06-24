# 4.จงเขียนโปรแกรมเพื่อกำหนดตัวแปร mail = "k.chan@hotmail.com"แล้วประมวลผลเพื่ิอ
# 1)แสดงข้อมูลของตัวแปร mail
# 2)แสดงความยาวของข้อมูลในตัวแปร mail
# 3)ให้เปลี่ยนข้อความจาก "k."ที่อยู่ในตัวแปร mail เป็น "kacha-"
# 4)ให้เปลี่ยนข้อความจาก "hotmail" ที่อยู่ในตัวแปร mail เป็น "gmail"
# 5)แสดงข้อมูลของตัวแปร mail
# 6)แสดงความยาวของข้อมูลในตัวแปร mail

# The variable mail contains "k.chan@hotmail.com".
# The length of mail is 18.
# mail contains "kacha-chan@gmail.com".
# The length of mail is 20.

mail = "k.chan@hotmail.com"
print("The variable mail contains \"%s\"."%mail)
print("The length of mail is %d."%(len(mail)))
mail = mail.replace("k","kacha")
mail = mail.replace("hotmail","gmail")
print("mail contains \"%s\"."%mail)
print("The length of mail is %d."%(len(mail)))