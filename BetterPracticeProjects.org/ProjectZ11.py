num = int(input("Pleae Enter a number: "))

lNum = num + 1
a = []

[(a.append(i)) for i in range(1,lNum) if num / i != 0 ]
if len(a) > 1:
    print ("This # Is Prime")
else:
    print ("This # Not Prime")
