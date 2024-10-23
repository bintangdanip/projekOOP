#1

class perpustakaan:
    def _init_(self, nama):
        self.nama = nama 
        self,__buku = ()

    def tambah_buku(self, buku):
        self.__buku.append(self)
   
    def tampilkan_buku(self):
        for buku in self,_buku:
            print(buku,info())
  
    def _str_(self):
        return f"Perpustakaan: {self.nama}"

class buku:
    def init_(self, judul, penulis):
        self,judul = judul
        self,penulis = penulis 
    def info(self):
        return f"buku: {self,judul} oleh (self.penulis)"
class bukufiksi(buku):
    def init_(self, judul, penulis,genre):
        super().__init__(self, judul, penulis)
        self,genre = genre
    
    def info(self):
        return f"buku fiksi: (self,judul) oleh {self.penulis}, Genre: {self.genre}"
class bukunonfiksi (buku):
    def__init_(self, judul, penulis.topik):
    super(),_init_(judul, penulis)
        self,topik = topik
    def info(self):
        return f"Buku Non-Fiksi: (self.judul) oleh {self.penulis}, Topik: {self.topik}"
perpustakan perpustakaan ("perpustakaan Kota")

buku1 =bukufiksi("Harry Potter", "J.K. Rowling", "Fantasi")
buku2 =bukunonfiksi ("Sapiens", "Yuval Noah Harari", "Sejarah")

perpustakan.tambah_buku(bukul)
perpustakan.tambah_buku(buku2)

print(perpustakaan)
perpustakaan.tampilkan_buku()