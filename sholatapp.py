from datetime import datetime
from tkinter import *
import urllib.request,json
import tkinter as tk
import requests
import json
import time

win = tk.Tk()
win.title("Jadwal Sholat")
win.geometry("580x400")
win.resizable(width=False, height=False)
win.iconbitmap('masjid.ico')

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
    url = "https://api.banghasan.com/sholat/format/json/kota/nama/"+kota

    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    output = json.loads(data)
    kota = output['kota']
    try:
        idkota = kota[0]['id']
    except IndexError:
          label_2['text'] = text="Tidak ada kecocokan"

    tanggal = datetime.today().strftime('%Y-%m-%d')
    urlsholat = "https://api.banghasan.com/sholat/format/json/jadwal/kota/"+idkota+"/tanggal/"+tanggal
    page1=urllib.request.Request(urlsholat,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile1=urllib.request.urlopen(page1).read()
    data1 = infile1.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    output1 = json.loads(data1)
    datanya = output1['jadwal']['data']

    if output['status'] == "ok":
        tanggalnya = datanya['tanggal']
        terbit = datanya['terbit']
        imsyak = datanya['imsak']
        subuh = datanya['subuh']
        dhuha = datanya['dhuha']
        dhuhur = datanya['dzuhur']
        ashar = datanya['ashar']
        maghrib = datanya['maghrib']
        isya = datanya['isya']
        kotanya = kota[0]['nama']
        label_2['text'] =  text=f'Kota  : {kotanya},\n' f'Hari  : {tanggalnya},\n'f'Matahari Terbit  : {terbit},\n'f'Imsak  : {imsyak},\n' f'Subuh  : {subuh},\n'f'Dhuha  : {dhuha},\n'f'Dhuhur  : {dhuhur},\n'f'Ashar  : {ashar},\n'f'Maghrib  : {maghrib},\n'f'Isya  : {isya},\n'
      

        label_3['text'] = text="sumber : https://api.banghasan.com/"
      
    else:
        print("gagal")


myLabel = Label(text="Jadwal Sholat Wilayah +62",fg="black",justify='center')
myLabel.config(font=("times",20))
myLabel.pack()
obj1 = Clock()

label_1 = Label( text="Masukkan kota yang ingin dicari  =",font=("bold", 12))
label_1.place(x=80,y=70)

entry = Entry(win)
entry.place(x=330,y=70,width=150)
label_2 = Label(win,font=("bold", 12),justify='left')
label_2.place(x=80,y=140)
label_3 = Label(win,font=("italic", 9),justify='left')
label_3.place(x=80,y=350)
Button(win,text="Keluar",command=keluar,width=10,bg='red',fg='white').place(x=150,y=100)
Button(win,text="Clear",command=lambda : [clear_widget_text(label_2,label_3),entry.delete(0, 'end')],width=10).place(x=250,y=100)
Button(win,text="Cari",command=sholat,width=10,bg='blue',fg='white').place(x=350,y=100)


win.mainloop()