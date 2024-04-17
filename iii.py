import sys


def get_grade(key):
    k ={
    "F":1,
    "FX":2,
    "E":3,
    "D":3,
    "C":4,
    "B":5,
    "A":5
    } 
    
    return k.get(key)


def get_description(key):
    k ={
        'F':'Unsatisfactorily',
        'FX':'Unsatisfactorily',
        'E':'Enough',
        'D':'Satisfactorily',
        'C':'Good',
        'B':'Very good',
        "A":"Perfectly"
}
    
    return k.get(key)
        
if __name__ == "__main__":
    print(get_grade(sys.argv[4]))
    print(get_description(sys.argv[3]))

