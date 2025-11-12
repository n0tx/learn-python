from pathlib import Path
p = Path("mahasiswa.txt")
with p.open("r", encoding="utf-8") as f:
  isi = f.read()
  print(isi)