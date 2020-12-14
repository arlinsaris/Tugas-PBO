class Product:
    __vendor_message = " "  #atribute
    name = " "  #public
    price =" "
    size = " "
    unit = " "

    def __init__(self, name): # method Konstruktor
        self.name = name
        self.unit = "gr,"
        self.unit1= "gr,"
        self.unit2 = "gr,"
        self.unit3 = "gr,"
        self.unit4 = "gr,"
        self.size = 60  # indensasi
        self.size1 = 75
        self.size2 = 370
        self.size3 = 600
        self.size4 = 220
    def get_vendor_message(self):  # method
        print (self.__vendor_message)

    def set_price(self, price): # method
        self.price = price

p = Product("Indomie goreng,")
p.set_price(3000)
p1 = Product("Pepsodent,")
p1.set_price(12000)
p2 = Product("susu kaleng frisien flag,")
p2.set_price(23000)
p3 = Product("wafer roll coklat,")
p3.set_price(14000)
p4 = Product("coco drink,")
p4.set_price(2000)
# print p.__vendor_message
p.get_vendor_message()
print("Detail Barang")
print("----------------------------------------------------------------------")
print ("%s          | Dengan Berat : %s %s  Harganya : Rp.%d" % (p.name, p.size, p.unit, p.price))
print ("%s               | Dengan Berat : %s %s  Harganya : Rp.%d" % (p1.name, p.size1, p.unit1, p1.price))
print ("%s| Dengan Berat : %s %s Harganya : Rp.%d" % (p2.name, p.size2, p.unit2, p2.price))
print ("%s       | Dengan Berat : %s %s Harganya : Rp.%d" % (p3.name, p.size3, p.unit3, p3.price))
print ("%s              | Dengan Berat : %s %s Harganya : Rp.%d" % (p4.name, p.size4, p.unit4, p4.price))




