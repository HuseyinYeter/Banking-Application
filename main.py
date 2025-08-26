import getpass

import random

class Banka:
    def __init__(self,name):
        self.name = name
        self.müşteriler = list()

    def müşteri_ekle(self,müsteri):
        self.müşteriler.append(müsteri)

class Müşteri:
    def __init__(self, isim, şifre,iban,bakiye= 0):
        self.isim = isim
        self.şifre = şifre
        self.iban = iban
        self.bakiye = bakiye


    def __eq__(self, other):
        if isinstance(other, Müşteri):
            return self.isim == other.isim and self.şifre == other.şifre
        return False

class Asistan:
    def __init__(self,name):
        self.name = name

    def konuşma(self):
        print(f"{self.name} > Merhaba! Size hangi konuda yardımcı olabilirim ? :)")
    def sohbet_bitirme(self):
        print("İyi günler dilerim!")
    def talep_para_çekme(self):
        print("Kullanıcı dönütlerimize göre,bu problem uygulamamızdan çık gir yaparak çözülebilir.")
        print("Aynı zamanda Wi-Fi bağlantınızı ve hesabınızdaki bakiye miktarıyla,çekmek istediğiniz miktarın\n"
              "uyumlu olduğunu kontrol ederek bu problemi çözebilirsiniz :)")

    def talep_para_yatırma(self):
        print("Kullanıcı dönütlerimize göre,bu problem uygulamamızdan çık gir yaparak çözülebilir.")
        print("Aynı zamanda bu problemi Wi-Fi ayarlarını kontrol ederek çözebilirsiniz.")

    def talep_iban_gözükme(self):
        print("Bu problem'i uygulamamızdan çıkış yapıp tekrar girerek çözebilirsiniz.")

    def talep_iban_para_yollama(self):
        print("Hedef IBAN'ı doğru yazdığınızdan emin olun.")
        print("Bu IBAN'ın gerçekliğinden emin olun.")
        print("Yollamak istediğiniz miktar ile mevcut bakiyenizin uyumluluğunu kontrol ediniz.")

def para_yatır(müşteri):
    miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
    return miktar

def para_çek(müşteri):
    miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
    return miktar

def iban_para_gönder(müşteri, banka):
    hedef_iban = input("Hedef IBAN Giriniz: ")
    miktar = float(input("Yollamak istediğiniz miktarı giriniz: "))

    # Hedef müşteriyi bul
    hedef_müşteri = next((m for m in banka.müşteriler if m.iban == hedef_iban), None)

    if hedef_müşteri is None:
        print("Hedef IBAN bulunamadı!")
        return 0

    if miktar <= 0:
        print("Geçersiz miktar!")
        return 0

    if miktar > müşteri.bakiye:
        print("Yetersiz bakiye!")
        return 0

    # İşlemi gerçekleştir
    müşteri.bakiye -= miktar
    hedef_müşteri.bakiye += miktar
    print(f"{miktar:.2f} TL başarıyla gönderildi.")
    return miktar


def main():
    banka = Banka("Yeter Bank")
    asistan = Asistan("YeterAsistan")
    kullanıcı_bakiye = 0
    is_running = True

    while is_running:

        print("***** YETER BANK *****")
        print("1.Bankaya Kayıt Ol")
        print("2.Giriş Yap")
        print("3.Çıkış")
        seçenek = input("İşlem Numaranızı Giriniz: ")

        if seçenek == "1":

            müşteri = Müşteri(input("İsim Soyisim Giriniz: "),
                              (input("6 haneli Şifrenizi giriniz: ")),
                              iban = f"4627-5600-{random.randint(1000,9999)}-{random.randint(1000,9999)}"

                              )

            if not müşteri.şifre.isdigit():
                print("Şifre rakam dışı unsur içeriyor!")

            elif len(müşteri.şifre) != 6:
                print(f"{len(müşteri.şifre)} haneli şifre geçersizdir! 6 haneli olmak zorundadır.")

            else:
                banka.müşteriler.append(müşteri)
                print("Başarıyla Kayıt Oluşturuldu")

        elif seçenek == "2":
            print("İsminizi ve Şifrenizi giriniz-")
            isim = input("İsim: ")
            şifre = input("Şifre: ")
            
            müşteri_deneme = next((m for m in banka.müşteriler if m.isim == isim and m.şifre == şifre), None)

            if müşteri_deneme:
                print("Başarıyla Giriş Yapıldı!")
                while is_running:

                    print("***** YETER BANK *****")
                    print(f"Kullanıcı: {müşteri_deneme.isim}")
                    print(f"IBAN: {müşteri_deneme.iban} | Bakiye: {müşteri_deneme.bakiye:.2f} TL")

                    print()
                    print("1.Para Yatır")
                    print("2.Para Çek")
                    print("3.IBAN'a Para Gönder")
                    print("4.Ana Menüye Dön")
                    print("5.Asistana Bağlan")
                    print("6.Çıkış")
                    secenek_1 = input("İşleminizi Giriniz: ")

                    if secenek_1 == "1":
                        para = para_yatır(müşteri_deneme)


                        if para <= 0:
                            print("İşlem Gerçekleştirilemedi # GEÇERSİZ DEĞER")
                        else:
                            müşteri_deneme.bakiye += para
                            print("BAŞARIYLA İŞLEM TAMAMLANDI")

                    elif secenek_1 == "2":
                        para = para_çek(müşteri_deneme)
                        if para > müşteri_deneme.bakiye:
                            print("İşlem Gerçekleştirilemedi # GEÇERSİZ DEĞER")
                        elif para <= 0:
                            print("İşlem Gerçekleştirilemedi # GEÇERSİZ DEĞER")
                        else:
                            müşteri_deneme.bakiye -= para
                            print("BAŞARIYLA İŞLEM TAMAMLANDI")


                    elif secenek_1 == "3":

                        iban_para_gönder(müşteri_deneme, banka)




                    elif secenek_1 == "4":
                        break

                    elif secenek_1 == "5":
                        asistan.konuşma()
                        print("1.PARA ÇEKME PROBLEMİ")
                        print("2.PARA YATIRMA PROBLEMİ")
                        print("3.IBAN'IM GÖRÜNMÜYOR")
                        print("4.IBAN'A GÖNDEREMİYORUM")
                        print("5.Geri Dön")
                        talep = input("İşleminizin numarasını giriniz: ")

                        if talep == "1":
                            asistan.talep_para_çekme()
                            asistan.sohbet_bitirme()
                            print()

                        elif talep == "2":
                            asistan.talep_para_yatırma()
                            asistan.sohbet_bitirme()
                            print()

                        elif talep == "3":
                            asistan.talep_iban_gözükme()
                            asistan.sohbet_bitirme()
                            print()

                        elif talep == "4":
                            asistan.talep_iban_para_yollama()
                            asistan.sohbet_bitirme()
                            print()

                        elif talep == "5":
                            break

                        else:
                            print("Geçersiz Komut")



                    elif secenek_1 == "6":
                        is_running = False
                        print("Çıkış Yapıldı!")



            else:
                print("Kullanıcı Bulunamadı! Lütfen Kayıt Olunuz.")


        elif seçenek == "3":
            is_running = False
            print("Çıkış Yapıldı!")

        else:
            print("Geçersiz İşlem")

if __name__ == "__main__":
    main()
