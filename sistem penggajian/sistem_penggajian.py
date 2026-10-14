# 1. Class Induk: Karyawan
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok

    # Getter: mengambil/melihat gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Setter: mengubah gaji pokok
    def set_gaji_pokok(self, gaji_pokok): #menghitung gaji pokok dan tunjangan
        if gaji_pokok <= 0: #if itu jika
            print("Peringatan: Gaji pokok harus lebih dari 0!")
        else: #jika tidak/digunakan jika if tidak terpenuhi/menjalankan pilihan lain
            self.__gaji_pokok = gaji_pokok
            print("Gaji pokok berhasil diubah.")

    def hitung_gaji_total(self): 
        return self.__gaji_pokok

    def tampilkan_info(self): #def itu untuk membuat fungsi atau method/kita membuat perinta bernama tampilkan info untuk menampilkan inforfasi karyawan
        print("Nama Karyawan :", self.nama)
        print("ID Karyawan   :", self.id_karyawan)
        print("Gaji Pokok    : Rp", self.get_gaji_pokok())


# 2. Class Anak: Karyawan Tetap
class KaryawanTetap(Karyawan): #karyawan itu induk dan karyawan tetap mewarisi ilmu indukny
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan

    def tampilkan_info(self):
        print("=== KARYAWAN TETAP ===")
        print("Nama Karyawan :", self.nama)
        print("ID Karyawan   :", self.id_karyawan)
        print("Gaji Pokok    : Rp", self.get_gaji_pokok())
        print("Tunjangan     : Rp", self.tunjangan)
        print("Total Gaji    : Rp", self.hitung_gaji_total())


# 3. Class Anak: Karyawan Kontrak
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok,
                 jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur
#menghitung total gaji karyawan kontrak /gaji pokok dan jam lembur
    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + (
            self.jam_lembur * self.tarif_lembur # jam lembur menyimpan jumlah jam lembur dan tarif lembur menyimpan bayaran per jam lembur
        )
#
    def tampilkan_info(self):
        print("=== KARYAWAN KONTRAK ===")
        print("Nama Karyawan :", self.nama)
        print("ID Karyawan   :", self.id_karyawan)
        print("Gaji Pokok    : Rp", self.get_gaji_pokok()) 
        print("Jam Lembur    :", self.jam_lembur, "jam")
        print("Tarif Lembur  : Rp", self.tarif_lembur)
        print("Total Gaji    : Rp", self.hitung_gaji_total()) #total gaji : 4500000


# 4. Main Program: Membuat objek karyawan
karyawan1 = KaryawanTetap(
    "Friska Amelia", "K001", 5000000, 1000000
)

karyawan2 = KaryawanKontrak(
    "Pusing", "K002", 4000000, 10, 50000
)


# 5. Menyimpan objek ke dalam list
daftar_karyawan = [karyawan1, karyawan2]


# 6. Polymorphism: perintah yang sama bisa menghasilkan yang sama/
print("===== DAFTAR KARYAWAN =====")

for karyawan in daftar_karyawan: #dari karyawan untuk daftar karyawan atau dari induk ke anak
    karyawan.tampilkan_info()
    print()


# 7. Encapsulation: Menguji perubahan gaji pokok mencoba perlidungan data gaji berjalan dengan benar
print("===== UJI ENCAPSULATION =====")

print("\nMengubah gaji dengan nilai tidak valid:")
karyawan1.set_gaji_pokok(-1000000) 

print("\nMengubah gaji dengan nilai valid:")
karyawan1.set_gaji_pokok(5500000)

print("\nInformasi karyawan setelah gaji diubah:")
karyawan1.tampilkan_info()