# mini aplikasi perpustakaan dengan python
# Shelyn Yaasinta JC - DS 012
listBuku = [
    {
        'judul': 'Pendidikan Modern',
        'kategori': 'Pendidikan',
        'penulis': 'Dian Prima',
        'tahun': 2020,
        'harga': 20000,
        'bahasa':'Indonesia'
    },
    {
        'judul': 'Education Revolution',
        'kategori': 'Pendidikan',
        'penulis': 'Sir Ken Robinson',
        'tahun': 2017,
        'harga': 20000,
        'bahasa':'Inggris'
    },
    {
        'judul':'Dunia Kecil',
        'kategori':'Komik',
        'penulis':'Rini Kartika',
        'tahun': 2012,
        'harga': 10000,
        'bahasa':'Indonesia'
    },
    {
        'judul':'Lost in Time',
        'kategori':'Komik',
        'penulis':'Sarah Miller',
        'tahun': 2018,
        'harga': 10000,
        'bahasa':'Inggris'
    },
    {
        'judul':'Bayangan Cinta',
        'kategori':'Fiksi',
        'penulis':'Agung Nugroho',
        'tahun': 2018,
        'harga': '10000',
        'bahasa':'Indonesia'
    },
    {
        'judul': 'Midnight Return',
        'kategori': 'Fiksi',
        'penulis': 'Alex Turner',
        'tahun': 2020,
        'harga': '10000',
        'bahasa':'Inggris'
    }
    
]

cart = [] # variable untuk menyimpan buku yang akan di pinjam 

# Menu awal
def menuAwal() :
    while True :
        pilih = input('''
                >>>>>>>>>> Selamat Datang di Perpustakaan <<<<<<<<<<
                
                Masuk Sebagai : 
                1. Pustakawan
                2. Pengunjung Perpustakaan
                3. Keluar Program
                      
                Silahkan Pilih Angka Yang Ingin Di Jalankan : ''')
        if pilih == '1' :
            login()
        elif pilih == '2' :
            pengunjung()
        elif pilih == '3' :
            exit()
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-3)')

# menu awal Pustakawan 
def pustakawan():
    while True :
        pilihanMenu = input('''
            >>>>>>>>>> Data Buku Perpustakan <<<<<<<<<<

                List Menu :
                1. Menampilkan Daftar Buku Yang Tersedia
                2. Menambah Buku
                3. Update Data Buku
                4. Menghapus Buku
                5. Kembali Ke Menu Utama
                6. Keluar Program

                Silahkan Pilih Menu Yang Ingin Di Jalankan: ''')
        if(pilihanMenu == '1') :
            menampilkanDaftarBuku()
        elif(pilihanMenu == '2') :
            menambahBuku()
        elif(pilihanMenu == '3') :
            updateDataBuku()
        elif(pilihanMenu == '4') :
            hapusBuku()
        elif(pilihanMenu == '5') :
            menuAwal()
        elif(pilihanMenu == '6'):
            print ("Terimakasih Sudah Berkunjung\nSemoga Harimu Menyenangkan\n")
            exit()
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-6)')
            

# Menu Pengunjung Perpustakan
def pengunjung() :
    while True :
        pilihanMenu = input('''
            >>>>>>>>>> Selamat Datang di Perpustakaan <<<<<<<<<<

            List Menu :
            1. Menampilkan Daftar Buku Yang Tersedia
            2. Meminjam Buku
            3. Keranjang Buku
            4. Kembali Ke Menu Utama

            Silahkan Pilih Menu Yang Ingin Di Jalankan : \n''')
        if(pilihanMenu == '1') :
            menampilkanDaftarBuku2()
        elif(pilihanMenu == '2') :
            pinjamBuku()
        elif(pilihanMenu == '3') :
            keranjang()
        elif(pilihanMenu == '4') :
            menuAwal()
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-4)')

