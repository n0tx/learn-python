"""
Tulislah kode Python untuk kasus berikut:

Minta input angka dari user (pakai input())
Konversi ke integer

Jika user memasukkan selain angka, 
tangkap error dan print "Input tidak valid!"

Jika berhasil, print "Angka yang kamu masukkan: X"
"""

input_angka = input("Masukan angka: ")

try:
    angka_hasil_konversi = int(input_angka)
except ValueError as e:
    print("Input tidak valid!!")
else:
    print("Angka yang kamu masukkan: ", angka_hasil_konversi)
finally:
    print("Program check input selesai")