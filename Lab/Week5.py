#แลปในสไลด์

# 5.1 เขียนโปรแกรมโดยก ำหนดให้ตัวแปรต่ำง ๆ ประกอบไปด้วย name เก็บชื่อ – สกุล
# age เก็บอำยุ weight เก็บน ำหนัก (เลขจ ำนวนจริง) และ sex เก็บเพศ (male หรือ
# female) แล้วแสดงผลของข้อมูลเหล่ำนั นออกที่จอภำพ ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Using variable to print out ...
# Somchai Jaidee
# Your age is 21
# Weight = 56.5
# Sex = Male

# name = 'Somchai Jaidee'
# age = 21
# weight = 56.5
# sex = 'Male'
# print('Using variable to print out ...')
# print(name)
# print('Your age is ',age)
# print('Weight = ',weight)
# print('Sex = ',sex)

# =================================================================================


# 5.2 เขียนโปรแกรมโดยก ำหนดให้ตัวแปรต่ำง ๆ ประกอบไปด้วย name เก็บชื่อ – สกุล
# age เก็บอำยุ weight เก็บน ำหนัก (เลขจ ำนวนจริง) และ sex เก็บเพศ (male หรือ
# female) แล้วแสดงผลของข้อมูลเหล่ำนั นออกที่จอภำพ โดยใช้ %d, %f และ %s
# ในกำรแสดงผลข้อมูลของตัวแปรต่ำง ๆ ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Using %d, %f and %s to print out ...
# Hi, Somchai Jaidee.
# You are 21 years old and your weight id 56.500.
# You are Male..

# name = 'Somchai Jaidee.'
# age = 21
# weight = 56.5
# sex = 'Male'
# print('Using %d, %f and %s to print out ...')
# print('Hi, %s'%name)
# print('You are %d years old and your weight id %.3f.'%(age,weight))
# print('You are %s'%sex)

# =================================================================================


# 5.3 เขียนโปรแกรมโดยก ำหนดให้ตัวแปรต่ำง ๆ ประกอบไปด้วย name เก็บชื่อ – สกุล
# age เก็บอำยุ weight เก็บน ำหนัก (เลขจ ำนวนจริง) และ sex เก็บเพศ (M หรือ F)
# แล้วแสดงผลของข้อมูลเหล่ำนั นออกที่จอภำพ โดยกำรจองพื นที่และใช้ %d, %f และ
# %s ในกำรแสดงผลข้อมูลของตัวแปรต่ำง ๆ ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Using space determination with %d, %f and %s to print out ...
# 1234567890123456789012345678901234567890
# NAME                AGE  WEIGHT      SEX
# Somchai Jaidee      21   56.5000      M

# name = 'Somchai Jaidee'
# age = 21
# weight = 56.5000
# sex = 'M'
# print('1234567890'*4)
# print('%0s%19s%8s%9s'%('NAME','AGE','WEIGHT','SEX'))
# print('%0s%8d%10.4f%7s'%(name,age,weight,sex))

# =================================================================================


# 5.4 เขียนโปรแกรมในกำรรับข้อมูลประกอบไปด้วย ชื่อ – สกุล เก็บไว้ที่ตัวแปร
# name อำยุ (จ ำนวนเต็ม) เก็บไว้ที่ตัวแปร age น ำหนัก (เลขจ ำนวนจริง) เก็บไว้
# ที่ตัวแปร weight และเพศ (male หรือ female) เก็บไว้ที่ตัวแปร sex เก็บ แล้ว
# แสดงผลของข้อมูลเหล่ำนั นออกที่จอภำพ โดยใช้ %d, %f และ %s ในกำร
# แสดงผลข้อมูลของตัวแปรต่ำง ๆ ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Name: Jack Smith
# Age: 25
# Weight: 72.8
# Sex: male
# Hi, Jack Smith.
# You are 25 years old and your weight is 72.800000.
# You are male.

# =================================================================================


# 5.5 เขียนโปรแกรมในกำรรับข้อมูลประกอบไปด้วย ชื่อ เก็บไว้ที่ตัวแปร name อำยุ เก็บไว้ที่ตัวแปร age
# น ำหนัก เก็บไว้ที่ตัวแปร weight และเก็บข้อมูลกำรจองพื นที่ในกำรแสดงผลของข้อมูลทั ง 3 โดยกำร
# จองพื นที่ส ำหรับแสดงแข้อมูลแต่ละข้อมูลนั นจะไม่เกิน 10 ช่อง ดังตัวอย่ำงกำรรันโปรแกรม
# ตัวอย่ำงกำรรันโปรแกรม
# Display data as your request
# Enter name: Sumate
# Enter age: 20
# Enter height: 178
# Your name: Sumate
# Your age: 20
# Your height: 178
# Requested space for name: -10
# Requested space for age: 5
# Requested space for height: 10
# 123456789012345678901234567890
# Sumate 20 178

print("Display data as your request")

name = input("Enter name: ")
age = input("Enter age: ")
height = input("Enter height: ")

print(f"Your name: {name}")
print(f"Your age: {age}")
print(f"Your height: {height}")

print("1234567890" * 3) 

print(f"{name:<10}{age:<10}{height:<10}")
