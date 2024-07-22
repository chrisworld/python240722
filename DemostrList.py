# demo str list

strA = "python is very powerful"
strB = "파이썬은 강력해"
x = 100
y = 3.14

print(len(strA))
print(len(strB))
print(len(strA[0]))
print(len(strA[0:6]))
print(len(strA[:6]))
print(len(strA[-3:]))

colors = ["red", "blue", "green"]
print(colors)
print(type(colors))
colors.append("yellow")
colors.insert(1,"pink")
print(colors)
colors.remove("blue")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

# 형식 변환

a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)

#dic

tp = (10,20,30)
print(type(tp))
print(len(tp))

def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))
      
device = {"아이폰":5, "아이패드":10}
print(type(device))
device["맥북"] = 15
device["아이폰"] = 6
del device["아이패드"]
print(device)
print(device["맥북"])

for item in device.items():
    print(item)
    
      
