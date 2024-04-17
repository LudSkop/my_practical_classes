def lookup_key(data, value):
    result = []
    for key, el in data.items():
        print(el)
        if el == value:
            result.append(key)
    return print(result)
            
    
    
        
            
if __name__ == "__main__":
    data = {
        '1': 1,
        '2': 2,
        '3': 1,

    }  
    val = 2
    lookup_key(data, val)