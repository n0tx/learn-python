"""
Tulislah kode Python untuk kasus berikut:

Minta input angka dari user (pakai input())
Konversi ke integer

Jika user memasukkan selain angka, 
tangkap error dan print "Input tidak valid!"

Jika berhasil, print "Angka yang kamu masukkan: X"
Jawaban versi 2
- menjadikan fungsi agar mudah dipakai ulang dari error_handling_quiz.py sebelumnya
- membuat 
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
if angka is not None:
    print(f"Angka yang kamu masukkan: {angka}")


