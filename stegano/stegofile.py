import cv2
import os
import string

img = cv2.imread(r"path of image to be encrypted with extension eg- C:\Users\Desktop\stegano\img.jpg ")

msg = input("Enter secret message: ")

password = input("Enter password: ")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

m=0;
n=0;
z=0;

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite(r"path of image to be decrypted with entension eg- C:\Users\Desktop\stegano\Encryptedmsg.jpg",img)

os.system("start Encryptedmsg.jpg")

if input("do you want to decrypt the image? (y/n)") != "y":
   exit()

message =""

n=0
m=0
z=0

pas = input("Enter password for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decrypted message: ",message)
else:
    print("Invalid Password!")
