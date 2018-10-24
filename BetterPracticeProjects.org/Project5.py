a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in a:
    for y in b:
        if x == y:
            c.append(x)
            
print (c)

"""----------Better Version---------"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

[(c.append(x)) for x in a if x in b if x not in c]

print (c)

"""----------Another Version--------"""
import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = []
result = [i for i in a if i in b if i not in result]
print (result)
