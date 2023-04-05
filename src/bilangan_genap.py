#Menentukan bilangan genap dan ganjil

#-menginput angka
angka = int(input("Tulis sebuah angka: "))
 
#-jika habis dibagi, maka genap
if (angka % 2) == 0:
   print(angka, "adalah bilangan genap")
 
#-jika tidak habis dibagi, maka ganjil
else:
   print(angka, "adalah bilangan ganjil") 
