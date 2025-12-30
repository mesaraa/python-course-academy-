# Create a class Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car details
    def car_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("--------------------")

# Create first object
car1 = Car("Toyota", "Corolla", 2020)
car1.car_info()

# Create second object
car2 = Car("Honda", "City", 2022)
car2.car_info()
