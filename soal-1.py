import os

kontak = []

def menu():
    os.system('cls')
    print("-------Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    pilihan=int(input("Pilih menu: "))
    return pilihan

def daftar_kontak():
    print("--------Daftar Kontak-------")
    for key in kontak:
        print("Nama       :", key['nama'])
        print("No Telepon :", key["no tlp"])
        print("----------------------------")

def tambah_kontak():
    print("-------Tambah Kontak--------")
    new = {'nama':'-', "no tlp":'-'}
    new["nama"] = input("Masukan nama kontak  : ")
    new["no tlp"] = input("Masukan No telepon   : ")
    kontak.append(new)
    print("Kontak berhasil ditambahkan")

def cari_kontak():
    a=0
    key = input('Masukan nama kontak : ')
    for i in kontak:
        if key==i['nama']:
            a = 1
            print("Nama       :", i['nama'])
            print("No Telepon :", i["no tlp"])
            print("----------------------------")
    if a==0:
        print('Kontak yang Anda cari tidak ditemukan')

def hapus_kontak():
    a=0
    key=input('Masukan nama kontak yang ingin dihapus : ')
    for i in kontak:
        if key==i['nama']:
            a = 1
            kontak.remove(i)
            print("Kontak berhasil dihapus")
            break
    if a==0:
        print('Kontak yang Anda cari tidak ditemukan')

pilihan=menu()
while(pilihan!=5):
    os.system('cls')
    if pilihan==1:
        daftar_kontak()
    elif pilihan==2:
        tambah_kontak()
    elif pilihan==3:
        cari_kontak()
    elif pilihan==4:
        hapus_kontak()  
    else:
        print("Menu yang Anda pilih tidak tersedia!\nSilahkan pilih menu lainnya")
    input('Tekan enter untuk kembali ke menu....')
    pilihan=menu()

os.system('cls')
print("----Terima Kasih-----")