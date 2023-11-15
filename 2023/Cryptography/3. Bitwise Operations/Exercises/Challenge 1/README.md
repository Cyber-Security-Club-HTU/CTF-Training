**Description:**   Simple xor   :)

```Python
from pwn import xor

flag = b"*********************"
key = bytes.fromhex("37dcb292030faa90d07eec17e3b1")

bytes.hex(xor(flag, key))  # 7f88e7e9743cc6a18f1aa379d0ee43b481c04672
```
