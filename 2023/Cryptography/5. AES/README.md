
### Introduction

Advanced Encryption Standard (AES) is a symmetric schema. Symmetric cryptography means that the key used for encrypting the plain text originally, *is* the same key used for decrypting the cipher text back to the plain text.

AES deals with data as *blocks*. It takes every 16 bytes (or 32 bytes) from the plaintext and feeds them into the encryption function, and returns back a block of the ciphered text. Next, we get the next block and puts in under encryption.

**There are 2 famous types of AES:**
- **AES-128:** It means that each block is 128 bits long, that is, 16 bytes.
- **AES-256:** It means that each block is 256 bits long, that is, 32 bytes.

---
### Some terms

- **Initialization Vector (IV):** It is a value used in the encryption/decryption process. It has the same size as the block. It's purpose is to increase the secrecy and make the encryption schema stronger.
- **Padding:** It is the process of adding random data until the desired size or length of the data is satisfied.

---
### AES modes

We have many modes that can be used to encrypt our data using AES. They differ on how operations are carried and performed against the plaintext. Every mode has some vulnerabilities, thus, some modes are less secure than others.

##### ECB (Electronic Code Book) mode (AES-ECB)

- This mode is the least secure.
- It takes every 16 bytes and encrypt it separately.
- If the block size is less than 16 bytes, *pads* it.

![[Pasted image 20231012160206.png]]

```Python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# Prepare the key (as bytes)
key = b"This is my key!!"
data = b"secret_message"
# Create an AES object (instance) for encryption
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt the plaintext
cipher_text = cipher.encrypt(pad(data))

# ------------------------------------------


# Create an AES object (instance) for decryption
decrypt_cipher = AES.new(key, AES.MODE_EBC)

# Decrypt the ciphertext
plain_text = unpad(decrypt_cipher.decrypt(cipher_text), 16)

```

##### CBC (Cipher Block Chaining) mode (AES-CBC)

The encryption process in this mode works as EBC in terms of blocks, however there are slightly different things. The first block of the plain text is xored with the I.V, then is passed into the encryption function. The other blocks is the same, but instead of exoring them with the I.V, they are xored with the previous encrypted block.

![[Pasted image 20231010152812.png]]

- This has better security mechanisms than EBC.
- We must have a random I.V. This will get xored with the first plaintext block. It give also some randomness to the encryption process.
- Even we have same identical plaintext blocks, they don't have the same ciphertext value.

 *Encryption* 

```Python
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
import os

# Our secret data (plaintext) to be encrypted.
data = b"secret"

# Assign the KEY value with random characters of size 16 bytes.
key = os.urandom(16)

# Assign the I.V value with random characters of size 16 bytes.
iv = os.urandom(16)

# Create an AES cipher object with CBC mode, with value for the key and  I.V passed to it.
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad out data first to ensure we have a full blocks, then encrypt our data.
ciphertext = cipher.encrypt(pad(data, AES.block_size))

print(b64encode(iv)) # b'tJhswkibmrtmzn75+9f30w=='
print(b64encode(ciphertext)) # b'D7AkGDPIFvY57FO+MG/P4Q=='
```

 *Decryption* 

```Python
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad

# Given data is neseery to perfrom decryptio
ciphertext = b64decode(b'D7AkGDPIFvY57FO+MG/P4Q==')
iv = b64decode(b'tJhswkibmrtmzn75+9f30w==')
key = b64decode(b'EVneCPO5yI9/jQBD8ITC+w==') # Shouldn't be given, but we assume that we have it.

# Create an AES cipher object with CBC mode, with value for the key and  I.V passed to it.
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt our data, then unpad to ensure we remove null bytes.
plaintext = unpad(cipher.decrypt(ciphertext), 16)

print(plaintext) # b'secret'
```

---
### Common attacks

##### ECB - Oracle

The idea simply is based on bruteforcing the `secret_value` or the `flag` in CTFs. Where we are told that (our input) + (FLAG) is being encrypted, not only our input.

```Python
from Crypto.Cipher import AES

flag = "******"
key = ********

data = input() + flag
padded = pad(data.encode(), 16)

cipher = AES.new(KEY, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded)
```

The vulnerability exists in the way ECB work. It encrypts every block separately according to a prespecified block size. And if the text size still less than the block size, random data will be appended till the required size.

*Example:*
```Python

block_size = 16
flag = "I_like_eating_cake"
_input = "A"*15

|      16 bytes    |     16 bytes	  |
| AAAAAAAAAAAAAAAI | _like_cake000000 |
```

**Attack approach:**
1. We will give an input of size 15, so 1 character from the flag will be inserted in the first block.
2. We will encrypt it and get the first encrypted block (first 16 chars), and put it aside.
3. Start encrypting our input, but by replacing the last character (in place of "I"), and trying each possible character.
4. We will trunk the encrypted text to get the first block.
5. Compare this block with the first block we have put it aside.
6. If it is the same encrypted text, then that tried character was the correct first character of the flag (because it gave us the same ciphertext).
7. We will keep decrementing our input size by the number of the reveled flag characters, as we keep going over and over until we retrieve the hidden flag.