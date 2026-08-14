
def convert_currebcy(value, currency):
   if currency == "USD":
       print(f"{value} THB = {value / 33.0} USD")
   else:
       print(f"{value} USD = {value * 33.0} THB")

print("Temperature Converter:")
print(convert_currebcy(100, "USD"))
print(convert_currebcy(100, "THB"))
print()

