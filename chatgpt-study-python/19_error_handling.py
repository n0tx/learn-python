try:
    # kode yang mungkin error
    print("Fungsi Konverting dimulai...")
    x = int("abc")
except ValueError as e:
    # tangani error tertentu
    print("!!! Terjadi error !!!", e)
finally:
    # selalu dijalankan
    print("Fungsi Konverting selesasi...")