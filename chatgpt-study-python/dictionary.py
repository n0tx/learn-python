"""
ini seperti Map di java,
associative array di php
"""

user = {
    "nama" : "Riki",
    "usia" : 25,
    "alamat": "Jl. kura-kura ninja, Jakarta"
}

print(user)
print("")

print("akses dictionary")
print("akses value by key")
print(user["nama"])
print("")

print("menambahkan no handphone ke dictionary user")
user["no handpone"] = "081310001000"
print(user)
print("")

print("panjang dictionary")
print(len(user))