#Kalender

#-mengimpor modul calendar
import calendar
 
#-menginput tahun dan bulan
yy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan Bulan: "))
 
#-menampilkan kalender bulanan
print(calendar.month(yy, mm)) 
