import cv2
import os
import string

# Get input paths from user
image_path = input("Enter the path to the image: ")
output_path = input("Enter the path for the output image: ")

img = cv2.imread(image_path)

msg = input("Enter secret message: ")
password = input("Enter password: ")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite(output_path, img)

os.startfile(output_path)

if input("Do you want to decrypt the image? (y/n)") != "y":
    exit()

# Read the encrypted image for decryption
encrypted_img = cv2.imread(output_path)

message = ""
n = 0
m = 0
z = 0

pas = input("Enter password for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message = message + c[encrypted_img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Invalid Password!")
