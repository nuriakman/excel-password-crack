# Excel Password Crack

## Kurulum

`RockYou.txt` dosyası: İnternetten indirilebilecek ve en çok kullanılan şifreleri barındıran bir şifre listedir.

İndir: [`RockYou.txt`](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

```bash
sudo apt update

#pip kurulumu
sudo apt install python3-pip

#xls dosya için şifre kırma python paketinin yüklenmesi
pip install msoffcrypto-tool
#Kaldırmak için: pip uninstall msoffcrypto-tool

#Yukarıdaki kurmazsa bunu kullan
python3 -m pip install msoffcrypto-tool

wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt RockYou1.txt
#Şifre kırma işlemini başlatalım
```

## Şifre Çözme

```bash
python3 xlsPasswordCrack.py sifreli.xls RockYou.txt

#Örnek çıktı:
#Başlıyor...
#Tamamlanan: 0.07% (10000/14344391)
#Tamamlanan: 0.14% (20000/14344391)
#.....
#Tamamlanan: 3.07% (440000/14344391)
#Şifre bulundu: 2255

```

Şifre çözüldüyse, şifresiz dosya `decrypted.xls` adı ile oluşturulacaktır.

## John the Ripper

Proje sitesi: https://github.com/openwall/john

John the Ripper jumbo - advanced offline password cracker, which supports hundreds of hash and cipher types, and runs on many operating systems, CPUs, GPUs, and even some FPGAs
