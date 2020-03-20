<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Aplikasi Desktop Lihat Waktu Sholat

Aplikasi desktop sederhana dibangun dengan Tkinter Python untuk melihat waktu sholat. Data diambil dari [API Banghasan](https://api.banghasan.com/)

## Installation

Buat virtualenv terlebih dahulu
```bash
virtualenv {nama_virtual}
```
Masuk kedalam virtual
```bash
source {nama_virtual}/Scripts/activate
```
Install requirements menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt
```
Jalankan dengan perintah
```bash
python sholatapp.py
```
### Build menjadi (.exe) windows
Build menjadi Application(.exe) Windows
```bash
python setup.py build
```
Lokasi hasil eksekusi berada pada /build
### Build menjadi desktop app di linux
- Copykan file launcher.desktop ke Desktop linux kalian
- Klik kanan pada file (launcher.desktop) , pilih <b><i>Allow launching</i></b>
## Demo <br>
Windows <br>
![Alt Text](https://github.com/afrizal423/Tkinter-waktu-sholat/blob/master/assets/tkintersholat.gif?raw=true)<br>

<br>Linux (Tested on Ubuntu)<br>
![Alt Text](https://github.com/afrizal423/Tkinter-waktu-sholat/blob/master/assets/linux.gif?raw=true)<br>

## Releases
Tagging untuk belajar tiap partnya. <br>
- [v1.0.0](https://github.com/afrizal423/Tkinter-waktu-sholat/releases/tag/v1.0.0) - Release for windows 

