def calculate_electricity_cost(units):  
 
   if units >200:
    cost = 125.0 + 350.00 + ((units - 200) * 4.00) + 25
    print(cost)
    print("1-50 หน่วย: 125.00 บาท")
    print("51-100 หน่วย: 150.00 บาท")
    print("101-200 หน่วย: 300.00 บาท")
    print(f"201-{units} หน่วย : {(units - 200) * 4.00} บาท")
    print("ค่าบริการ : 25.00 บาท")
    print("รวมค่าไฟทั้งสิ้น : ",cost, "บาท")

   elif units >100:
    cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50) + 25
    print(cost)
    print("1-50 หน่วย: 125.00 บาท")
    print("51-100 หน่วย: 150.00 บาท")
    print(f"101-{units }หน่วย : {(units - 100) *3.50} บาท")
    print("ค่าบริการ : 25.00 บาท")
    print("รวมค่าไฟทั้งสิ้น : ",cost, "บาท")
 
   elif units > 50 :
    cost = 125.0 + ((units - 50) * 3.00) + 25
    print("1-50 หน่วย: 125.00 บาท")
    print(f"51-{units} หน่วย:  {(units - 50) * 3.00} บาท ")
    print("ค่าบริการ : 25.00 บาท")
    print("รวมค่าไฟทั้งสิ้น : ",cost, "บาท")

   elif units >= 0:
    cost = units * 2.50 + 25
    print(f"{units} หน่วย:{(units)*2.50} บาท")
    print("ค่าบริการ : 25.00 บาท")
    print("รวมค่าไฟทั้งสิ้น : ",cost, "บาท")

   else:
    print("จำนวนไฟหน่วยไฟฟ้าต้องไม่ติดลบ")

while(True):
  print("==== โปรแกรมคำนวณค่าไฟฟ้า ====")
  print("1.คำนวณค่าไฟ")
  print("2.ออกจากโปรแกรม")
  choice = input ("เลือกเมนู:")
  if choice == "1":
    units = int(input("กรอกค่าห่นวยไฟฟ้า :"))
    calculate_electricity_cost(units)
  elif choice == "2":
    break
  else:
    print("หากเลือกเมนูอื่น ให้แจ้งว่าเลือกเมนูไม่ถูกต้อง")  

