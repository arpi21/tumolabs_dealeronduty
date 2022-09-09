def averageoflist():
    str = input("Input a list of numbers separated by a space  ")
    lst = str.split(" ")
    newlst = [eval(i) for i in lst]
    return sum(newlst)/len(newlst)
print(averageoflist())
