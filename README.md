# Basic_AES_Encryption
Basic AES with IV
This script demonstrates AES encryption and decryption using a Cipher Feedback (CFB) mode.

It encrypts a sample data string using AES with a randomly generated key and saves the encrypted data to a file.
Then, it reads the encrypted data from the file, extracts the initialization vector (IV) and ciphertext,
and decrypts it back to the original data.

Libraries Used:
    - Crypto.Cipher: AES encryption and decryption functions
    - Crypto.Random: Generating random bytes for the encryption key

Note: This script is for educational purposes and should be used responsibly.
