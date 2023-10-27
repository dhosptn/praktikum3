import math
# Input jari-jari lingkaran dari pengguna
r = float(input("Masukan Jari-jari lingkaran : "))

# Menghitung luas lingkaran
luas = math.pi*(r*r)

# Menghitung keliling lingkaran
keliling = 2*math.pi*r

# Menampilkan hasil
print ("Luas Lingkaran \t\t= ",luas)
print ("Keliling Lingkaran\t= ",keliling)