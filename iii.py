from colorama import Fore
from tabulate import tabulate



cars = ['BMW', 'Tesla', 'Toyota', 'Mercedes',]
cars_copy = cars.copy()
cars_copy_2 = list(cars)
cars_copy_3 = cars[:]

print(tabulate(cars, headers=['1', '2', '3', '4', '5', '6', '7', '8', '9'], tablefmt='grid' ))
print(cars_copy_2)
print( cars_copy_3)
print(len( cars))






