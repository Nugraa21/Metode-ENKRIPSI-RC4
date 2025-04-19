
# Naskah
Link ppt [Canva](https://youtu.be/oocm0fDqDKY?si=1oP3Djgcrcgic7v0)
#


> Yow di sini saya akan menjelaskan tentang model kriptografi untuk mengenkripsi dengan metode RC4

> Nah sebelum itu disclaimer dulu di encripsi ada yang di sebut dengan 

## Stream Cipher dan Block Cipher 

> yang pertama ada Stream Cipher
```
metode enkripsi yang mengenkripsi data satu bit
atau satu byte dalam satu waktu

Biasanya lebih cepat dan digunakan untuk data dengan ukuran besar atau transmisi data secara langsung atau (real-time). Kunci digunakan untuk menghasilkan "keystream" yang dikombinasikan dengan data plaintext menggunakan operasi XOR.
```

#
> Berikutnya ada Block Cipher
```
mengenkripsi data dalam blok-blok dengan
ukuran tetap

misalnya 64-bit atau 128-bit). Data yang kurang dari ukuran blok di-padding agar sesuai. Blok-blok ini dienkripsi satu per satu menggunakan algoritma dan kunci tertentu.
```

## Habis itu ada juga yang di maksut dengan  Simmetric Cipher dan Asymmetric Cipher

>  Simmetric Cipher 
```
Menggunakan satu kunci untuk proses enkripsi 

jadi hanya satu kunci saja 
```
#
>  Asymmetric Cipher
```
Menggunakan pasangan kunci (kunci publik dan
kunci privat)

Kunci publik digunakan untuk enkripsi, sementara kunci privat untuk dekripsi. Metode ini lebih lambat tetapi lebih aman untuk pertukaran kunci.

```


#  RC4 Encryption

# RC4 adalah algoritma stream cipher

> Ini adalah sebuah algoritma untuk mengenkripsi dengan muda pada zamanya 

> dan Perancang Ron Rivest pada tahun 1987. dan di publickaskasikan pada tahun 1994 untuk RSA Security dan dikenal karena efisiensi dan kecepatan prosesnya.

> sering digunakan untuk aplikasi
- SSL / TLS ( Secure socket ,transport layer )
    Biasanya di gunakan pada kemananan website atau yang lebih di kenal dengan HTTPS

- WEP / WPA ( Wired Equivalen Privacy ,Wi-Fi Protected Access )
    Ini lebih sering di gunakan untuk jaringan seperti wifi atau aksespoin

















