class bunga:
    def __init__(self, warna, jenis, fungsi):
        self.warna = warna
        self.jenis = jenis
        self.fungsi = fungsi

    def printname(self):
        print(self.warna)
        print(self.jenis)
        print(self.fungsi)

class rose(bunga):
    def __init__(self, warna, jenis, fungsi):
        bunga.__init__(self, warna, jenis, fungsi)

    def tampilanrose(self):
        print("Jenis bunga rose : ", self.jenis)
        print("Warna            : ", self.warna)
        print("Fungsi           : ", self.fungsi)

class tulip(bunga):
    def __init__(self, warna, jenis, fungsi):
        bunga.__init__(self, warna, jenis, fungsi)

    def tampilantulip(self):
        print("Jenis bunga tulip: ", self.jenis)
        print("Warna            : ", self.warna)
        print("Fungsi           : ", self.fungsi)

a = rose("merah", "rose canina", "rose can be a valentine flower and they can produce a natural vitamin C")
b = tulip("pink", "tulip gesneriana", "tulip flower usually used for celebrate an important moment and can be a valentine flower too")

a.tampilanrose()
print("==================================================================================")
b.tampilantulip()