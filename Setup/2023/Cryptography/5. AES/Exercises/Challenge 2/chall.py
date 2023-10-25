from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long,long_to_bytes
from os import urandom

FLAG = b"************"

key = urandom(16)
iv  = urandom(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

ciphertext = cipher.encrypt(pad(FLAG, 16))

rand1 = bytes.hex(urandom(16))
rand2 = bytes.hex(urandom(16))

key   = int(bytes.hex(key), 16)
rand1 = int(rand1, 16)
rand2 = int(rand2, 16)

rand3 = rand1 ^ rand2
rand4 = (rand3 ^ key) + 1337

print(rand1) # 35964950056845805491914361496267951738
print(rand2) # 43856906863402926175407203532798990466
print(rand4) # 199214885439756744209517727923393517387
print(bytes_to_long(iv)) # 275802377685853184357075818678849513367
print(bytes_to_long(ciphertext)) # 31450203249802901495471219163548391181562914760617313226640491700833710123188715546181501122534673126063235088663959

