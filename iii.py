from colorama import Fore
from tabulate import tabulate



cars = ['BMW', 'Tesla', 'Toyota', 'Mercedes',]
string = ', '.join(cars)




print(Fore.LIGHTGREEN_EX + string)
print(type(string))
print(cars.index('Mercedes'))
print(cars.index('BMW'))