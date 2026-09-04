#1.รับค่า text จากผู้ใช้
#2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
#3.แสดงผลจำนวนของอักขระในข้อความ text

# ตัวอย่างหน้าจอ
# Insert your text : Boonchoo Jitnupong
# Character to find:o
# 5 letters 'o' found in 'Booncho Jitnupong'

"""
print("\n=== ITERATING THROUGH STRING ===")
float = input("Insert your text :")
count = 0
for letter in float:
    if letter == 'o':
        count += 1
print(f"{count} letters 'o' found in '{float}'")
"""


password= input("Insert your password:")

lenght = len(password)
words = password.split('@')

if len(words) >1:
   left = words[0].isalnum()
   right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password ia strong")
else:
    print("Your password is not strong!")

