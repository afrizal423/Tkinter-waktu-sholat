from datetime import datetime
from tkinter import *
import urllib.request,json
import tkinter as tk
import tkinter.messagebox as MessageBox
import requests, os, json, time

win = tk.Tk()
win.title("Jadwal Sholat")
win.geometry("580x400")
win.resizable(width=False, height=False)

if "nt" != os.name:
    win.iconbitmap('@masjid1.jpg.xbm')
else:
    win.iconbitmap('masjid.ico')
def about():
    MessageBox.showinfo("About This App", "Dibuat oleh Afrizal Muhammad Yasin")  
menubar = Menu(win)
win.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=filemenu)
filemenu.add_command(label="Tentang aplikasi", command=about)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=win.quit)
class Clock:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.mFrame = Frame()

        self.watch = Label( text=self.time2, font=('times',15))
        self.watch.pack()

        self.changeLabel() 

    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=f'Waktu sekarang {self.time2} WIB')
        self.mFrame.after(200, self.changeLabel) 

def keluar():
        win.destroy()

def clear_widget_text(widget, widget2):
    widget['text'] = ""
    widget2['text'] = ""

def sholat():
    kota = entry.get()
    url = "https://api.myquran.com/v1/sholat/kota/cari/"+kota

    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    output = json.loads(data)
    # print(output['data'][0]['lokasi'])
    kota = output['data']
    try:
        idkota = kota[0]['id']
    except IndexError:
          label_2['text'] = text="Tidak ada kecocokan"
    tanggal = datetime.today().strftime('%Y/%m/%d')
    # print(idkota, tanggal)
    urlsholat = "https://api.myquran.com/v1/sholat/jadwal/"+idkota+"/"+tanggal
    page1=urllib.request.Request(urlsholat,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile1=urllib.request.urlopen(page1).read()
    data1 = infile1.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    output1 = json.loads(data1)
    # print(output1)
    datanya = output1['data']['jadwal']

    if output['status']:
        tanggalnya = datanya['tanggal']
        terbit = datanya['terbit']
        imsyak = datanya['imsak']
        subuh = datanya['subuh']
        dhuha = datanya['dhuha']
        dhuhur = datanya['dzuhur']
        ashar = datanya['ashar']
        maghrib = datanya['maghrib']
        isya = datanya['isya']
        kotanya = output1['data']['lokasi']
        label_2['text'] =  text=f'Lokasi  : {kotanya},\n' f'Hari  : {tanggalnya},\n'f'Matahari Terbit  : {terbit},\n'f'Imsak  : {imsyak},\n' f'Subuh  : {subuh},\n'f'Dhuha  : {dhuha},\n'f'Dhuhur  : {dhuhur},\n'f'Ashar  : {ashar},\n'f'Maghrib  : {maghrib},\n'f'Isya  : {isya}.\n'
      

        label_3['text'] = text="sumber : https://api.myquran.com/"
      
    else:
        print("gagal")


myLabel = Label(text="Jadwal Sholat Wilayah +62",fg="black",justify='center')
myLabel.config(font=("times",20))
myLabel.pack()
obj1 = Clock()

label_1 = Label( text="Masukkan kota yang ingin dicari  =",font=("bold", 12))
if "nt" != os.name:
    # Linux
    label_1.place(x=40,y=70)
else:
    # windows
    label_1.place(x=80,y=70)

entry = Entry(win)
entry.place(x=330,y=70,width=150)
label_2 = Label(win,font=("bold", 12),justify='left')
label_2.place(x=80,y=140)
label_3 = Label(win,font=("italic", 9),justify='left')
label_3.place(x=80,y=350)
if "nt" != os.name:
    # Linux
    Button(win,text="Keluar",command=keluar,width=10,bg='red',fg='white').place(x=100,y=100)
    Button(win,text="Clear",command=lambda : [clear_widget_text(label_2,label_3),entry.delete(0, 'end')],width=10).place(x=230,y=100)
    Button(win,text="Cari",command=sholat,width=10,bg='blue',fg='white').place(x=360,y=100)
else:
    # windows
    Button(win,text="Keluar",command=keluar,width=10,bg='red',fg='white').place(x=150,y=100)
    Button(win,text="Clear",command=lambda : [clear_widget_text(label_2,label_3),entry.delete(0, 'end')],width=10).place(x=250,y=100)
    Button(win,text="Cari",command=sholat,width=10,bg='blue',fg='white').place(x=350,y=100)



win.mainloop()