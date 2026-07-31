
def calculate_tax(income):
   tax1 = 0
   tax2 = 0
   tax3 = 0
   tax4 = 0
   tax5 = 0
   tax6 = 0
   tax7 = 0
   tax8 = 0
   
   if income > 0:
       if income > 150000:
           tax1 = 150000 * 0
       else:
           tax1 = income * 0
   
   if income > 150000:
       if income > 300000:
           tax2 = (300000 - 150000) * 0.05
       else:
           tax2 = (income - 150000) * 0.05
   
   if income > 300000:
       if income > 500000:
           tax3 = (500000 - 300000) * 0.10
       else:
           tax3 = (income - 300000) * 0.10
   
   if income > 500000:
       if income > 750000:
           tax4 = (750000 - 500000) * 0.15
       else:
           tax4 = (income - 500000) * 0.15
   
   if income > 750000:
       if income > 1000000:
           tax5 = (1000000 - 750000) * 0.20
       else:
           tax5 = (income - 750000) * 0.20
   
   if income > 1000000:
       if income > 2000000:
           tax6 = (2000000 - 1000000) * 0.25
       else:
           tax6 = (income - 10000000) * 0.30
   
   if income > 2000000:
       if income > 5000000:
           tax7 = (5000000 - 2000000) * 0.30
       else:
           tax7 = (income - 2000000) * 0.30
 
   if income > 5000000:
       tax8 = (income - 5000000) * 0.35
   total_tax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6 + tax7 + tax8
   return tax1, tax2, tax3, tax4, tax5, tax6, tax7, tax8, total_tax


income = float(input("กรอกเงินได้สุทธิ : "))
tax1, tax2, tax3, tax4, tax5, tax6, tax7, tax8, total_tax = calculate_tax(income)
print("----------------------------------------")
print("รายละเอียดภาษี")
print("----------------------------------------")
if income > 0:
   print("0 - 150,000        ", round(tax1), "บาท")
if income > 150000:
   print("150,001 - 300,000   ", round(tax2), "บาท")
if income > 300000:
   print("300,001 - 500,000   ", round(tax3), "บาท")
if income > 500000:
   print("500,001 - 750,000   ", round(tax4), "บาท")
if income > 750000:
   print("750,001 - 1,000,000 ", round(tax5), "บาท")
if income > 1000000:
   print("1,000,001 - 2,000,000", round(tax6), "บาท")
if income > 2000000:
   print("2,000,001 - 5,000,000", round(tax7), "บาท")
if income > 5000000:
   print("มากกว่า 5,000,000    ", round(tax8), "บาท")
net_income = income - total_tax
effective_rate = (total_tax / income) * 100
print()
print("ภาษีรวม            ", round(total_tax), "บาท")
print("รายได้หลังหักภาษี  ", round(net_income), "บาท")
print("Effective Tax Rate =", round(effective_rate, 2), "%")