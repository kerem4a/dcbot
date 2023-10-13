import random

def sifre_uret(parola_uzunlugu):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


    olusturulan_parola = ""

    for _ in range(parola_uzunlugu):

        rastgele_karakter = random.choice(karakterler)
        olusturulan_parola += rastgele_karakter

    return olusturulan_parola
