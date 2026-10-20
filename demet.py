menu = [
    ("Mercimek Çorbası", 80, 250),
    ("Adana Kebap", 320, 200),
    ("Kuru Fasulye", 120, 300)
]
def fiyati_getir(yemek):
    return yemek[1]  # Fiyat 1. indekste (ikinci eleman

menu_fiyata_gore = sorted(menu, key=fiyati_getir)

print("Fiyata Göre Sıralı Menü:")
for yemek in menu_fiyata_gore:
    print(f"- {yemek[0]}: {yemek[1]} TL")