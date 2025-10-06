class Mahasiswa:
  def __init__(self, nama, ipk):
    self.nama = nama
    self.ipk = ipk
  
  def sapa(self):
    print(f"Halo nama saya {self.nama} dengan ipk {self.ipk}")
    
m1 = Mahasiswa("Riki", 3.09)
m1.sapa()