# login untuk Pustakawan
userName = "user" ; password = "12345"
def login():
    max_gagal = 3 # jumlah maksimal mencoba login
    gagal = 0 # untuk menyimpan value gagal login user
    print ('Silahkan Masukan Username dan Password Pustakawan \n')

    while gagal < max_gagal:
        inputUsername = input('Username: ')
        inputPassword = input('Password: ')

        if inputUsername.lower() == userName and inputPassword == password:
            print('Selamat, Anda berhasil!')
            pustakawan()
            return
        else:
            print('Login gagal.')
            gagal += 1

    print(f"Anda telah melebihi batas percobaan login yang diperbolehkan ({max_gagal} kali).")
    exit()

# fitur read pustakawan dan pengunjung
def menampilkanDaftarBuku() :
    while True:
        angka = input('''
            ++++++++++ Daftar Buku ++++++++++
        
            1. Menampilkan Semua Daftar Buku Yang Tersedia
            2. Menampilkan Daftar Buku Sesuai Kategori
            3. Menampilkan Buku Sesuai Index
            4. Kembali Ke Menu Awal
                              
            Silahkan pilih angka yang ingin dijalankan : ''')
        
        if(angka == '1') :
            semuaBuku()
        elif(angka == '2') :
            kategori() 
        elif(angka == '3') :
            index()
        elif(angka == '4') :
            pustakawan()
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-4)')
def menampilkanDaftarBuku2() :
    while True:
        angka = input('''
            ++++++++++ Daftar Buku ++++++++++
        
            1. Menampilkan Semua Daftar Buku Yang Tersedia
            2. Menampilkan Daftar Buku Sesuai Kategori
            3. Menampilkan Buku Sesuai Index
            4. Kembali Ke Menu Awal
                              
            Silahkan pilih angka yang ingin dijalankan : ''')
        
        if(angka == '1') :
            semuaBuku()
        elif(angka == '2') :
            kategori() 
        elif(angka == '3') :
            index()
        elif(angka == '4') :
            pengunjung()
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-4)')
# menampilkan semua buku
from prettytable import PrettyTable

def semuaBuku():
    if len(listBuku) == 0:
        print("Daftar Buku Kosong")
        menampilkanDaftarBuku()
    else:
        table = PrettyTable()
        # menentukan kolom-kolom tabel.
        table.field_names = ["Index", "Harga", "Judul", "Kategori", "Tahun", "Penulis", "Bahasa"] 
        for i in range(len(listBuku)): 
            buku = listBuku[i] # data dari setiap buku ditambahkan ke tabel sebagai satu baris.
            table.add_row([i, buku["harga"], buku["judul"], buku["kategori"], buku["tahun"], buku["penulis"], buku["bahasa"]])
        print(table)
#+-------+-------+----------------------+------------+-------+------------------+-----------+
#| Index | Harga |        Judul         |  Kategori  | Tahun |     Penulis      |   Bahasa  |
#+-------+-------+----------------------+------------+-------+------------------+-----------+
#|   0   | 20000 |  Pendidikan Modern   | Pendidikan |  2020 |    Dian Prima    | Indonesia |
#|   1   | 20000 | Education Revolution | Pendidikan |  2017 | Sir Ken Robinson |  Inggris  |
#|   2   | 10000 |     Dunia Kecil      |   Komik    |  2012 |   Rini Kartika   | Indonesia |
#|   3   | 10000 |     Lost in Time     |   Komik    |  2018 |   Sarah Miller   |  Inggris  |
#|   4   | 10000 |    Bayangan Cinta    |   Fiksi    |  2018 |  Agung Nugroho   | Indonesia |
#|   5   | 10000 |   Midnight Return    |   Fiksi    |  2020 |   Alex Turner    |  Inggris  |
#+-------+-------+----------------------+------------+-------+------------------+-----------+

# memfilter buku sesuai kategori
def kategori():
    if len(listBuku) == 0:
        print("Daftar Buku Kosong")
        menampilkanDaftarBuku()
    else:
        kategori_input = input('Masukkan Kategori Buku: ')
        found_books = [buku for buku in listBuku if buku['kategori'].capitalize() == kategori_input.capitalize()]
        if found_books:
            table = PrettyTable()
            table.field_names = ["Index", "Harga", "Judul", "Kategori", "Tahun", "Penulis", "Bahasa"]
            
            for buku in found_books:
                index = listBuku.index(buku)
                table.add_row([index, buku["harga"], buku["judul"], buku["kategori"], buku["tahun"], buku["penulis"], buku["bahasa"]])
            
            print(table)
        else:
            print(f'Tidak ada buku dengan kategori {kategori_input}')

