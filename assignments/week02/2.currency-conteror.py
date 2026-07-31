"""
Write a program
Question that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

rate = 35.5

print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose (1 or 2): ")

amount = float(input("Enter amount: "))

if choice == "1":
    result = amount / rate
    print(f"Formula: {amount} / {rate}")
    print(f"{amount:.2f} THB = {result:.2f} USD")
elif choice == "2":
    result = amount * rate
    print(f"Formula: {amount} * {rate}")
    print(f"{amount:.2f} USD = {result:.2f} THB")
else:
    print("Invalid choice")
