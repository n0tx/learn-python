from pathlib import Path
p = Path("mahasiswa.txt")
with p.open("w", encoding = "utf-8") as f:
  f.write("Andi, Informatika, 3.9\n")
  f.write("Budi, Sistem Informasi, 3.5\n")
  f.write("Citra, Teknik Komputer, 3.7\n")