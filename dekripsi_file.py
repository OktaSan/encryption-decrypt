from cryptography.fernet import Fernet

#Dekripsi dengan alur yang mudah di pahami
def dekripsi(nama_file):
    #Kita meload key dari file key_file.key
    with open("key_file.key", "rb") as kunci:
        key = kunci.read()

    #Setelah diload, masukka ke dalam variabel ini
    f = Fernet(key)

    #Kita membaca file yang di enkripsi
    with open(nama_file, "rb") as asli:
        original = asli.read()

    #Proses dekripsi filenya
    dekripsi_file = f.decrypt(original)

    file_name = nama_file
    new_file_name = file_name.replace(".enkripsi", "")

    #Menyimpan file yang sudah di dekripsi ke dalam file baru
    with open(new_file_name, "wb") as new:
        new.write(dekripsi_file)

        #Pesan jika dekripsi berhasil dilakukan
        print("Dekripsi file telah berhasil dilakukan !")

#Masukkan file yang akan di dekripsi
dekripsi("")

