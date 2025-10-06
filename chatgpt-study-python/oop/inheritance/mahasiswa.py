from orang import Orang
class Mahasiswa(Orang):
  def __init__(self, nama, ipk):
    super().__init__(nama)
    self.ipk = ipk
  
  def info(self):
    print(f"{self.nama} dengan ipk {self.ipk}")

if __name__ == "__main__":
  m1 = Mahasiswa("Riki", 3.09)
  m1.sapa()
  m1.info()