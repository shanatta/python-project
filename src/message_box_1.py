#Message box

#-menggunakan modul Tkinter
from tkinter import *
# Menggunakan class messagebox
import tkinter.messagebox

#-membuat object Tkinter
root = Tk()
#-mengatur ukuran window
root.geometry("300x150")

#-membuat function yang isinya sebuah message
def Message():
    tkinter.messagebox.showinfo("Haii", "Morning Azuru, have a nice day!")

#-membuat button yang jika diklik akan memanggil function Message() yang dibuat diatas lalu menampilkan messagenya
button = Button(root, text="Show Message", command=Message)
button.pack(pady=20)

#-menjalankan program
root.mainloop() 
