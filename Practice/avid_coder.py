x = input("enter the number:  ")
a = list()
for i in x.split(','):
    a.append(i)
t = tuple(a)
print(a)
print(t)