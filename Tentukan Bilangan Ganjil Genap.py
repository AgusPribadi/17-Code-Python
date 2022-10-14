# Menginput Angka
angka = int(input("Tulis Sebuah Angka: "))

# Jika Habis dibagi Nol, Maka Genap
if (angka % 2) == 0:
    print("{0} adalah Bilangan Genap".format(angka))

# Jika Tidak Habis dibagi Nol, Maka Ganjil
else:
    print("{0} adalah Bilangan Ganjil".format(angka))