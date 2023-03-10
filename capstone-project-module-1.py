stokgudang = {'kalung':15, 'gelang':10, 'cincin':20}

def tampilkan_stok():
    while True:
        print('''
        \t TAMPILKAN STOK GUDANG\n
        1 - Tampilkan seluruh stok gudang
        2 - Tampilkan stok item tertentu
        3 - Kembali ke menu utama
        ''')
        input_menu = int(input('Masukkan nomor menu ... '))
        if input_menu == 1:
            print('''
            \t   DAFTAR STOK GUDANG PERHIASAN\n
            \tITEM\t\tQUANTITY
            ''')
            for key, val in stokgudang.items():
                print('''\t\t{}\t\t{}'''.format(key.capitalize(), val))
            continue
        elif input_menu == 2:
            input_item = input('Masukkan nama item yang dicari ... ').lower()
            if input_item in stokgudang:
                print('''
                ITEM\t\tQUANTITY
                ''')
                print('''\t\t{}\t\t{}\n'''.format(input_item.capitalize(), stokgudang[input_item]))
                continue
            else:
                print('Item tidak ditemukan.')
                continue
        elif input_menu == 3:
            menu_utama()
        else:
            print('Menu tidak ditemukan.')
            continue

def tambah_stok():
    while True:
        print('''
        \tTAMBAH DATA STOK\n
        1 - Tambah data stok
        2 - Kembali ke menu utama
        ''')
        input_menu = int(input('Masukkan nomor menu ... '))
        if input_menu == 1:
            input_item = input('Masukkan nama item yang ingin ditambahkan ... ').lower()
            if input_item in stokgudang:
                print('Data sudah ada.')
                continue
            else:
                input_qty = int(input('Masukkan quantity item ... '))
                stokgudang[input_item] = input_qty
                print('Item sudah tersimpan.')
                continue
        elif input_menu == 2:
            menu_utama()
        else:
            print('Menu tidak ditemukan.')
            continue

def update_stok():
    while True:
        print('''
        \tUPDATE DATA STOK\n
        1 - Update data stok
        2 - Kembali ke menu utama
        ''')
        input_menu = int(input('Masukkan nomor menu ... '))
        if input_menu == 1:
            input_item = input('Masukkan nama item yang ingin di-update ... ').lower()
            if input_item in stokgudang:
                input_qty = int(input('Masukkan quantity item yang baru ... '))
                stokgudang[input_item] = input_qty
                print('Data {} berhasil di-update.'.format(input_item))
            else:
                print('Item tidak ditemukan.')
                continue
        elif input_menu == 2:
            menu_utama()
        else:
            print('Menu tidak ditemukan.')
            continue

def hapus_stok():
    while True:
        print('''
        \tHAPUS DATA STOK\n
        1 - Hapus data stok
        2 - Kembali ke menu utama
        ''')
        input_menu = int(input('Masukkan nomor menu ... '))
        if input_menu == 1:
            input_item = input('Masukkan nama item yang ingin dihapus ... ').lower()
            if input_item in stokgudang:
                input_hapus = (input('''Yakin ingin menghapus data {}? [Y]es/[N]o '''.format(input_item))).upper()
                if input_hapus == 'Y':
                    del stokgudang[input_item]
                    print('Data {} berhasil dihapus.'.format(input_item))
                elif input_hapus == 'N':
                    print('Item gagal dihapus.')
                    continue
                else:
                    print('Input Anda tidak valid.')
                    continue
            else:
                print('Item tidak ditemukan.')
                continue
        elif input_menu == 2:
            menu_utama()
        else:
            print('Menu tidak ditemukan.')
            continue

def menu_utama():
    while True:
        print('''
        \tMENU UTAMA STOK GUDANG PERHIASAN\n
        1 - Tampilkan stok gudang 
        2 - Tambah data stok
        3 - Update data stok
        4 - Hapus data stok
        5 - Exit
        ''')
        input_menu = int(input('Masukkan nomor menu ... '))
        if input_menu == 1:
            tampilkan_stok()
        elif input_menu == 2:
            tambah_stok()
        elif input_menu == 3:
            update_stok()
        elif input_menu == 4:
            hapus_stok()
        elif input_menu == 5:
            exit()
        else:
            print('Menu tidak ditemukan.')
            continue

print(menu_utama())
