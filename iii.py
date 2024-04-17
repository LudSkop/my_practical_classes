from tabulate import tabulate
import sys

def split_list(grade):
    less_avarage = []
    more_avarage = []
    count = 0
    colvo = len(grade)
    if  not grade:
        return [], []
    for element in grade :
        count += int(element)
    mid_avarage = count / colvo
    for element in grade:
        if int(element) <= mid_avarage:
            less_avarage.append(element)
        else:
            more_avarage.append(element)
    return less_avarage, more_avarage,
        
    
    
if __name__ == "__main__":
    data = {3, 5, 6, 78, 90,}
    less, more = split_list(data)
    data_dict = {
        'less': less,
        'more': more,
    }
    table = tabulate(data_dict, headers="keys", tablefmt='grid')

    print(table)

    
    