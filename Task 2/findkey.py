from Crypto.Cipher import AES



plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")


with open(r"C:\Users\yassa\Downloads\keys.txt", "r") as f:
    for line in f:
        key = bytes.fromhex(line.strip())
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext_to_check = cipher.encrypt(plaintext)

        if ciphertext_to_check == ciphertext:
            print(f"{line.strip()}")
            break
