from tkinter import Tk, Label, Text, END
from tkinter.ttk import Button, Entry, Style, Frame
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64
import ttkbootstrap as ttk


# Fungsi untuk mengenkripsi teks
def encrypt_blowfish(plain_text, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    padded_text = pad(plain_text.encode(), Blowfish.block_size)
    encrypted_bytes = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_bytes).decode()


# Fungsi untuk mendekripsi teks
def decrypt_blowfish(encrypted_text, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), Blowfish.block_size)
    return decrypted_bytes.decode()


# Fungsi untuk menangani enkripsi
def handle_encrypt():
    plain_text = input_text.get("1.0", END).strip()
    key = key_entry.get()
    if len(key) < 4 or len(key) > 56:
        result_text.delete("1.0", END)
        result_text.insert(END, "Kunci harus antara 4 hingga 56 karakter.")
    else:
        encrypted_text = encrypt_blowfish(plain_text, key)
        result_text.delete("1.0", END)
        result_text.insert(END, encrypted_text)


# Fungsi untuk menangani dekripsi
def handle_decrypt():
    encrypted_text = input_text.get("1.0", END).strip()
    key = key_entry.get()
    if len(key) < 4 or len(key) > 56:
        result_text.delete("1.0", END)
        result_text.insert(END, "Kunci harus antara 4 hingga 56 karakter.")
    else:
        try:
            decrypted_text = decrypt_blowfish(encrypted_text, key)
            result_text.delete("1.0", END)
            result_text.insert(END, decrypted_text)
        except Exception:
            result_text.delete("1.0", END)
            result_text.insert(END, "Dekripsi gagal. Pastikan teks dan kunci benar.")


# Membuat antarmuka menggunakan ttkbootstrap
root = ttk.Window(themename="superhero")  # Pilih tema modern
root.title("Blowfish Encryption & Decryption")
root.geometry("600x500")

# Frame utama
main_frame = Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Label dan Entry untuk kunci
Label(main_frame, text="Masukkan Kunci ", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
key_entry = Entry(main_frame, width=50)
key_entry.grid(row=1, column=0, pady=10)

# Label dan Text untuk teks masukan
Label(main_frame, text="Masukkan Teks:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")
input_text = Text(main_frame, height=5, width=60)
input_text.grid(row=3, column=0, pady=10)

# Tombol untuk Enkripsi dan Dekripsi
button_frame = Frame(main_frame)
button_frame.grid(row=4, column=0, pady=10)
Button(button_frame, text="Enkripsi", command=handle_encrypt, width=15, bootstyle="success").pack(side="left", padx=5)
Button(button_frame, text="Dekripsi", command=handle_decrypt, width=15, bootstyle="info").pack(side="left", padx=5)

# Label dan Text untuk hasil
Label(main_frame, text="Hasil:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w")
result_text = Text(main_frame, height=5, width=60)
result_text.grid(row=6, column=0, pady=10)

# Menjalankan GUI
root.mainloop()

