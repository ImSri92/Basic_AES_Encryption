from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

output_file = 'encrypted.bin'
data = b'erick is in the class'
key = get_random_bytes(32)

cipher = AES.new(key, AES.MODE_CFB)
ciphered_data = cipher.encrypt(data)

file_out = open(output_file, "wb")
file_out.write(cipher.iv)
file_out.write(ciphered_data)
file_out.close()

file_in = open('encrypted.bin', 'rb')
iv = file_in.read(16)
ciphered_data = file_in.read()
file_in.close()

cipher = AES.new(key, AES.MODE_CFB, iv=iv)
original_data = cipher.decrypt(ciphered_data)
print(original_data.decode('UTF-8'))