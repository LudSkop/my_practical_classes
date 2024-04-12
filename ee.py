
from colorama import Fore


delete_useless =['Hello Alisa', 1980, 378, 'mersedes', 'Pusha', 'return', 'Oleg', 'coon', ]

char_element = []
symbol_element = []
for element in delete_useless:
    if isinstance(element, str):
        char_element.append(element)
    else:
        symbol_element.append(element)    
        

print(Fore.LIGHTRED_EX + f'char : {char_element}, symbol : {symbol_element}')








