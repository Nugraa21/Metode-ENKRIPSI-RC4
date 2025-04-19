# Algoritma RC4

[Link ke PPT](https://www.canva.com/design/DAGWUZmmoco/aAExQWA5eFwlTMbwNTiGmw/view?utm_content=DAGWUZmmoco&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd802fd307f)

## Pendahuluan
RC4 adalah salah satu algoritma stream cipher yang sederhana dan cepat. Algoritma ini terdiri dari dua tahap utama:
1. **Key-Scheduling Algorithm (KSA)**: Untuk menginisialisasi array kunci.
2. **Pseudo-Random Generation Algorithm (PRGA)**: Untuk menghasilkan byte pseudo-acak yang digunakan dalam proses enkripsi atau dekripsi.

---

## Langkah-Langkah Algoritma

### 1. Key-Scheduling Algorithm (KSA)
KSA bertujuan untuk menginisialisasi array `S` berdasarkan kunci yang diberikan.

#### Pseudocode KSA:
```plaintext
Input: Kunci (key) dengan panjang N byte
Output: Array S yang teracak

1. Buat array S yang berisi nilai 0 hingga 255:
   S[i] = i untuk i = 0 hingga 255.

2. Inisialisasi j = 0.

3. Lakukan permutasi pada array S:
   Untuk i dari 0 hingga 255:
      j = (j + S[i] + key[i % panjang_key]) mod 256
      Tukar nilai S[i] dan S[j]

4. Array S siap digunakan.
```

---

### 2. Pseudo-Random Generation Algorithm (PRGA)
PRGA menghasilkan byte pseudo-acak yang digunakan dalam proses enkripsi atau dekripsi melalui operasi XOR.

#### Pseudocode PRGA:
```plaintext
Input: Array S dari KSA
Output: Byte pseudo-acak untuk proses XOR

1. Inisialisasi i = 0 dan j = 0.

2. Untuk setiap byte yang diinginkan:
   a. i = (i + 1) mod 256
   b. j = (j + S[i]) mod 256
   c. Tukar nilai S[i] dan S[j]
   d. K = S[(S[i] + S[j]) mod 256]

3. Byte K adalah byte pseudo-acak yang digunakan.
```

---

### 3. Enkripsi/Dekripsi
Proses enkripsi dan dekripsi menggunakan operasi XOR antara plaintext/ciphertext dan byte pseudo-acak yang dihasilkan dari PRGA.

#### Rumus:
```plaintext
ciphertext = plaintext XOR K
plaintext = ciphertext XOR K
```

---

## Implementasi Kode RC4 dalam JavaScript
Berikut adalah implementasi algoritma RC4 dalam JavaScript:

```javascript
// RC4 Implementation

function KSA(key) {
    const S = Array.from({ length: 256 }, (_, i) => i);
    let j = 0;

    for (let i = 0; i < 256; i++) {
        j = (j + S[i] + key.charCodeAt(i % key.length)) % 256;
        [S[i], S[j]] = [S[j], S[i]]; // Swap S[i] and S[j]
    }

    return S;
}

function PRGA(S) {
    let i = 0;
    let j = 0;

    return function generateByte() {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        [S[i], S[j]] = [S[j], S[i]]; // Swap S[i] and S[j]
        return S[(S[i] + S[j]) % 256];
    };
}

function RC4(key, data) {
    const S = KSA(key);
    const keystream = PRGA(S);
    
    return data.map(byte => byte ^ keystream());
}

// Contoh penggunaan
const key = "mysecretkey";
const plaintext = "Hello, RC4!";

// Enkripsi
const plaintextBytes = Array.from(plaintext).map(char => char.charCodeAt(0));
const ciphertext = RC4(key, plaintextBytes);
console.log("Ciphertext:", ciphertext);

// Dekripsi
const decryptedBytes = RC4(key, ciphertext);
const decryptedText = String.fromCharCode(...decryptedBytes);
console.log("Decrypted:", decryptedText);
```

---

## Penjelasan
1. **KSA**:
   - Membentuk array `S` berdasarkan kunci untuk menghasilkan permutasi awal.
2. **PRGA**:
   - Menghasilkan byte pseudo-acak secara terus-menerus dari array `S`.
3. **Enkripsi/Dekripsi**:
   - Menggunakan operasi XOR untuk mengamankan data. Karena sifat XOR yang reversibel, proses dekripsi menggunakan algoritma yang sama.

---

## Catatan Keamanan
- RC4 rentan terhadap serangan kriptografi modern, terutama jika kunci tidak diolah dengan baik atau jika byte awal dari stream tidak diabaikan.
- **Hindari menggunakan RC4 untuk aplikasi keamanan modern.** Algoritma ini telah digantikan oleh cipher yang lebih aman seperti AES.

