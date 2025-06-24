# 4.จงเขียนโปรแกรมในการคำนวณค่าอาหารของร้านอาหารบุฟเฟต์แห่งหนึ่งเพื่อคืนกำไรให้ลูกค้า 
# โดยรับข้อมูลเพื่อกำหนดโปรโมชันคือ จำนวนลูกค้าที่มาและจำนวนลูกค้าที่คิดค่าหัวที่จะต้องจ่าย เช่น "มา 4 จ่าย 3"หรือ"มา 3 จ่าย 2" เป็นต้น
# หลังจากนั้นรับข้อมูลจำนวนลูกค้าที่จะเข้ามาและราคาต่อหัวแล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Setup Promotion --- How many COME: 4
# Setup Promotion --- How many PAY: 3
# How many customer?: 5
# How much per head?: 200
# Total payment for 5 customers is 800 baht.
    
# Setup Promotion --- How many COME: 3
# Setup Promotion --- How many PAY: 2
# How many customer?: 6
# How much per head?: 200
# Total payment for 6 customers is 2,000 baht.

come = int(input("Setup Promotion --- How many COME: "))
pay = int(input("Setup Promotion --- How many PAY: "))


customer = int(input("How many customer?: "))
price_per_head = int(input("How much per head?: "))

group = customer // come           
remainder = customer % come        
total_pay = (group * pay + remainder) * price_per_head

print(f"Total payment for {customer} customers is {total_pay:,} baht.")
