"""
ubah fungsi di atas supaya mengulangi input 
sampai user memasukkan angka valid 
(atau user mengetik q untuk keluar)
"""

# bungkus dalam sebuah fungsi
def input_angka(prompt: str = "Masukan angka: ") -> int | None:
    s = input(prompt).strip() # strip() buat membersihkan spasi sebelum dan sesudah
    try:
        return int(s)
    except ValueError as e:
        print("Input tidak valid!!")
        return None # else jadi hilang unreachable karena ada return disini
    finally:
        print("Program check input selesai")


angka = input_angka()
while (angka is None):
    angka = input_angka()
else:
    print(f"Angka yang kamu masukkan: {angka}")