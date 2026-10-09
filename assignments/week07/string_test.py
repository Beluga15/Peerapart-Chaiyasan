#ข้อที่ 1
import string

letters = string.ascii_uppercase  

for i in range(1, 7):  
    print(letters[:i])


#ข้อที่ 4
def reverse_string(text):
    return text[::-1]

word = input("กรอกข้อความที่ต้องการกลับด้าน: ")
print("ข้อความกลับด้าน:", reverse_string(word))