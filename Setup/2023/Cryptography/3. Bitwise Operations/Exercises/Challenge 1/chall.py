from pwn import xor

flag = bytes.fromhex("*********************")
key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1")

xor(flag, key1) # 4854557b6778ecd6cd6940c8cfa436a94586cc

------
from secrets import KEY1, KEY2, KEY3

# flag = 0x4854557b7830725f69355f61737330633161743176337d
flag = *****************

KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 = 0x911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d
# KEY3 = 0x504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc

print(hex(KEY1^KEY2)) # 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
print(hex(KEY2^KEY3)) # 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
print(hex(KEY1^KEY2^KEY3^flag)) # 0x679ce16d00b02cd59091d04767ae47963170d1660df7f56f5faf