# memfilter buku sesuai index
def index():
    if len(listBuku) == 0:
        print("Daftar Buku Kosong")
        menampilkanDaftarBuku()
    else:
        try: # untuk menangani kemungkinan kesalahan pada input pengguna.
            indexBuku = int(input('Masukkan Index Buku yang Ingin Dicari: '))
            if 0 <= indexBuku < len(listBuku): # pengecekan apakah index yang dimasukkan berada dalam rentang 
                buku = listBuku[indexBuku]
                table = PrettyTable()
                table.field_names = ["Index", "Harga", "Judul", "Kategori", "Tahun", "Penulis", "Bahasa"]
                table.add_row([indexBuku, buku["harga"], buku["judul"], buku["kategori"], buku["tahun"], buku["penulis"], buku["bahasa"]])
                print(table)
            else:
                print(f'Index {indexBuku} tidak valid.')
        except ValueError:
            print('Input harus berupa angka.')

             
# fitur Create 
from prettytable import PrettyTable

def menambahBuku():
    while True:
        create1 = input('''
            ++++++++++ Menu Menambah Daftar Buku ++++++++++

            1. Menambah Buku
            2. Kembali Ke Menu Utama
                            
            Silahkan Pilih Angka Yang Ingin Di Jalankan : ''')

        if create1 == '1':
            if len(listBuku) == 0:
                print("Daftar Buku Kosong")
                break
            while True:
                semuaBuku()
                namaBuku = input('Masukkan Judul Buku Yang Ingin ditambahkan: ').capitalize()

                if any(buku['judul'].capitalize() == namaBuku for buku in listBuku):
                    print('Judul buku yang Anda masukkan sudah tersedia.')
                else:
                    hargaBuku = input('Masukkan Harga Sewa Buku Per Minggu: ')
                    while not hargaBuku.isdigit() or int(hargaBuku) < 5000:
                        print('Harga harus berupa angka dan minimal 5000. Coba lagi.')
                        hargaBuku = input('Masukkan Harga Sewa Buku Per Minggu: ')

                    tahunBuku = input('Masukkan Tahun Buku Di Rilis: ')
                    while not tahunBuku.isdigit() or int(tahunBuku) < 1990:
                        print('Tahun harus berupa angka dan minimal 1990. Coba lagi.')
                        tahunBuku = input('Masukkan Tahun Buku Di Rilis: ')

                    penulisBuku = input('Masukkan Nama Penulis Buku: ')
                    kategoriBuku = input('Masukan Kategori Buku: ')
                    bahasaBuku = input('Masukan Bahasa Buku: ')

                    create2 = input('Apakah Anda ingin menyimpan data tersebut di perpustakaan? (ya/tidak): ')

                    if create2.lower() == 'tidak':
                        print('Data Tersebut Tidak Tersimpan.')
                    elif create2.lower() == 'ya':
                        buku = {
                            'judul': namaBuku,
                            'kategori': kategoriBuku,
                            'harga': int(hargaBuku),
                            'tahun': int(tahunBuku),
                            'penulis': penulisBuku,
                            'bahasa': bahasaBuku
                        }
                        listBuku.append(buku)
                        print('Buku Berhasil Ditambahkan\n')
                        semuaBuku()
                    break
        elif create1 == '2':
            pustakawan()
            break
        else:
            print('Pilihan Tidak Ada. Silakan Pilih 1 atau 2.')


# fitur update 
from prettytable import PrettyTable

