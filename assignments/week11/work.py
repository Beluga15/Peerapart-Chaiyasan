#6830252270 พีรภาส ไชยสาร

# ข้อ 1 - Vahicle
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

test = Vehicle(250, 70000)

print(test.max_speed)
print(test.mileage)


#ข้อ 2 - Circle Area
class circle:
    def calculate_circle_area(self, r):
        area = 3.14 * r * r
        return area

test1 = circle()
print(test1.calculate_circle_area(10))

#ข้อ 3 - Circle Area & Perimeter
class circle:
    def calculate_circle_area(self, r):
        area = 3.14 * r * r
        return area

    def calculate_circle_perimeter(self, r):
        perimeter = 2 * 3.14 * r
        return perimeter

test1 = circle()

r = float(input("Enter radius: "))

print("Area:", test1.calculate_circle_area(r))
print("Perimeter:", test1.calculate_circle_perimeter(r))

#ข้อ 4 - Calculator
class calculator:
    def add(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

test = calculator()

print(test.add(10, 5))
print(test.subtraction(10, 5))
print(test.multiplication(10, 5))