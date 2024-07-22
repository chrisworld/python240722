# function.py

# 함수정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURL(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

print(connectURL("multi.com", "80"))
print(connectURL(port="8080", server="multi.com"))

x = 5
def func(a):
    return a+x

print(func(1))

def func2(a):
    x=1
    return a+x
print(func2(1))

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG","SPAM"))


g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