def updateDataBuku():
    while True:
        update1 = input('''
            +++++++ Menu Update Data Barang ++++++++

            List Menu :
            1. Update Data Buku
            2. Kembali Ke Menu Utama

            Silahkan Pilih Angka Yang Ingin DiJalankan: ''')

        if update1 == '1':
            if len(listBuku) == 0:
                print("Daftar Buku Kosong")
                break
            while True:
                semuaBuku()
                indexBuku = input('Masukkan Index Buku yang Ingin Diupdate: ')
                
                if not indexBuku.isdigit():
                    print("Input harus berupa angka. Silakan masukkan angka index yang valid.")
                    continue

                indexBuku = int(indexBuku)
                if indexBuku in range(len(listBuku)):
                    buku = listBuku[indexBuku]
                    table = PrettyTable()
                    table.field_names = ["Index", "Harga", "Judul", "Kategori", "Tahun", "Penulis", "Bahasa"]
                    table.add_row([indexBuku, buku["harga"], buku["judul"], buku["kategori"], buku["tahun"], buku["penulis"], buku["bahasa"]])
                    print(table)
                    break
                else:
                    print(f'Buku Dengan Index {indexBuku} Tidak Ada. Silakan masukkan index yang valid.')
                    continue  # Lanjutkan ke iterasi berikutnya

            while True:
                update2 = input('Apakah Anda Ingin Mengubah Data Buku Ini? (ya/tidak): ')
                if update2.lower() == 'ya':
                    temp_changes = {}  #dictionary sementara untuk menampung update data

                    kolomBuku = input('Masukkan Kolom Buku yang Ingin Diubah: ').lower()
                    if kolomBuku == 'judul':
                        temp_changes['judul'] = input('Masukkan Judul Baru: ').capitalize()
                    elif kolomBuku == 'kategori':
                        temp_changes['kategori'] = input('Masukkan Kategori Baru: ').capitalize()
                    elif kolomBuku == 'harga':
                        hargaBuku = input('Masukkan Harga Baru: ')
                        while not hargaBuku.isdigit() or int(hargaBuku) < 5000:
                            print('Harga harus berupa angka dan minimal 5000. Coba lagi.')
                            hargaBuku = input('Masukkan Harga Baru: ')
                        temp_changes['harga'] = int(hargaBuku)
                    elif kolomBuku == 'tahun':
                        tahunBuku = input('Masukkan Tahun Baru: ')
                        while not tahunBuku.isdigit() or int(tahunBuku) < 1990:
                            print('Tahun harus berupa angka dan minimal 1990. Coba lagi.')
                            tahunBuku = input('Masukkan Tahun Baru: ')
                        temp_changes['tahun'] = int(tahunBuku)
                    elif kolomBuku == 'penulis':
                        temp_changes['penulis'] = input('Masukkan Penulis Baru: ').capitalize()
                    elif kolomBuku == 'bahasa':
                        temp_changes['bahasa'] = input('Masukkan Bahasa Baru: ').capitalize()
                    else:
                        print('Kolom Buku Tidak Valid')
                        continue

                    update3 = input('Apakah Anda Yakin Ingin Mengupdate Data Buku Ini? (ya/tidak): ')
                    if update3.lower() == 'ya':
                        buku.update(temp_changes)  # Update hanya ketika user memasukan input 'ya'
                        print('Update Data Buku Berhasil.\n')
                        semuaBuku()
                        break
                    elif update3.lower() == 'tidak':
                        print('Data Buku Tidak di Update')
                        break
                    else :
                        print ('Input harus diisi dengan  "ya" atau "tidak". Silakan coba lagi.')
                    
                elif update2.lower() == 'tidak':
                    break
                else:
                    print('Pilihan Tidak Ada, Silahkan Pilih Menu Yang Tersedia')

        elif update1 == '2':
            pustakawan()
            break

        else:
            print('Pilihan Tidak Ada, Silahkan Pilih Menu Yang Tersedia')


