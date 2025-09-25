"""
Buat for loop yang mencetak semua nama mahasiswa dari 
mahasiswa_list di 16_dictionary_list_bersarang.py, hanya yang ipk ≥ 3.7.
"""

mahasiswa_list = [
    {"nama": "Andi", "ipk": 3.9},
    {"nama": "Budi", "ipk": 3.5},
    {"nama": "Citra", "ipk": 3.7}
]

for mhs in mahasiswa_list:
    if mhs["ipk"] >= 3.7:
        print(f"{mhs["nama"]} - {mhs["ipk"]}")