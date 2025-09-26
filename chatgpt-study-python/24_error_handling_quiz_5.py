"""
ubah fungsi di atas supaya mengulangi input 
sampai user memasukkan angka valid 
(atau user mengetik q untuk kelua

tambahan baru, versi yang menerima float dan punya batas percobaan
"""

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
"""

def minta_number(prompt="Masukan angka (qi untuk keluar): ", max_attempts: int = 5):
    attempts = 0
    while attempts < max_attempts:
        s = input(prompt).strip()
        if s.lower() == "q":
            print("Keluar.")
            return None
        try:
            # coba int dulu, jika gagal coba float
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                attempts += 1
                print(f"Input tidak valid! Sisa percobaan: {max_attempts - attempts}")
    print("Melebihi batas percobaan.")
    return None  
    
angka = minta_number()
if angka is not None:
    print(f"Angka yang kamu masukkan: {angka}")
    
