from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configuration
key = bytes.fromhex("95fa2030e73ed3f8da761b4eb805dfd7")
data = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")

cipher = AES.new(key, AES.MODE_CBC, iv)

# 2. Pad data to 16-byte blocks and encrypt
padded_data = pad(data, AES.block_size)
ciphertext = cipher.encrypt(padded_data)

print(f"IV (hex): {iv.hex()}")
print(f"{ciphertext.hex()}"[:32])