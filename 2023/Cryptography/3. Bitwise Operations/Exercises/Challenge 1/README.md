**Description:**   Simple xor   :)

```Python
from pwn import xor

flag = bytes.fromhex("*********************")
key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1")

xor(flag, key1) # 4854557b6778ecd6cd6940c8cfa436a94586cc
```