# fitur Delete
def hapusBuku():
    while True:
        delete1 = input('''
            +++++++ Menu Hapus Buku ++++++++

            List Menu:
            1. Hapus Buku
            2. Kembali Ke Menu Utama

            Silahkan Pilih Angka Yang Ingin DiJalankan: ''')

        if delete1 == '1':
            if len(listBuku) == 0:
                print('Daftar Buku Kosong')
                break
            # Menampilkan daftar buku
            else:
                semuaBuku()
            while True:
                try: # untuk menangani kemungkinan kesalahan pada input pengguna.
                    delete2 = int(input('Masukkan Index Buku Yang Ingin Dihapus : '))
                    if delete2 < 0 or delete2 >= len(listBuku):
                        print(f'Buku Dengan Nomor Index {delete2} Tidak Ada. Silakan masukkan index yang valid.')
                        continue
                    else:
                        lanjutHapus = input('Apakah Anda Yakin Ingin Menghapus Buku Tersebut ? (ya/tidak): ')
                        if lanjutHapus.lower() == 'ya':
                            del listBuku[delete2]
                            print(f'Buku Dengan Nomor Index {delete2} Berhasil Dihapus.')
                            break
                        elif lanjutHapus.lower() == 'tidak':
                            break
                        else:
                            print('Input harus diisi dengan "ya" atau "tidak". Silakan coba lagi.')
                            continue
                except ValueError:
                    print('Input harus berupa angka. Silakan masukkan angka index yang valid.')
        elif delete1 == '2':
            pustakawan()
            break
        else:
            print('Pilihan Tidak Ada. Silakan Pilih 1 atau 2.')


# Menu keranjang buku
def keranjang() :
    while True :
        keranjang= input('''
            ++++++++++ Keranjang Buku ++++++++++

                List Menu :
                1. Melihat Keranjang Buku
                2. Menghapus Buku Di Keranjang
                3. Membayar Sewa Buku
                4. Kembali Ke Menu Utama

                Silahkan Pilih Menu Yang Ingin Di Jalankan : ''')
        if(keranjang == '1') :
            lihatKeranjang()
        elif(keranjang == '2') :
            hapusKeranjang()
        elif(keranjang == '3') :
            bayar()
        elif(keranjang == '4') :
            break
        else :
            print('Pilihan Tidak Ada, Masukkan Pilihan (1-4)')

#fitur create
def pinjamBuku():
    while True:
        if len(listBuku) == 0:
            print('Data Buku Kosong')
            break

        while True:
            semuaBuku()
            indexBuku = int(input('Masukkan Index Buku Yang Ingin Di Sewa : '))
            if indexBuku in range(len(listBuku)):
                buku = listBuku[indexBuku]
                print(f'Buku dengan Index {indexBuku}\n')
                print('Index \t| Harga \t| Judul \t\t\t| Kategori \t| Tahun \t| Penulis \t\t| Bahasa\n')
                print(f'{indexBuku} \t| {buku["harga"]:<7} \t| {buku["judul"]:<25} \t| {buku["kategori"]:<12} \t| {buku["tahun"]:<6} \t| {buku["penulis"]:<18} \t| {buku["bahasa"]}')
                cart.append(buku)
                print('Buku Sudah Ditambahkan Ke Keranjang')
                # Hapus buku dari listBuku berdasarkan index
                listBuku.pop(indexBuku)
                break
            else:
                print(f'Buku Dengan Nomor Index {indexBuku} Tidak Ada. Silakan masukkan index yang valid.')

        while True:
            tanya1 = input('Apakah Anda Ingin Meminjam Buku Ini? (ya/tidak): ')
            if tanya1.lower() == 'tidak':
                pengunjung()
                break
            elif tanya1.lower() == 'ya':
                while True:
                    tanya2 = input('Apakah Ada Buku Lain Yang Ingin Anda Pinjam? (ya/tidak): ')
                    if tanya2.lower() == 'tidak':
                        print('Terima kasih sudah meminjam buku!\nSilahkan Membayar Uang Sewa Buku')
                        bayar()
                        return
                    elif tanya2.lower() == 'ya':
                        break
                    else:
                        print('Pilihan Tidak Ada. Silakan masukkan "ya" atau "tidak"')
            else:
                print('Pilihan Tidak Ada. Silakan masukkan "ya" atau "tidak"')




