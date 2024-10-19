from cryptography.fernet import Fernet

#Fungsi untuk membuat kunci
def kunci():
    keys = Fernet.generate_key()
    with open("key_file.key", "wb") as key:
        key.write(keys)

#Fungsi untuk enkripsi file/folder
def enkripsi(nama_file):
    #Load key yang sudah dibuat
    with open("key_file.key", "rb") as keys:
        key = keys.read()
        f = Fernet(key)   

    #Membaca file yang akan di enkripsi
    with open(nama_file, "rb") as original:
        file_data = original.read()

    #Melakukan enkripsi pada file yang ditentukan
    enkripsi_mode = f.encrypt(file_data)

    #Menyimpan file yang di enkripsi
    with open(nama_file + ".enkripsi", "wb") as save:
        save.write(enkripsi_mode)

    #Pesna berhasil ini akan muncul apabila file benar berhasil dijalakan
    print("Berhasil enkripsi")

#Menjalankan proses enkripsi
kunci()
#Masukkan file yang akan di enkripsi
enkripsi("")