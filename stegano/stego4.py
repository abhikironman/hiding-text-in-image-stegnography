import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_message(img, message, password):
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(message)):
        img[n, m, z] = (d[message[i]] + ord(password[i % len(password)])) % 256
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return img

def decrypt_message(img, password):
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    message = ""
    n = 0
    m = 0
    z = 0

    for i in range(len(password)):
        img[n, m, z] = (img[n, m, z] - ord(password[i])) % 256
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return message

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    return cv2.imread(file_path)

def save_image(img):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png")])
    cv2.imwrite(file_path, img)
    return file_path

def perform_encryption():
    img = select_image()

    if img is None:
        messagebox.showerror("Error", "Image not found or invalid.")
        return

    msg = entry_msg.get()
    password = entry_password.get()

    encrypted_img = encrypt_message(img.copy(), msg, password)
    output_path = save_image(encrypted_img)

    messagebox.showinfo("Encryption", f"Image encrypted and saved to {output_path}")

def perform_decryption():
    img = select_image()

    if img is None:
        messagebox.showerror("Error", "Image not found or invalid.")
        return

    password_decrypt = entry_password_decrypt.get()

    decrypted_message = decrypt_message(img, password_decrypt)
    messagebox.showinfo("Decryption", f"Decrypted message: {decrypted_message}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryption and Decryption")

# Encryption Frame
frame_encrypt = tk.Frame(root)
frame_encrypt.pack(pady=10)

label_msg = tk.Label(frame_encrypt, text="Enter secret message:")
label_msg.grid(row=0, column=0, padx=5, pady=5)

entry_msg = tk.Entry(frame_encrypt)
entry_msg.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(frame_encrypt, text="Enter password:")
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = tk.Entry(frame_encrypt, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

btn_encrypt = tk.Button(frame_encrypt, text="Encrypt Image", command=perform_encryption)
btn_encrypt.grid(row=2, columnspan=2, pady=10)

# Decryption Frame
frame_decrypt = tk.Frame(root)
frame_decrypt.pack(pady=10)

label_password_decrypt = tk.Label(frame_decrypt, text="Enter password for Decryption:")
label_password_decrypt.grid(row=0, column=0, padx=5, pady=5)

entry_password_decrypt = tk.Entry(frame_decrypt, show="*")
entry_password_decrypt.grid(row=0, column=1, padx=5, pady=5)

btn_decrypt = tk.Button(frame_decrypt, text="Decrypt Image", command=perform_decryption)
btn_decrypt.grid(row=1, columnspan=2, pady=10)

root.mainloop()

