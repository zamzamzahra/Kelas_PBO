class student:
 """ A class representing a student"""
 def __init__(self,n,a,k,p):
    self.full_name=n
    self.age=a
    self.kampus=k
    self.prodi=p
 def get_age(self):
    return self.age
 def get_kampus(self):
    return self.kampus
 def get_prodi(self):
    return self.prodi
f = student ("Zamzam Kholidatuzzahra",19,"UPI PWK","Sistem Telekomunikasi")
print(f.full_name)
print(f.get_age())
print(f.get_kampus())
print(f.get_prodi())