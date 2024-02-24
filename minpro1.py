import os
os.system('cls')


class Toko:
    def __init__(self):
        self.inven = [
            {"id" : "1a", "nama" : "cat merah", "kategori" : "cat", "harga" : 70000, "stok" : 6},
            {"id" : "1b", "nama" : "semen tiga roda", "kategori" : "cat", "harga" : 50000, "stok" : 15},
            {"id" : "1c", "nama" : "cat biru", "kategori" : "cat", "harga" : 70000, "stok" : 4},
            {"id" : "1d", "nama" : "cat abu-abu", "kategori" : "cat", "harga" : 70000, "stok" : 9},
            {"id" : "1e", "nama" : "keramik", "kategori" : "cat", "harga" : 120000, "stok" : 20}
        ]

    def tambah_barang(self, id, nama, kategori, harga, stok):
        for i in toko.inven:
            if id == i["id"]:
                print("Id sudah tersedia, buat id barang baru")
                return
        toko.inven.append(
            {
                "id" : id,
                "nama" : nama,
                "kategori" : kategori,
                "harga" : harga,
                "stok" : stok
            }
        )
        print(f"{nama} dengan {id} berhasil ditambahkan")

    def lihat_barang(self):
        print(toko.inven)

    def update_barang(self, id_barang):
        for item in self.inven:
            if item['id'] == id_barang:
                print("Menu Update:")
                print("1. Nama")
                print("2. Kategori")
                print("3. Harga")
                print("4. Stok")
                print("5. Semuanya")
                pilihan = input("Pilih apa yang ingin diupdate: ")
                if pilihan == '1':
                    nama_baru = input("Masukkan nama baru: ")
                    print("Nama telah berhasil diupdate.")
                elif pilihan == '2':
                    kategori_baru = input("Masukkan kategori baru: ")
                    item['kategori'] = kategori_baru
                    print("Kategori telah berhasil diupdate.")
                elif pilihan == '3':
                    harga_baru = int(input("Masukkan harga baru: "))
                    item['harga'] = harga_baru
                    print("Harga telah berhasil diupdate.")
                elif pilihan == '4':
                    stok_baru = int(input("Masukkan stok baru: "))
                    item['stok'] = stok_baru
                    print("Stok telah berhasil diupdate.")
                elif pilihan == '5':
                    nama_baru = input("Masukkan nama baru: ")
                    if nama_baru == '':
                        return toko.update_barang(id_barang)
                    kategori_baru = input("Masukkan kategori baru: ")
                    if kategori_baru == '':
                        return toko.update_barang(id_barang)
                    harga_baru = int(input("Masukkan harga baru: "))
                    if harga_baru == '':
                        return toko.update_barang(id_barang)
                    stok_baru = int(input("Masukkan stok baru: "))
                    if stok_baru == '':
                        return toko.update_barang(id_barang)
                    item['nama'] = nama_baru
                    item['kategori'] = kategori_baru
                    item['harga'] = harga_baru
                    item['stok'] = stok_baru
                else:
                    print("Pilihan tidak valid.")
                return
        print("Item dengan ID tersebut tidak ditemukan.")

    def hapus_barang(self, id_barang):
        for item in self.inven:
            if item['id'] == id_barang:
                self.inven.remove(item)
                print("Item dengan ID {} telah berhasil dihapus.".format(id_barang))
                return
        print("Item dengan ID tersebut tidak ditemukan.")

toko = Toko()

def main():

    while True:
        print('''
        ============Toko IRY============
        [+]  1. Tambah Barang        [+]
        [+]  2. Tampilkan Barang     [+]
        [+]  3. Update Barang        [+]
        [+]  4. Hapus Barang         [+]
        [+]  5. Keluar               [+]
        ================================
        ''')
        pilihan = input("masukkan pilihan anda : ")
        if pilihan == '1': # menu create
            id = input("masukkan id barang : ")
            nama = input("masukkan nama barang : ")
            kategori = input("masukkan kategori barang : ")
            harga = int(input("masukkan harga barang : "))
            stok = int(input("masukkan stok barang : "))
            toko.tambah_barang(id, nama, kategori, harga, stok)

        elif pilihan == '2': # menu read
            toko.lihat_barang()

        elif pilihan == '3':
            id_barang = input("masukkan id barang yang ingin diupdate")
            toko.update_barang(id_barang)

        elif pilihan == '4':
            id_barang = input("Masukkan id barang yang ingin dihapus")
            toko.hapus_barang(id_barang)
        elif pilihan == '5':
            break
        else:
            print("Menu tidak valid")

main()