a = 10
b = 20
print("10 + 20 = ") # 10 + 20 =
print(a + b) # 30
print("Konversi ke string...")
print("print(str(a) + str(b))")
print(str(a) + str(b)) # 1020

print("")

c = "50"
print("10 + \"50\" = ") # 10 + "50"

# print(a + c) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("Konversi ke integer...")
print("print(a + int(c))")
print(a + int(c)) 

print("Konversi ke string...")
print("print(str(a) + c)")
print(str(a) + c)

print("")

d = "20.5"
# print(a + d) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a + int(d)) # ValueError: invalid literal for int() with base 10: '20.5'
print("Konversi ke float...")
print("10 + \"20.5\"")
print(a + float(d))


