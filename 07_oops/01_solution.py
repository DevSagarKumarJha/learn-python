class Car:
  total_car = 0
  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model
    Car.total_car += 1

  def full_name(self):
    return f"{self.__brand} {self.__model}"

  def get_brand(self):
    return self.__brand
  
  @property
  def model(self):
    return self.__model

  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod
  def general_description():
    return "Cars are means of transport"


class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    self.battery_size = battery_size
    super().__init__(brand, model)
  def fuel_type(self):
    return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S","85KWH")
# # print(my_tesla.get_brand())
# # print(my_tesla.fuel_type())

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# my_car =Car("Tata","Safari")
# Car("Tata","Nexon")
# # print(my_car.general_description())

# print(my_car.model)
# print(Car.general_description())


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


class Battery:
  def battery_info(self):
    return "This is Battery " 

class Engine:
  def engine_info(self):
    return "This is Engine "

class ElecticCarTwo(Battery, Engine, Car):
  pass

my_new_tesla = ElecticCarTwo("Tesla", "Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())