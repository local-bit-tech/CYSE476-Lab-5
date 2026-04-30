#module that allows for a person to use AES protocol
from Crypto.Cipher import AES


#turn plaintext, ciphertext, and iv into bytes
plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")

file = r"C:\Users\yassa\CYSE476-Lab-5-1\Task 2\keys.txt"

#open the file and read it
with open(file, "r") as f:
    #parse through each line of the file
    for line in f:
        #strip the lines and turn them into bytes
        key = bytes.fromhex(line.strip())
        
        #create a cipher from the key and iv then encrypt plaintext
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext_to_check = cipher.encrypt(plaintext)


        #check if the ciphertext we generated matches ciphertext we have
        #if it does, then print the key
        if ciphertext_to_check == ciphertext:
            print(f"{line.strip()}")

