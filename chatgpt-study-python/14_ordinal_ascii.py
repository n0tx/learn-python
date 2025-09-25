"""
print ordinal number dari huruf 'A'
print ordinal number dari symbol '€' (Euro)
"""

huruf = 'A'
symbol = '€'

print("print ordinal number dari sebuah huruf atau symbol")
print(f"huruf: {huruf}")
ordinal_number_huruf = ord(huruf)
print(f"ordinal number: {ordinal_number_huruf}")
print("")

print(f"symbol: {symbol}")
ordinal_number_symbol = ord(symbol)
print(f"ordinal number: {ordinal_number_symbol}")
print("")

print("print character, huruf dari ordinal number")
print(f"ordinal number: {ordinal_number_huruf}")
print(f"huruf: {chr(ordinal_number_huruf)}") # "A"
print("")

print("print symbol dari ordinal number")
print(f"ordinal number: {ordinal_number_symbol}")
print(f"symbol: {chr(ordinal_number_symbol)}") # "€"
print("")

