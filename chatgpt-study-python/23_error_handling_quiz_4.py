"""
ubah fungsi di atas supaya mengulangi input 
sampai user memasukkan angka valid 
(atau user mengetik q untuk keluar)
"""

def minta_angka_sampai_valid(prompt="Masukan angka (ketik q untuk keluar): "):
    while True:
        s = input(prompt).strip()
        if s.lower() == "q":
            print("Keluar.")
            return None
        try:
            return int(s)
        except ValueError:
            print("Input tidak valid! Coba lagi.")

angka = minta_angka_sampai_valid()
if angka is not None:
    print(f"Angka yang kamu masukkan: {angka}")
