def missing_num(lst):
   for n in range(1,11):
       if n not in lst:
           return(n)


print(missing_num([1,2,5,6,4,7,9,10]))
