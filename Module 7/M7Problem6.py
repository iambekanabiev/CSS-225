# Bekzodbek Nabiev
# 09/08/2024
# Problem 6: Car Class with Additional Attributes

class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.type} {self.model} {self.year} {self.color}"

# Example 
car1 = Car("Sports", 2012, "Blue", "Coupe", "Tesla")
car2 = Car("Sedan", 2020, "Black", "Luxury", "BMW")

print(car1.get_color())
print(car1.get_model())
print(car1.get_type())
print(car1.get_manufacturer())
print(car1.fullspecs())

print(car2.get_color())
print(car2.get_model())
print(car2.get_type())
print(car2.get_manufacturer())
print(car2.fullspecs())
