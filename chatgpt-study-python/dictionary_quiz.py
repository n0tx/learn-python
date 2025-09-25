"""
Buat sebuah dictionary mahasiswa dengan isi:

nama: "Andi"
jurusan: "Informatika"
ipk: 3.8

Lalu:
Print nama mahasiswa
Ubah ipk jadi 3.9
Tambahkan key baru: "angkatan" = 2022
"""

mahasiswa = {
    "nama": "Andi",
    "jurusan": "Informatika",
    "ipk": 3.8
}

print("print mahasiswa")
print(mahasiswa)
print("")

print("ubah ipk jadi 3.9")
mahasiswa["ipk"] = 3.9
print(mahasiswa)
print("")

print("menambahkan key baru: \"angkatan\" = 2002")
mahasiswa["angkatan"] = 2002
print(mahasiswa)
print("")