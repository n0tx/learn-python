"""
Tulis kode Python untuk mencetak semua
kode ordinal number dari string "ABC"
"""

def get_ordinal_numbers(word: str) -> list[int]:
    result: list[int] = []
    for s in word:
        result.append(ord(s))
    return result

def get_ordinal_numbers_ringkas(word: str) -> list[int]:
    return [ord(s) for s in word]

def get_ordinal_numbers_map(word: str) -> list[int]:
    return list(map(ord, word))

print("get ordinal number")
print(get_ordinal_numbers("ABC"))
print("")

print("get ordinal number lebih ringkas")
print(get_ordinal_numbers_ringkas("ABC"))
print("")

print("get ordinal number menggunakan map")
print(get_ordinal_numbers_map("ABC"))
print("")