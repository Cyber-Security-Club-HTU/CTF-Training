
### Data Types

The computer system uses a variety of *forms* that represent the same data. **We can use:**

- **Integer (` int `) values:** Range from 0-9, Example: 79, 80, 5, 1337.
- **String (`str`) values:** All printable characters. Example: "Hi !!!", "ONE1two2?".
- **Hexadecimal (`hex`) values:** Range From 0-9 and A-F. Example: 2A66FF32.
- **Binary (bin) value:** Range from 0-1. Example: 00110110101

>If I have the word "hello", I can convert it into another datatype by keeping its value. So the computer will still treat it as the word "hello" even if it is like this: 0x68656c6c6f.

---
### Conversion in Python:

**Writing in Python**
```Python
print("Apple") # string 
print(123321)  # intger
print(0x68656c6c6f) # hexadecimal (note the prefex "0x")
print("\x68\x65\x6c\x6c\x6f") # hexadicimal (note the "\x")
print(0b110001110) #  binary (note the prefex "0b")
```

**Int to hex**
```Python
hex_value = hex(123321)
print(hex_value) # 0x1e1b9
```

**Hex to int**
```Python
int_value = int("1e1b9", 16)
print(int_value) # 123321
```

**String to Hex**
```Python
hex_value = bytes.hex(b"Apple") # it will return it in (bytes), so decode() it
print(hex_value) # 4170706c65
```

**Hex to String**
```Python
str_value = bytes.fromhex("4170706c65").decode() # it will return it in (bytes), so decode() it
print(str_value) # Apple
```

>You can also use the `hexlify` and `unhexlify` functions from the *binascii* library.

---
### ASCII

As said before, each character (whether is it alphanumeric -letters and nums- or symbols) , all have an integer value equal to it. These values are organized and saved in a table called [ASCII table](https://www.johndcook.com/ascii.png).

```Python

# Get the charectre from int value
>> chr(65) # A
>> chr(36) # $ 

# Get the int value from the charecter
>> ord('a') # 97
>> ord('b') # 98

```

---
### Sending message in Cryptography

We will encounter later on different types of encryption. They all deal with numbers. No string text is involved. How is that?

 >You need install the `PyCryptodome` library using the following command to use the functions below.
 
```bash
pip3 install pycryptodome
```


**Text to numbers**
```Python
from Crypto.Util.number import bytes_to_long

msg = "I like cake" 

# Convert these bytes into a long intger (numbers)
m = bytes_to_long(msg.encode()) # the functions accepte it in bytes (by encoding it)

print(m)  # 88404700403956105303124837
```

**Numbers to text**
```Python
from Crypto.Util.number import long_to_bytes

m = 88404700403956105303124837 

# Convert this long intger into bytes (encoded text)
msg = long_to_bytes(m) # the function will return the text encoded (in bytes), you can decode() it if you want

print(m)  # b'I like cake'
```
