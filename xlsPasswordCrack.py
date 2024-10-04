import msoffcrypto
import sys

if len(sys.argv) != 3:
    print("Kullanım: python3 xlsPasswordCrack.py  şifreli_dosya_yolu  word-list-yolu")
    sys.exit(1)

# Komut satırından dosya yollarını al
file_path = sys.argv[1]
rockyou_path = sys.argv[2]

# Şifreli dosyayı aç
with open(file_path, "rb") as f:
    office_file = msoffcrypto.OfficeFile(f)

    # RockYou listesindeki şifreleri oku
    with open(rockyou_path, "r", encoding="latin-1") as rockyou:
        print("Başlıyor...");
        # Toplam şifre sayısını al
        total_passwords = sum(1 for _ in rockyou)
        rockyou.seek(0)  # Dosya konumunu başa al

        for index, password in enumerate(rockyou):
            password = password.strip()  # Her şifreden boşlukları temizle
            try:
                office_file.load_key(password=password)  # Şifreyi yükle
                # Şifre doğruysa dosyayı aç
                with open("decrypted.xls", "wb") as decrypted:
                    office_file.decrypt(decrypted)
                print(f"Şifre bulundu: {password}")
                break  # Şifre bulunduğunda döngüden çık
            except Exception as e:
                # Yanlış şifre durumunda bir şey yapma
                pass

            # Yüzdeyi hesapla ve yazdır
            if (index + 1) % 1000 == 0:  # Her 1000 denemede bir yazdır
                percent_done = (index + 1) / total_passwords * 100
                print(f"Tamamlanan: {percent_done:.2f}% ({index + 1}/{total_passwords})")

