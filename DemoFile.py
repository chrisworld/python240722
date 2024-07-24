
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫\n둘\n셋\n")
f.close()

f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

f.seek(0)
lst = f.readlines()
print(lst)


f.close