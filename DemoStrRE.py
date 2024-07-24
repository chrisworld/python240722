
data = "<<< spam and ham >>>"
result = data.strip("<>")
print(data)
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))

strA = "pth is very pow"
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())


import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("apple", "this is apple")
print(result)
print(result.group())

result = re.search("\d{4}", "올해는 2024입니다.")
print(result)
print(result.group())