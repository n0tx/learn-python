from pegawai import Pegawai

class Manager(Pegawai):
  def __init__(self, nama, gaji, departemen):
    super().__init__(nama, gaji)
    self.departemen = departemen
    
  def info(self):
    print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}")

if __name__ == "__main__":
  p1 = Pegawai("Riki", 1000)
  p1.info()
  m1 = Manager(p1.nama, p1.gaji, "HR")
  m1.info()