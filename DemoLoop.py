value = 5
while value > 0:
    print(value)
    value -=1


lst = ["apple", 100, 3.14]
for item in lst:
    print(item)

print(list(range(1,11)))
print(list(range(2000,2025)))
print(list(range(1,32)))

lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "orange")
print([len(i) for i in tp])


