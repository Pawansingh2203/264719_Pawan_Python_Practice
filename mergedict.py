dict1={}
dict2={}
result={}
def inputdictionary():
    print("Enter the values in dictionary 1")
    n = 3
    dict1 = [ map(str,input().split()) for x in range(n)]
    print("Enter the values in dictionary 2")
    dict2 = [ map(str,input().split()) for x in range(n)]
    return

def merge_dictionary():
    result={**dict1, **dict2}
    print( result)

def print_result(result):
    print("After merging the Dictionary")
    print(result)