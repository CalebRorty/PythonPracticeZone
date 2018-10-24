a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
[(b.append(i)) for i in a if i < 5]

print (b)

"""-----------Written In One Line-----------"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[(a.remove(i)) for i in a[::-1] if i >= 5]

print (a)

#technicaly 3
