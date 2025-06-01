# Inisialisasi list untuk menyimpan data buku
daftar_buku = []

def tambah_buku():
    while True:
        id_buku = input("Masukkan ID Buku: ")
        # Cek apakah ID Buku sudah ada dalam daftar
        for buku in daftar_buku:
            if buku['ID Buku'] == id_buku:
                print("Buku sudah terdaftar.")
                return  # Kembali ke menu utama tanpa menunggu input
        nama_buku = input("Masukkan Nama Buku: ")
        nama_penulis = input("Masukkan Nama Penulis: ")
        kategori_buku = input("Masukkan Kategori Buku: ")
        penerbit = input("Masukkan Penerbit: ")
        
        # Tambahkan buku baru ke dalam daftar_buku
        daftar_buku.append({
            "ID Buku": id_buku,
            "Nama Buku": nama_buku,
            "Nama Penulis": nama_penulis,
            "Kategori Buku": kategori_buku,
            "Penerbit": penerbit
        })
        print("Buku berhasil ditambahkan.")  # Pesan ini tetap ada
        
        # Tanyakan apakah pengguna ingin menambahkan buku lain
        lagi = input("Apakah Anda ingin menambahkan buku lain? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            break  # Keluar dari loop dan kembali ke menu utama

def tampilkan_buku():
    if not daftar_buku:
        print("Tidak ada buku dalam perpustakaan. Silakan tambahkan buku terlebih dahulu.")
        input("Press any key to continue...")
        return
    
    print("\n=== Menu Lihat Buku ===")
    for index, buku in enumerate(daftar_buku, start=1):
        print(f"\nBuku ke- {index}")
        print(f"ID Buku    : {buku['ID Buku']}")
        print(f"Nama Buku  : {buku['Nama Buku']}")
        print(f"Penulis    : {buku['Nama Penulis']}")
        print(f"Kategori   : {buku['Kategori Buku']}")
        print(f"Penerbit   : {buku['Penerbit']}")
    
    input("\nPress any key to continue...")

def cari_buku():
    nama_buku = input("Masukkan nama buku yang dicari: ")
    ditemukan = False
    for buku in daftar_buku:
        if nama_buku.lower() in buku['Nama Buku'].lower():
            print(f"\nDitemukan - ID Buku: {buku['ID Buku']}")
            print(f"Nama Buku: {buku['Nama Buku']}")
            print(f"Penulis: {buku['Nama Penulis']}")
            print(f"Kategori: {buku['Kategori Buku']}")
            print(f"Penerbit: {buku['Penerbit']}")
            ditemukan = True
    if not ditemukan:
        print("\nBuku tidak ditemukan.")
    input("\nPress any key to continue...")

def hapus_buku():
    id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
    for buku in daftar_buku:
        if buku['ID Buku'] == id_buku:
            daftar_buku.remove(buku)
            print("\nBuku berhasil dihapus.")
            input("Press any key to continue...")
            return
    print("\nBuku dengan ID tersebut tidak ditemukan.")
    input("Press any key to continue...")

def menu():
    while True:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_buku()
        elif pilihan == '2':
            tampilkan_buku()
        elif pilihan == '3':
            cari_buku()
        elif pilihan == '4':
            hapus_buku()
        elif pilihan == '5':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Press any key to continue...")

# Menjalankan program
menu()