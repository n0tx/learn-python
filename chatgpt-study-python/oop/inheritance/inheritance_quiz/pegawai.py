class Pegawai:
  def __init__(self, nama, gaji):
    self.nama = nama
    self.gaji = gaji
  
  def info(self):
    print(f"Nama: {self.nama}, Gaji: {self.gaji}")