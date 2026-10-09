#first script
import os


print("current dir", os.getcwd())
data_path = "data/sales.csv" 

if(os.path.exists(data_path)):
    print("Sales data file exists.")
else:
    print("Sales data file does not exist.") 



import pandas as pd
import json
import os

df = pd.read_csv("data/sales.csv")

print("CSV data")
print(df)
print(f"\n shape {df.shape[0]} rows, {df.shape[1]} columns")

df["total"] = df["quantity"] * df["price"]
print("\n with totals:")
print(df)

#create output directory
os.makedirs("output", exist_ok=True)

#1.save to CSV
df.to_csv("output/sales_data.csv", index=False)

#2. Save to excel
df.to_excel("output/sales_data.xlsx", index=False)
#3. Save to JSON
df.to_json("output/sales_data.json", orient="records", indent=2)

#working with custome modules
from helpers import calculate_total, format_currency
import pandas as pd

df = pd.read_csv("data/sales.csv")

totals = []
for index, row in df.iterrows():
    total = calculate_total(row["quantity"], row["price"])
    totals.append(total)

df["total"] = totals
print("\n with totals using custom module:")
print(df)

#error handling
try:
    with open("data/sales.csv", "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)
    number = int(content)
    result = 100/number

except FileNotFoundError as e:
    print(f"An error occurred: {e}")
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
except NameError as e:
    print(f"An error occurred: {e}")
finally:
    if 'content' in locals():
        print("File content was read successfully.")
    print("Error handling complete.")

#oop concept
class Car:
    __total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.__total_car += 1

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    @property
    def model(self):
        return self.__model
    
    def get_battery_size(self):
        return self.batterySize
    
    def display_info(self):
        print(f"Car brand: {self.__brand}, Model: {self.__model}")

    def fuel_type(self):
        print("Petrol or diesel")

    @staticmethod
    def get_total_car():
        return Car.__total_car


class ElectriCar(Car):
    def __init__(self,brand,model, batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize

    def fuel_type(self):
        print("Electric")
#example usage

my_tesla = ElectriCar("Tesla", "Model S", "100kWh")
my_tesla.engine = "Electric"
print(f"My Tesla engine type: {my_tesla.engine}")
my_tesla.display_info()
my_tesla.get_battery_size()
my_tesla.fuel_type()

print(isinstance(my_tesla, ElectriCar))
print(isinstance(my_tesla, Car))    
# print(isinstance(my_car, ElectriCar))
# print(isinstance(my_car, Car))
# print(f"My car model: {my_car.model}")

print(f"My Tesla model: {my_tesla.model}")



my_car = Car("Toyota", "Corolla")
print(my_car.get_model())
print(f"Total cars created: {my_car.get_total_car()}")

my_car.display_info()
