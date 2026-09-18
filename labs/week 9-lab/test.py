try:
    num1  = int(input("ตัวเลขที่ 1:"))
    num2  = int(input("ตัวเลขที่ 2:"))

    op = input("เครื่องหมาย(+,-,*,/):")

    result = 0
    if op == "+":
       result = num1 + num2 
    elif op == "-":
       result = num1 - num2
    elif op == "*":
       result = num1 * num2
    elif op == "/":
       result = num1 / num2
    else:
       raise ValueEorror("เครื่องหมายต้องเป็น + - * / เท่านั้น")

    print(f"{num1} {op} {num2} = {result}")

except ValueEorror:
    print("กรุณากรอกข้อมูลที่เป็นตัวเลขเท่านั้น")

except ZeroDivisonEorror:
    print("ไม่สามารถหารด้วยศูนย์ได้")

except Exception:
   print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจว่าคืออะไร")

else:
    print("คำนวณข้อมูลเรียบร้อยแล้ว")

finally:
   print("จบการทำงาน")