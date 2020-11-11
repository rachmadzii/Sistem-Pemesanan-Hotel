# Import waktu dan tanggal lokal komputer
from time import localtime

# Kode Data Penginapan untuk Single Linked List dan Queue
class DataPenginapan:
    no_regist = str
    nik = str
    nama = str
    no_telp = str
    check_in = list
    check_out = list
    biaya = int
    jenis = str
    no_kamar = str

# Kode Elemen untuk Single Linked List
class Elemen:
    def __init__(self):
        self.kontainer = DataPenginapan()
        self.next = None

    def getKontainer(self):
        return self.kontainer

    def setNext(self, nextt):
        self.next = nextt

    def getNext(self):
        return self.next

# Kode Struktur Data Single Linked List
class List:
    def __init__(self):
        self.first = None
        self.data = []

        for i in range(0,20):
            self.data.append([])
            self.data[i] = Elemen()

    def setFirst(self, first):
        self.first = first

    def getFirst(self):
        return self.first

    def createList(self):
        self.first = -1
        for i in range(0, len(self.data)):
            self.data[i].setNext(-2)

    def countElemen(self):
        hasil = 0
        if(self.first != -1):
            bantu = self.first

            while bantu != -1:
                hasil = hasil + 1
                bantu = self.data[bantu].getNext()
        return hasil

    def emptyElemen(self):
        hasil = -1

        if(self.countElemen() < len(self.data)):
            ketemu = False
            i = 0
            
            while(ketemu == False) and (i < len(self.data)):
                if(self.data[i].getNext() == -2):
                    hasil = i
                    ketemu = True
                else:
                    i = i+1
        return hasil

    def addFirst(self, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar):
        if(self.countElemen() < len(self.data)):
            baru = self.emptyElemen()
            
            self.data[baru].getKontainer().no_regist = no_regist
            self.data[baru].getKontainer().nik = nik
            self.data[baru].getKontainer().nama = nama
            self.data[baru].getKontainer().no_telp = no_telp
            self.data[baru].getKontainer().check_in = check_in
            self.data[baru].getKontainer().check_out = check_out
            self.data[baru].getKontainer().biaya = biaya
            self.data[baru].getKontainer().jenis = jenis
            self.data[baru].getKontainer().no_kamar = no_kamar

            if(self.first == -1):
                self.data[baru].setNext(-1)
            else:
                self.data[baru].setNext(self.first)
            self.first = baru
        else:
            print("[!] List sudah tidak dapat ditambah")

    def addAfter(self, prev, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar):
        if((self.countElemen() < len(self.data)) and (prev != -1)):
            baru = self.emptyElemen()
            self.data[baru].getKontainer().no_regist = no_regist
            self.data[baru].getKontainer().nik = nik
            self.data[baru].getKontainer().nama = nama
            self.data[baru].getKontainer().no_telp = no_telp
            self.data[baru].getKontainer().check_in = check_in
            self.data[baru].getKontainer().check_out = check_out
            self.data[baru].getKontainer().biaya = biaya
            self.data[baru].getKontainer().jenis = jenis
            self.data[baru].getKontainer().no_kamar = no_kamar

            if(self.data[prev].getNext() == -1):
                self.data[baru].setNext(-1)
            else:
                self.data[baru].setNext(self.data[prev].getNext())

            self.data[prev].setNext(baru)
        else:
            print("[!] List sudah tidak dapat ditambah")

    def add(self, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar):
        if self.countElemen() == 0:
            self.addFirst(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
        else:
            index = self.getFirst()
            prev = self.getFirst()
            for i in range(self.countElemen()):
                if self.data[index].getKontainer().no_regist > no_regist:
                    if index == self.getFirst():
                        self.addFirst(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                    else:
                        self.addAfter(prev, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                    break
                else:
                    if self.countElemen() == (i+1):
                        self.addAfter(index, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                        break
                    else:
                        prev = index
                        index = self.data[prev].getNext()

    def delFirst(self):
        if(self.first != -1):
            hapus = self.first

            if(self.countElemen() == 1):
                self.first = -1
            else:
                self.first = self.data[self.first].getNext()
            self.data[hapus].setNext(-2)
        else:
            print("[!] List kosong")

    def delAfter(self, prev):
        if(prev != -1):
            hapus = self.data[prev].getNext()
            if(hapus != -1):
                if(self.data[hapus].getNext() == -1):
                    self.data[prev].setNext(-1)
                else:
                    self.data[prev].setNext(self.data[hapus].getNext())

                self.data[hapus].setNext(-2)

    def delete(self, no_co):
        if(self.first != -1):
            if self.countElemen() == 1:
                self.delFirst()
            else:
                bantu = self.first
                prev = self.first

                while bantu != -1:
                    if self.data[self.first].getKontainer().no_kamar == no_co:
                        self.delFirst()
                        break
                    elif self.data[bantu].getKontainer().no_kamar == no_co:
                        self.delAfter(prev)
                        break
                    
                    prev = bantu
                    bantu = self.data[bantu].getNext()

    def printElement(self):
        if(self.first != -1):
            bantu = self.first
            i = 1

            while bantu != -1:
                print("> Data ke -", i)
                print("  No. Registrasi     : ", self.data[bantu].getKontainer().no_regist)
                print("  NIK                : ", self.data[bantu].getKontainer().nik)
                print("  Nama Lengkap       : ", self.data[bantu].getKontainer().nama)
                print("  No. Telepon        : ", self.data[bantu].getKontainer().no_telp)
                print("  Tanggal Check In   : ", "/".join(self.data[bantu].getKontainer().check_in))
                print("  Tanggal Check Out  : ", "/".join(self.data[bantu].getKontainer().check_out))
                print("  Nomor Kamar        : ", self.data[bantu].getKontainer().no_kamar)
                print("  Total Biaya        :  Rp.", self.data[bantu].getKontainer().biaya)
                print('--------------------------------------------------')
                bantu = self.data[bantu].getNext()
                i = i+1
        else:
            print("[!] Tidak ada data")

    def search(self, n): 
        for i in range(self.countElemen()):
            if self.data[i].getKontainer().no_regist == n:
                print('\n[!] Data berhasil ditemukan\n')
                print('-----------------------------------------------------')
                print("No. Registrasi     : ", self.data[i].getKontainer().no_regist)
                print("NIK                : ", self.data[i].getKontainer().nik)
                print("Nama Lengkap       : ", self.data[i].getKontainer().nama)
                print("No. Telepon        : ", self.data[i].getKontainer().no_telp)
                print("Tanggal Check In   : ", "/".join(self.data[i].getKontainer().check_in))
                print("Tanggal Check Out  : ", "/".join(self.data[i].getKontainer().check_out))
                print("Jenis Kamar        : ", self.data[i].getKontainer().jenis)
                print("Nomor Kamar        : ", self.data[i].getKontainer().no_kamar)
                print("Total Biaya        :  Rp.", self.data[i].getKontainer().biaya)
                print('-----------------------------------------------------')
        
# Kode Struktur Data Binary Seacrh Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, id):
        current = self.root
        if current == None:
            return False   
        else:
            while(current!=None):
                if(current.data==id):
                    return True
                elif(current.data>id):
                    current = current.left
                else:
                    current = current.right
            return False

    def delete(self, id):
        parent = self.root
        current = self.root
        isLeftChild = False

        while(current.data != id):
            parent = current
            if(current.data>id):
                isLeftChild = True
                current = current.left
            else:
                isLeftChild = False
                current = current.right
            if(current == None):
                return False

        if(current.left == None and current.right == None):
            if(current == self.root):
                self.root = None
            if(isLeftChild == True):
                parent.left = None
            else:
                parent.right = None
        elif(current.right == None):
            if(current == self.root):
                self.root = current.left
            elif(isLeftChild):
                parent.left = current.left
            else:
                parent.right = current.left
        elif(current.left == None):
            if(current == self.root):
                self.root = current.right
            elif(isLeftChild):
                parent.left = current.right
            else:
                parent.right = current.right
        elif(current.left != None and current.right != None):
            successor = self.getSuccessor(current)
            if(current == self.root):
                self.root = successor
            elif(isLeftChild):
                parent.left = successor
            else:
                parent.right = successor
            successor.left = current.left
        return True
        
    def getSuccessor(self, deleteNode):
        successor = None
        successorParent = None
        current = deleteNode.right
        while(current!=None):
            successorParent = successor
            successor = current
            current = current.left

        if(successor!=deleteNode.right):
            successorParent.left = successor.right
            successor.right = deleteNode.right

        return successor

    def insert(self, id):
        newNode = Node(id)
        if(self.root == None):
            self.root = newNode
            return
        current = self.root
        parent = None
        while(True):
            parent = current
            if(id<current.data):
                current = current.left
                if(current == None):
                    print
                    parent.left = newNode
                    return
            else:
                current = current.right
                if(current == None):
                    parent.right = newNode
                    return

    def display(self, root):
        if(root != None):
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)

# Kode Struktur Data Queue
class Queue:
    def __init__(self): # construktor
        self.first = None
        self.last = None
        self.DataPenginapan = []
      
    def createEmpty(self):
        self.first = -1
        self.last = -1
        
    def isEmpty(self):
        hasil = False
        if(self.first == -1):
            hasil = True
        return hasil
    
    def add(self, no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar):
        if(self.isEmpty() == True):
            self.last = 0
            self.first = 0
            self.nomor = 1
            self.DataPenginapan.append(DataPenginapan())
            self.DataPenginapan[0].no_regist = no_regist
            self.DataPenginapan[0].nik = nik
            self.DataPenginapan[0].nama = nama
            self.DataPenginapan[0].no_telp = no_telp
            self.DataPenginapan[0].check_in = check_in
            self.DataPenginapan[0].check_out = check_out
            self.DataPenginapan[0].biaya = biaya
            self.DataPenginapan[0].jenis = jenis
            self.DataPenginapan[0].no_kamar = no_kamar
        else:
            self.last += 1
            self.nomor += 1
            self.DataPenginapan.append(DataPenginapan())
            self.DataPenginapan[self.last].no_regist = no_regist
            self.DataPenginapan[self.last].nik = nik
            self.DataPenginapan[self.last].nama = nama
            self.DataPenginapan[self.last].no_telp = no_telp
            self.DataPenginapan[self.last].check_in = check_in
            self.DataPenginapan[self.last].check_out = check_out
            self.DataPenginapan[self.last].biaya = biaya
            self.DataPenginapan[self.last].jenis = jenis
            self.DataPenginapan[self.last].no_kamar = no_kamar
    
    def delete(self):
        if(self.last == 0):
            self.first = -1
            self.last = -1
        else:
            for i in range(self.first+1, self.last+1):
                self.DataPenginapan[i-1].no_regist = self.DataPenginapan[i].no_regist
                self.DataPenginapan[i-1].nik = self.DataPenginapan[i].nik
                self.DataPenginapan[i-1].nama = self.DataPenginapan[i].nama
                self.DataPenginapan[i-1].no_telp = self.DataPenginapan[i].no_telp
                self.DataPenginapan[i-1].check_in = self.DataPenginapan[i].check_in
                self.DataPenginapan[i-1].check_out = self.DataPenginapan[i].check_out
                self.DataPenginapan[i-1].biaya = self.DataPenginapan[i].biaya
                self.DataPenginapan[i-1].jenis = self.DataPenginapan[i].jenis
                self.DataPenginapan[i-1].no_kamar = self.DataPenginapan[i].no_kamar
            self.last = self.last-1

    def printData(self):
        if(self.first != -1):
            for i in range(self.last, (self.first-1), -1):
                print("> Data ke -", i+1)
                print("  No. Registrasi     : ", self.DataPenginapan[i].no_regist)
                print("  NIK                : ", self.DataPenginapan[i].nik)
                print("  Nama Lengkap       : ", self.DataPenginapan[i].nama)
                print("  No. Telepon        : ", self.DataPenginapan[i].no_telp)
                print("  Tanggal Check In   : ", "/".join(self.DataPenginapan[i].check_in))
                print("  Tanggal Check Out  : ", "/".join(self.DataPenginapan[i].check_out))
                print("  Nomor Kamar        : ", self.DataPenginapan[i].no_kamar)
                print("  Total Biaya        :  Rp.", self.DataPenginapan[i].biaya)
            print('--------------------------------------------------')  
        else:
            print('[!] Tidak ada data penginapan check out')
            print('--------------------------------------------------')

# Fungsi untuk mengecek validasi data
def validasiData(no_regist, nik, no_telp, check_in, check_out):
    try:
        hasil = True
        pesanError = ""

        # Mengecek validasi No. Regist
        if no_regist == '':
            raise ValueError("[!] No. Registrasi yang dimasukan tidak valid")
        elif no_regist.isalpha():
            raise ValueError("[!] No. Registrasi yang dimasukan tidak valid")

        # Mengecek validasi NIK
        if nik.isalpha():
            raise ValueError("[!] NIK yang dimasukan tidak valid")
        elif len(nik) != 16:
            raise ValueError("[!] NIK harus terdiri dari 16 angka")

        # Mengecek validasi No. Telp
        if no_telp.isalpha():
            raise ValueError("[!] No. Telepon yang anda masukan tidak valid")
        elif len(no_telp) < 10 or len(no_telp) > 13:
            raise ValueError("[!] No. Telepon harus terdiri dari 10 atau s.d 13 angka") 
        
        # Mengecek validasi tanggal check in
        if len(check_in) != 3:
            raise ValueError("[!] Format tanggal yang dimasukan salah")
        elif len(check_in) == 3:
            if check_in[0].isalpha() or check_in[1].isalpha() or check_in[2].isalpha():
                raise ValueError("[!] Format tanggal yang dimasukan salah")
            elif int(check_in[0]) < 1 or int(check_in[0]) > 31:
                raise ValueError("[!] Hari yang dimasukan di luar jangkauan")
            elif int(check_in[1]) < 1 or int(check_in[1]) > 12:
                raise ValueError("[!] Bulan yang dimasukan di luar jangkauan")
            elif int(check_in[2]) < localtime().tm_year or int(check_in[2]) > localtime().tm_year+1:
                raise ValueError("[!] Tahun yang dimasukan di luar jangkauan")

        # Mengecek validasi tanggal check out
        if len(check_out) != 3:
            raise ValueError("[!] Format tanggal yang dimasukan salah")
        elif len(check_out) == 3:
            if check_out[0].isalpha() or check_out[1].isalpha() or check_out[2].isalpha():
                raise ValueError("[!] Format tanggal yang dimasukan salah")
            elif int(check_out[0]) < 1 or int(check_out[0]) > 31:
                raise ValueError("[!] Hari yang dimasukan di luar jangkauan")
            elif int(check_out[1]) < 1 or int(check_out[1]) > 12:
                raise ValueError("[!] Bulan yang dimasukan di luar jangkauan")
            elif int(check_out[2]) < localtime().tm_year or int(check_out[2]) > localtime().tm_year+1:
                raise ValueError("[!] Tahun yang dimasukan di luar jangkauan")
            
    # Masuk jika ada error
    except ValueError as VE:
        hasil = False
        pesanError = VE
    finally:
        return hasil, pesanError

# Fungsi untuk mengecek validasi nomor regist atau dan nomor kamar
def validasiNomor(*isi): # Menggunakan *args
    hasil = True
    pesanError = ""

    # Jika hanya satu variabel yang masuk ke fungsi
    if len(isi) == 1:
        try:
            # Mengecek validasi No. Regist atau No. Kamar
            if isi[0] == '':
                raise ValueError("[!] Nomor yang dimasukan tidak valid")
            elif isi[0].isalpha():
                raise ValueError("[!] Nomor yang dimasukan tidak valid")
        
        # Masuk jika ada error
        except ValueError as VE:
            hasil = False
            pesanError = VE
        finally:
            return hasil, pesanError

    # Jika dua variabel yang masuk ke fungsi
    elif len(isi) == 2:
        try:
            # Mengecek validasi No. Regist
            if isi[0] == '':
                raise ValueError("[!] Nomor yang dimasukan tidak valid")
            elif isi[0].isalpha():
                raise ValueError("[!] Nomor yang dimasukan tidak valid")
            
            # Mengecek validasi No. Kamar
            if isi[1] == '':
                raise ValueError("[!] Nomor yang dimasukan tidak valid")
            elif isi[1].isalpha():
                raise ValueError("[!] Nomor yang dimasukan tidak valid")

        # Masuk jika ada error
        except ValueError as VE:
            hasil = False
            pesanError = VE
        finally:
            return hasil, pesanError

# Fungsi untuk menghitung total harga penginapan berdasarkan jumlah hari
def hitungTotal(hari_in, hari_out, bulan_in, bulan_out, harga):
    # Jika bulan check in yaitu Februari
    if bulan_in == 2:
        set_hari = 29
        hari     = set_hari - hari_in + hari_out
        biaya    = harga * hari
    # Jika bulan check in yaitu April, Juni, September, November
    elif bulan_in == 4 or bulan_in == 6 or bulan_in == 9 or bulan_in == 11:
        set_hari = 30
        hari     = set_hari - hari_in + hari_out
        biaya    = harga * hari
    # Jika bulan check in yaitu Januari, Maret, Mei, Juli, Agustus, Oktober, Desember
    elif bulan_in == 1 or bulan_in == 3 or bulan_in == 5 or bulan_in == 7 or bulan_in == 8 or bulan_in == 10 or bulan_in == 12:
        set_hari = 31
        hari     = set_hari - hari_in + hari_out
        biaya    = harga * hari
    return biaya

# MAIN CODE
if __name__ == '__main__':
    import os

    # Inisialisasi objek BST, SLL, dan Queue
    Regist   = BinarySearchTree() # BST untuk nomor registrasi
    Sgl      = BinarySearchTree() # BST untuk nomor single room
    Dbl      = BinarySearchTree() # BST untuk nomor double room
    Data_Sgl = List() # SLL untuk data penginapan di single room
    Data_Dbl = List() # SLL untuk data penginapan di double room  
    Sgl_Out  = Queue() # Queue untuk data penginapan check out pada single room
    Dbl_Out  = Queue() # Queue untuk data penginapan check out pada double room

    clsscr = lambda: os.system('cls') # clear screen

    # Menambahkan nomor kamar 1 s.d 20 ke BST single dan double room
    for i in range(0,20):
        no = i+1
        Sgl.insert(no)
        Dbl.insert(no)
    
    clsscr()
    # Halaman utama -> Login user dan password untuk admin
    print('======================================')
    print('     SISTEM PEMESANAN KAMAR HOTEL     ')
    print('======================================')
    print('        Masuk ke Sistem Hotel         ')
    print('--------------------------------------')
    while True:
        verif_user = input('User      :  ')
        verif_pass = input('Password  :  ')
        # Validasi user dan password sebagai 'Admin'
        if verif_user == 'Admin' and verif_pass == '123':
            break
        else:
            print('[!] Username atau Password salah!\n')

    # Membuat SLL untuk data pemesanan single room dan double room
    Data_Sgl.createList()
    Data_Dbl.createList()  
    # Membuat Queue untuk data check out single room dan double room
    Sgl_Out.createEmpty()
    Dbl_Out.createEmpty()
    
    # Pilihan menu program
    while True:
        clsscr()
        print('Selamat Datang', verif_user)
        print('=================================')
        print('          MENU PROGRAM           ')
        print('---------------------------------')
        print('1. |  Registrasi Pemesanan       ')
        print('2. |  No. Kamar yang Tersedia    ')
        print('3. |  Lihat Data Penginapan      ')
        print('4. |  Cari Data Penginapan       ')
        print('5. |  Check Out Penginapan       ')
        print('6. |  Lihat Data Check Out       ')
        print('7. |  Keluar Menu                ')
        print('=================================')
        pilih = input('Pilih menu [1..7] > ')

        # Pilihan 1 -> Registrasi pemesanan kamar baru
        if pilih == '1':
            clsscr()
            repeat = True
            while repeat:
                clsscr()
                print('============================================================')
                print('                    REGISTRASI PEMESANAN                    ')
                print('------------------------------------------------------------')
                no_regist   = input('Masukkan No. Registrasi     : ')
                nik         = input('Masukkan NIK                : ')
                nama        = input('Masukkan Nama Lengkap       : ')
                no_telp     = input('Masukkan No. Telepon        : ')
                print('\n- Format tanggal DD/MM/YYYY -')
                check_in    = input('Masukkan Tanggal Check In   : ').split('/')
                check_out   = input('Masukkan Tanggal Check Out  : ').split('/')
                print('============================================================')
                
                # Mengecek validasi data yang dimasukan
                valid, pesanError = validasiData(no_regist, nik, no_telp, check_in, check_out)
                
                if valid:
                    regist = int(no_regist)
                    # Mengecek apakah nomor regist yang dimasukan sudah tersedia atau belum
                    # Jika belum tersedia akan masuk ke if di bawah
                    if Regist.find(regist) == False:
                        tanggal = True
                        input('Tekan ENTER untuk beralih ke halaman pilihan jenis kamar... ')
                        # Inisialisasi data hari, bulan, tahun dari tanggal check in dan check out
                        hari_in   = int(check_in[0])
                        bulan_in  = int(check_in[1])
                        tahun_in  = int(check_in[2])
                        hari_out  = int(check_out[0])
                        bulan_out = int(check_out[1])
                        tahun_out = int(check_out[2])
                        
                        # Mengecek tahun check in dan tahun check out
                        # Kemudian mengecek apakah hari dan bulan check in dan check out sudah terlewat?
                        # Jika sudah terlewat, tanggal akan diinisialisasi 'False'
                        if tahun_in == localtime().tm_year and tahun_out == localtime().tm_year:
                            if bulan_in < localtime().tm_mon or hari_in < localtime().tm_mday:
                                tanggal = False
                            elif bulan_out < localtime().tm_mon or hari_out < localtime().tm_mday:
                                tanggal = False
                            elif bulan_out == bulan_in and hari_out < hari_in:
                                tanggal = False
                        elif tahun_in == localtime().tm_year and tahun_out == localtime().tm_year+1:
                            if bulan_in < localtime().tm_mon or hari_in < localtime().tm_mday:
                                tanggal = False
                            else:
                                tanggal = True
                        elif tahun_in == localtime().tm_year+1 and tahun_out == localtime().tm_year+1:
                            tanggal = True

                        if tanggal == True:
                            Regist.insert(regist) # Memasukan no. regist ke dalam BST

                            pilih_kamar = True
                            while pilih_kamar:
                                clsscr()
                                print('---------------------------------------')
                                print('              Jenis Kamar              ')
                                print('---------------------------------------')
                                print('[1] Single Room      Rp.  85.000/hari  ')
                                print('[2] Double Room      Rp. 150.000/hari  ')
                                print('---------------------------------------')
                                pilih = input('Pilih [1..2] > ')
                            
                                # Pemilihan nomor kamar pada single room
                                if pilih == '1':
                                    clsscr()
                                    print('---------------------------------------------------')
                                    print('                    SINGLE ROOM                    ')
                                    print('---------------------------------------------------')
                                    print('Nomor kamar yang tersedia :')
                                    Sgl.display(Sgl.root) # Menampilkan nomor kamar yang tersedia
                                    
                                    while True:
                                        no_kamar = input('\nPilih nomor kamar > ')
                                        # Validasi nomor kamar, apakah nomor yang dimasukan berupa alpha?
                                        valid, pesanError = validasiNomor(no_kamar)
                                        if valid:
                                            kamar = int(no_kamar)
                                            # Mengecek apakah nomor kamar yang dimasukan tersedia dalam BST
                                            if(Sgl.find(kamar) == True):
                                                break
                                            else:
                                                print('[!] Nomor kamar tidak tersedia...')
                                        else:
                                            print("\n[!] PERHATIAN [!]")
                                            print(pesanError)

                                    # Menghapus nomor kamar yang telah dipesan
                                    Sgl.delete(kamar)
                                    jenis  = 'Single Room'
                                    harga  = 85000

                                    # Mengecek apakah bulan check out lebih besar dari bulan check in?
                                    # dan apakah tahun check out lebih besar dari tahun check in?
                                    # Kemudian biaya akan dihitung dan otomatis ditampilkan
                                    if bulan_out > bulan_in:
                                        biaya  = hitungTotal(hari_in, hari_out, bulan_in, bulan_out, harga)
                                    elif bulan_out < bulan_in and tahun_out > tahun_in:
                                        biaya  = hitungTotal(hari_in, hari_out, bulan_in, bulan_out, harga)
                                    else:
                                        hari  = hari_out - hari_in
                                        biaya = harga * hari
                                    print('\nTotal Pembayaran          : ', biaya)

                                    # Memasukan data pemesanan ke dalam SLL single room
                                    Data_Sgl.add(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                                    print('\n[!] Data pemesanan kamar berhasil ditambahkan... ')
                                    print('---------------------------------------------------')
                                    input('Tekan ENTER untuk kembali ke Menu... ')
                                    pilih_kamar = False
                                    repeat      = False

                                # Pemilihan nomor kamar pada double room
                                elif pilih == '2':
                                    clsscr()
                                    print('---------------------------------------------------')
                                    print('                    DOUBLE ROOM                    ')
                                    print('---------------------------------------------------')
                                    print('Nomor kamar yang tersedia :')
                                    Dbl.display(Dbl.root) # Menampilkan nomor kamar yang tersedia
                                    
                                    while True:
                                        # Validasi nomor kamar, apakah nomor yang dimasukan berupa alpha?
                                        no_kamar = input('\nPilih nomor kamar > ')
                                        valid, pesanError = validasiNomor(no_kamar)
                                        if valid:
                                            kamar = int(no_kamar)
                                            # Mengecek apakah nomor kamar yang dimasukan tersedia dalam BST
                                            if(Dbl.find(kamar) == True):
                                                break
                                            else:
                                                print('[!] Nomor kamar tidak tersedia...')
                                        else:
                                            print("\n[!] PERHATIAN [!]")
                                            print(pesanError)

                                    # Menghapus nomor kamar yang telah dipesan
                                    Dbl.delete(kamar)
                                    jenis  = 'Double Room'
                                    harga  = 150000

                                    # Mengecek apakah bulan check out lebih besar dari bulan check in?
                                    # dan apakah tahun check out lebih besar dari tahun check in?
                                    # Kemudian biaya akan dihitung dan otomatis ditampilkan
                                    if bulan_out > bulan_in:
                                        biaya  = hitungTotal(hari_in, hari_out, bulan_in, bulan_out, harga)
                                    elif bulan_out < bulan_in and tahun_out > tahun_in:
                                        biaya  = hitungTotal(hari_in, hari_out, bulan_in, bulan_out, harga)
                                    else:
                                        hari  = hari_out - hari_in
                                        biaya = harga * hari
                                    print('\nTotal Pembayaran          : ', biaya)

                                    # Memasukan data pemesanan ke dalam SLL double room
                                    Data_Dbl.add(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                                    print('\n[!] Data pemesanan kamar berhasil ditambahkan... ')
                                    print('---------------------------------------------------')
                                    input('Tekan ENTER untuk kembali ke Menu... ')
                                    pilih_kamar = False
                                    repeat      = False
                                # Masuk else jika memasukan pilihan jenis kamar yang tidak tersedia
                                else:
                                    input('[!] Pilihan tidak tersedia ')
                        # Masuk else jika tanggal = False
                        else:
                            print("\n[!] PERHATIAN [!]")
                            print('[!] Tanggal yang dimasukan sudah terlewat')
                            print()
                            while True:
                                ulang = input("Apakah anda ingin mengulangi pengisian data? [y/t] > ")
                                # Memasukkan data ulang
                                if ulang.lower() == "y":   
                                    print()                         
                                    break
                                elif ulang.lower() == "t":
                                    repeat = False
                                    break 
                    # Masuk else jika nomor registrasi sudah tersedia pada data sebelumnya
                    else:
                        print("\n[!] PERHATIAN [!]")
                        print('[!] Nomor Registrasi sudah tersedia')
                        print()
                        while True:
                            ulang = input("Apakah anda ingin mengulangi pengisian data? [y/t] > ")
                            # Memasukkan data ulang
                            if ulang.lower() == "y":   
                                print()                         
                                break
                            elif ulang.lower() == "t":
                                repeat = False
                                break  
                # Masuk else jika ada kesalahan pada validasi data / valid = False     
                else:
                    print("\n[!] PERHATIAN [!]")
                    print(pesanError)
                    print()
                    while True:
                        ulang = input("Apakah anda ingin mengulangi pengisian data? [y/t] > ")
                        # Memasukkan data ulang
                        if ulang.lower() == "y":   
                            print()                         
                            break
                        elif ulang.lower() == "t":
                            repeat = False
                            break

        # Pilihan 2 -> Mengecek nomor kamar yang tersedia / aktif
        elif pilih == '2':
            clsscr()
            print('===================================================')
            print('             NOMOR KAMAR YANG TERSEDIA             ')
            print('---------------------------------------------------')
            print('Nomor Kamar yang Tersedia : \n                     ')
            print('[1] Single Room') # Menampilkan urutan nomor kamar single room yang tersedia
            Sgl.display(Sgl.root)
            print('\n')
            print('[2] Double Room') # Menampilkan urutan nomor kamar double room yang tersedia
            Dbl.display(Dbl.root)
            print()
            print('===================================================')
            input('Tekan ENTER untuk kembali ke Menu... ')

        # Pilihan 3 -> Mengecek data penginapan yang sedang aktif
        elif pilih == '3':
            clsscr()
            pilih_kamar = True
            while pilih_kamar:
                print('==================================================')
                print('           DATA PENGINAPAN YANG AKTIF             ')
                print('--------------------------------------------------')
                print('               Pilihan Jenis Kamar                ')
                print('--------------------------------------------------')
                print('[1] Single Room                                   ')
                print('[2] Double Room                                   ')
                print('==================================================')
                pilih = input('Pilih [1..2] > ')

                if pilih == '1':
                    clsscr()
                    print('==================================================')
                    print('           DATA PENGINAPAN YANG AKTIF             ')
                    print('                [ SINGLE ROOM ]                   ')
                    print('--------------------------------------------------')
                    # Menampilkan data penginapan pada kamar double room
                    Data_Sgl.printElement()
                    print('==================================================')
                    input('Tekan ENTER untuk kembali ke Menu... ')
                    pilih_kamar = False
                elif pilih == '2':
                    clsscr()
                    print('==================================================')
                    print('           DATA PENGINAPAN YANG AKTIF             ')
                    print('                [ DOUBLE ROOM ]                   ')
                    print('--------------------------------------------------')
                    # Menampilkan data penginapan pada kamar double room
                    Data_Dbl.printElement()
                    print('==================================================')
                    input('Tekan ENTER untuk kembali ke Menu... ')
                    pilih_kamar = False
                # Masuk else jika memasukan pilihan jenis kamar yang tidak tersedia
                else:
                    input('[!] Pilihan tidak tersedia ')
                    clsscr()

        # Pilihan 4 -> Mencari data penginapan berdasarkan nomor registrasi 
        elif pilih == '4':
            clsscr()
            repeat = True
            while repeat:
                print('=======================================================')
                print('               PENCARIAN DATA PENGINAPAN               ')
                print('              BERDASARKAN NOMOR REGISTRASI             ')
                print('-------------------------------------------------------')
                print('Nomor Registrasi yang Tersedia : ')
                Regist.display(Regist.root)
                print('\n')
                seacrh_data = input('Masukkan Nomor Registrasi      : ')
                
                # Mengecek validasi nomor registrasi, apakah nomor yang dimasukan berupa alpha?
                valid, pesanError = validasiNomor(seacrh_data)

                if valid:
                    regist = int(seacrh_data)
                    # Mengecek apakah nomor registrasi ada di dalam BST
                    # Masuk if jika nomor registrasi ditemukan
                    if(Regist.find(regist) == True):
                        # Mencari data sesuai dengan nomor registrasi di dalam SLL
                        Data_Dbl.search(seacrh_data)
                        Data_Sgl.search(seacrh_data)
                        print('=======================================================')
                        input('Tekan ENTER untuk kembali ke Menu... ')
                        repeat = False
                    # Masuk else jika nomor registrasi tidak tersedia atau tidak ditemukan
                    else:
                        print('[!] Data tidak ditemukan\n')
                        while True:
                            ulang = input("Apakah anda ingin mengulangi pencarian data? [y/t] > ")
                            # Memasukkan data ulang
                            if ulang.lower() == "y":
                                clsscr()                        
                                break
                            elif ulang.lower() == "t":
                                repeat = False
                                break
                # Masuk else jika ada kesalahan pada validasi nomor registrasi
                else:
                    print('\n=====================================================')
                    print("[!] PERHATIAN [!]")
                    print(pesanError)
                    input('Tekan ENTER untuk mencari data ulang... ')
                    clsscr()

        # Pilihan 5 -> Untuk check out penginapan yang sedang aktif
        elif pilih == '5':
            clsscr()
            pilih_kamar = True
            while pilih_kamar:
                print('==================================================')
                print('              CHECK OUT PENGINAPAN                ')
                print('--------------------------------------------------')
                print('                   Jenis Kamar                    ')
                print('--------------------------------------------------')
                print('[1] Single Room                                   ')
                print('[2] Double Room                                   ')
                print('==================================================')
                pilih = input('Pilih [1..2] > ')

                repeat = True
                if pilih == '1':
                    while repeat:
                        clsscr()
                        print('========================================================')
                        print('                   CHECK OUT PENGINAPAN                 ')
                        print('--------------------------------------------------------')
                        reg    = input('Masukkan Nomor Registrasi : ')
                        no_co  = input('Masukkan Nomor Kamar      : ')

                        # Mengecek validasi nomor registrasi dan nomor kamar, apakah nomor-nomor tersebut berupa alpha?
                        valid, pesanError = validasiNomor(reg, no_co)

                        if valid:
                            regist = int(reg)
                            kamar  = int(no_co)
                            # Mengecek apakah nomor regist dan nomor kamar yang dimasukan tersedia dalam BST
                            if(Regist.find(regist) == True and Sgl.find(kamar) == False):
                                # Menghapus nomor registrasi pada BST
                                Regist.delete(regist)
                                # Menambahkan kembali nomor kamar yang sudah di-check out ke BST
                                Sgl.insert(kamar)
                                # Menghapus data penginapan sesuai nomor registrasi
                                Data_Sgl.delete(no_co)
                                # Menambahkan data ke Queue data check out single room
                                Sgl_Out.add(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                                print('\n[!] Check out penginapan telah berhasil ')
                                print('========================================================')
                                input('Tekan ENTER untuk kembali ke Menu... ')
                                repeat      = False
                                pilih_kamar = False
                            # Masuk else jika nomor registrasi atau dan nomor kamar tidak ditemukan
                            else:
                                print('\n[!] No. Registrasi atau No. Kamar tidak ditemukan\n')
                                while True:
                                    ulang = input("Apakah anda ingin mengulangi pencarian data? [y/t] > ")
                                    # Memasukkan data ulang
                                    if ulang.lower() == "y": 
                                        print()                         
                                        break
                                    elif ulang.lower() == "t":
                                        repeat      = False
                                        pilih_kamar = False
                                        break
                        # Masuk else jika ada kesalahan pada nomor registrasi atau dan nomor kamar
                        else:
                            print('========================================================')
                            print("[!] PERHATIAN [!]")
                            print(pesanError)
                            input('Tekan ENTER untuk mencari data ulang... ')
                            clsscr()

                elif pilih == '2':
                    while repeat:
                        clsscr()
                        print('========================================================')
                        print('                   CHECK OUT PENGINAPAN                 ')
                        print('--------------------------------------------------------')
                        reg    = input('Masukkan Nomor Registrasi : ')
                        no_co  = input('Masukkan Nomor Kamar      : ')

                        # Mengecek validasi nomor registrasi, apakah nomor yang dimasukan berupa alpha?
                        valid, pesanError = validasiNomor(reg, no_co)

                        if valid:
                            regist = int(reg)
                            kamar  = int(no_co)
                            # Mengecek apakah nomor regist dan nomor kamar yang dimasukan tersedia dalam BST
                            if(Regist.find(regist) == True and Dbl.find(kamar) == False):
                                # Menghapus nomor registrasi pada BST
                                Regist.delete(regist)
                                # Menambahkan kembali nomor kamar yang sudah di-check out ke BST
                                Dbl.insert(kamar)
                                # Menghapus data penginapan sesuai nomor registrasi
                                Data_Dbl.delete(no_co)
                                # Menambahkan data ke Queue data check out double room
                                Dbl_Out.add(no_regist, nik, nama, no_telp, check_in, check_out, biaya, jenis, no_kamar)
                                print('\n[!] Check out penginapan telah berhasil ')
                                print('========================================================')
                                input('Tekan ENTER untuk kembali ke Menu... ')
                                repeat      = False
                                pilih_kamar = False
                            # Masuk else jika nomor registrasi atau dan nomor kamar tidak ditemukan
                            else:
                                print('\n[!] No. Registrasi atau No. Kamar tidak ditemukan\n')
                                while True:
                                    ulang = input("Apakah anda ingin mengulangi pencarian data? [y/t] > ")
                                    # Memasukkan data ulang
                                    if ulang.lower() == "y":   
                                        print()                         
                                        break
                                    elif ulang.lower() == "t":
                                        repeat      = False
                                        pilih_kamar = False
                                        break
                        # Masuk else jika ada kesalahan pada nomor registrasi atau dan nomor kamar
                        else:
                            print('========================================================')
                            print("[!] PERHATIAN [!]")
                            print(pesanError)
                            input('Tekan ENTER untuk mencari data ulang... ')
                            clsscr()
                # Masuk else jika memasukan pilihan jenis kamar yang tidak tersedia
                else:
                    input('[!] Pilihan tidak tersedia ')
                    clsscr()

        # Pilihan 6 -> Untuk melihat data penginapan yang sudah tidak aktif atau check out
        elif pilih == '6':
            clsscr()
            pilih_kamar = True
            while pilih_kamar:
                print('===================================================')
                print('             DATA PENGINAPAN CHECK OUT             ')
                print('---------------------------------------------------')
                print('                Pilihan Jenis Kamar                ')
                print('---------------------------------------------------')
                print('[1] Single Room                                    ')
                print('[2] Double Room                                    ')
                print('===================================================')
                pilih = input('Pilih [1..2] > ')

                if pilih == '1':
                    clsscr()
                    print('==================================================')
                    print('        DATA PENGINAPAN YANG TIDAK AKTIF          ')
                    print('                [ SINGLE ROOM ]                   ')
                    print('--------------------------------------------------')
                    # Menampilkan data penginapan check out pada kamar single room
                    Sgl_Out.printData()
                    print('==================================================')
                    input('Tekan ENTER untuk kembali ke Menu... ')
                    pilih_kamar = False
                elif pilih == '2':
                    clsscr()
                    print('==================================================')
                    print('        DATA PENGINAPAN YANG TIDAK AKTIF          ')
                    print('                [ DOUBLE ROOM ]                   ')
                    print('--------------------------------------------------')
                    # Menampilkan data penginapan check out pada kamar double room
                    Dbl_Out.printData()
                    print('==================================================')
                    input('Tekan ENTER untuk kembali ke Menu... ')
                    pilih_kamar = False
                # Masuk else jika memasukan pilihan jenis kamar yang tidak tersedia
                else:
                    input('[!] Pilihan tidak tersedia ')
                    clsscr()
            
        # Pilihan 7 -> Keluar dari program
        elif pilih == '7':
            print()
            exit('[!] Keluar dari program... ')

        # Jika pilihan tidak tersedia
        else:
            print()
            input('Menu pilihan tidak tersedia...')