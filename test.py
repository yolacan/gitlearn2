def toplama_islemi():
    try:
        # Kullanıcıdan iki tam sayı alıyoruz
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        
        # İki sayıyı topluyoruz
        toplam = sayi1 + sayi2
        
        # Sonucu ekrana yazdırıyoruz
        print(f"Toplam: {toplam}")
        
        # Kullanıcıya sonucu yazdırmak isteyip istemediğini soruyoruz
        yazdirma = input("Sonucu yazdırmak ister misiniz? (Evet/Hayır): ").strip().lower()
        
        if yazdirma == "evet":
            with open("sonuc.txt", "w") as dosya:
                dosya.write(f"Toplam: {toplam}")
            print("Sonuç 'sonuc.txt' dosyasına yazdırıldı.")
        else:
            print("Sonuç yazdırılmadı.")
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")

# Fonksiyonu çağırarak işlemi başlatıyoruz
toplama_islemi()
