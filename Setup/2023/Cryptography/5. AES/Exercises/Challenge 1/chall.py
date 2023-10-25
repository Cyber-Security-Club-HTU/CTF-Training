from Crypto.Cipher import AES
from random import randint
from secrets import FLAG

words = []

with open("wordlist.txt", "r") as f:
	for line in f.readlines():
		words.append(line.strip())


key = words[randint(0, len(words))].encode()

cipher = AES.new(key, AES.MODE_ECB)

cipher_text = cipher.encrypt(pad(FLAG, 16))

print(bytes.hex(cipher_text))
# 176ef67980307afbbedaccd44f8c89518895b1c94a65b5473b05f94f7e68ac7dc4421b4690defcc3b05a9582ef0bd33f