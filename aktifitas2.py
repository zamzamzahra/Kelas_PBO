bil1=int(input("Masukkan angka pertama: "))
bil2=int(input("Masukkan angka kedua: "))

jumlah=bil1+bil2
kurang=bil1-bil2
kali=bil1*bil2
bagi=bil1/bil2
modulus=bil1%bil2

print("Hasil dari %d + %d = %d" % (bil1, bil2, jumlah))
print("Hasil dari %d - %d = %d" % (bil1, bil2, kurang))
print("Hasil dari %d * %d = %d" % (bil1, bil2, kali))
print("Hasil dari %d / %d = %d" % (bil1, bil2, bagi))
print("Hasil dari %d mod %d = %d" % (bil1, bil2, modulus))