#WAP to create a package with name cars and add different modules (such as BMW, AUDI, NISSAN) having classes and functionality and import them in main file cars.
from cars.bmw import BMW
from cars.audi import Audi
from cars.nissan import Nissan

bmw_car = BMW(model="X5")
bmw_car.start_engine()
bmw_car.drive()
print()
audi_car = Audi(model="A4")
audi_car.start_engine()
audi_car.drive()
print()
nissan_car = Nissan(model="Altima")
nissan_car.start_engine()
nissan_car.drive()