from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes



plaintext = "255044462d312e350a25d0d4c5d80a34"
ciphertext = "d06bf9d0dab8e8ef880660d2af65aa82"
iv = "09080706050403020100A2B2C2D2E2F2"

with open(r"C:\Users\yassa\Downloads\keys.txt", "r") as f:
    for line in f:
        key = line.strip()
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(plaintext, AES.block_size)
        ciphertext_to_check = cipher.encrypt(padded_data)

        if ciphertext_to_check.hex() == ciphertext:
            print(f"Key found: {key}")
            break