#fitur read
#melihat Keranjang
def lihatKeranjang():
    if len(cart) == 0:
        print('Keranjang Anda Kosong')
    else:
        print('++++++++++ Selamat Datang Di Keranjang Anda ++++++++++ \n')
        table = PrettyTable()
        table.field_names = ["Index", "Harga", "Judul", "Kategori", "Tahun", "Penulis", "Bahasa"]
        
        for i in range(len(cart)):
            buku = cart[i]
            table.add_row([i, buku["harga"], buku["judul"], buku["kategori"], buku["tahun"], buku["penulis"], buku["bahasa"]])

        print(table)


#Fitur Delete
# Menghapus Buku Pada Keranjang Buku
def hapusKeranjang():
    while True:
        delete1 = input('''
            +++++++ Menu Hapus Buku ++++++++

            List Menu:
            1. Hapus Buku Dari Keranjang
            2. Kembali Ke Menu Utama

            Silahkan Pilih Angka Yang Ingin DiJalankan: ''')

        if delete1 == '1':
            if len(cart) == 0:
                print('Keranjang Anda Kosong')
                break
            delete2 = int(input('Masukkan Index Buku Yang Ingin Dihapus Dari Keranjang : '))
            if(delete2 > len(cart)-1):
                print(f'Buku Dengan Nomor Index {delete2} Tidak Ada Di Keranjang.')
                continue
            elif (delete2 < len(cart)):
                lanjutHapus = input('Apakah Anda Yakin Ingin Menghapus Buku Ini Dari Keranjang ? (ya/tidak): ')
                if(lanjutHapus.lower()== 'ya'):
                    del cart[delete2]
                    print(f'Buku Dengan Nomor Index {delete2} Berhasil Dihapus Dari Keranjang.')
                    break
                elif(lanjutHapus.lower()== 'tidak'):
                    continue
        elif(delete2 =='2'):
          pengunjung()
          break

#fitur update untuk membayar uang sewa buku 
def bayar():
    if len(cart) == 0:
        print('Keranjang Anda Kosong')
        return  # Keluar dari fungsi jika keranjang kosong
    
    print('Keranjang Anda : \n')
    
    totalHargaSewa = sum(buku['harga'] for buku in cart)  # Menghitung total harga sewa
    
    while True:
        print('Total Yang Harus Dibayar = {}'.format(totalHargaSewa))
        jumlahUang = int(input('Masukkan jumlah uang : '))
        
        if jumlahUang > totalHargaSewa:
            kembali = jumlahUang - totalHargaSewa
            print('Terima kasih \n\nUang kembali anda : {}\n'.format(kembali))
            tanggalPengembalian()
            for buku in cart:
                listBuku[buku] -= 1  # Mengurangkan stok buku yang disewa
            
            cart.clear()
            break
        elif jumlahUang == totalHargaSewa:
            cart.clear()
            tanggalPengembalian()
            break
        else:
            kekurangan = totalHargaSewa - jumlahUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))


from datetime import datetime, timedelta
#fitur untuk mengetahui tanggal pengembalian buku
def tanggalPengembalian():
    while True:
        # Input tanggal hari ini dari pengguna dengan format "DD-MM-YYYY"
        hariIni = input("Masukkan tanggal hari ini (format DD-MM-YYYY): ")

        # Validasi format tanggal
        try:
            hariIni = datetime.strptime(hariIni, '%d-%m-%Y')
            break  # Keluar dari loop jika format tanggal benar
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")

    # Hitung tanggal pengembalian (7 hari setelah tanggal peminjaman)
    tanggal_pengembalian = hariIni + timedelta(days=7)

    # Format tanggal pengembalian ke dalam string (DD-MM-YYYY)
    tanggal_pengembalian_str = tanggal_pengembalian.strftime('%d-%m-%Y')

    print(f'Tanggal Pengembalian Buku: {tanggal_pengembalian_str}')
    print('Terimakasih Sudah Berkunjung\nSemoga Hari Anda Menyenangkan\n')
    return tanggal_pengembalian_str


menuAwal()
       


                
    



