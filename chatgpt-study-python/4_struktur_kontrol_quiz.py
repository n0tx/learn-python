# Kalau variabel nilai = 75, tulis kode Python sederhana untuk cek:

# Kalau nilai >= 80 -> print "Bagus"

# Kalau nilai >= 60 -> print "Cukup"

# Selain itu -> print "Kurang"

# contoh pemakaian
def nilai_komentar(nilai: int) -> str:
    """Kembalikan komentar berdasarkan nilai"""
    if nilai >= 80:
        return "Bagus"
    if nilai >= 60:
        return "Cukup"
    else:
        return "Kurang"
    
print(nilai_komentar(75))
