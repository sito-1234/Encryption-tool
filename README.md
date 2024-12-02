Encryption Tool

This Python-based tool provides basic encryption and decryption functionalities using symmetric encryption algorithms (e.g., AES). It is designed to securely encrypt and decrypt text data using a user-defined key. The tool allows users to input a message and generate an encrypted version, or decrypt an encrypted message back to its original form.
Features

    Encrypts and decrypts text data using AES (Advanced Encryption Standard).
    Supports user-defined keys for encryption.
    Generates encrypted and decrypted outputs in a human-readable format.

Requirements

    Python 3.x
    PyCryptodome library for encryption and decryption

Dependencies

To use this tool, you need to install the pycryptodome library, which provides the necessary encryption algorithms. You can install it using pip:

pip install pycryptodome

Installation

    Clone the repository:

git clone https://github.com/yourusername/encryption-tool.git
cd encryption-tool

Install the required dependencies:

    pip install -r requirements.txt

Usage

Once the tool is installed, you can use it to encrypt or decrypt text from the command line or by running it in an interactive environment.

To encrypt a message, use the following command:

python3 encrypt.py --encrypt "Your message here" --key "yoursecretkey"

To decrypt a message, use the following command:

python3 encrypt.py --decrypt "encryptedmessage" --key "yoursecretkey"

Example
Encrypting a Message

python3 encrypt.py --encrypt "Hello, this is a secret message!" --key "mysecretkey123"

Output:

Encrypted message: 98a76d445b6c86a478c7349cbbcd2f5f4b31fe3c3e3ac1bce3fa9f7a5a8a540f

Decrypting a Message

python3 encrypt.py --decrypt "98a76d445b6c86a478c7349cbbcd2f5f4b31fe3c3e3ac1bce3fa9f7a5a8a540f" --key "mysecretkey123"

Output:

Decrypted message: Hello, this is a secret message!

How It Works

The encryption tool uses the AES algorithm from the pycryptodome library to encrypt and decrypt messages.

    Encryption: The tool generates a ciphertext from the input message using the provided encryption key.
    Decryption: It takes the encrypted message (ciphertext) and the same key used for encryption, and then converts it back to the original plaintext message.

Example Code

Here’s a simple example of how the tool works internally:

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Encryption
def encrypt_message(message, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Decryption
def decrypt_message(iv, ciphertext, key):
    iv = base64.b64decode(iv)
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    return pt

Notes

    Security: The key you use for encryption should be kept private. Sharing it could expose your encrypted data.
    Key Size: Ensure that the key used is of appropriate length for AES (e.g., 16, 24, or 32 bytes for AES-128, AES-192, and AES-256, respectively).
    Padding: AES requires the input message to be padded to a multiple of the block size (16 bytes). This tool automatically handles padding and unpadding.

Troubleshooting

    Issue: ModuleNotFoundError: No module named 'Crypto'
        Solution: Ensure you have installed the pycryptodome library by running pip install pycryptodome.

    Issue: Decryption fails with an error.
        Solution: Ensure that the correct key and IV (Initialization Vector) are used for decryption. The key must be the same as the one used for encryption.
