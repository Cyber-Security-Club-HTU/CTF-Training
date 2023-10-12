
### Caesar Cipher

An old *substitution cipher*, that needs 2 pieces information to work:
1. The message to be sent.
2. The key.

The *key* is a number that specifies how many chars in the alphabetic order we should walk over. For example, if we have the letter (A) and the key is 5, we will walk 5 chars, that is: B, C, D, E and F. The fifth character after (A) is (F). So the cipher text is (F). And if the plain text was "X" the cipher text is "C".

```Python
msg = "I LIKE CAKE"
cipher_text = ""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 5

# iterate over each char
for i in msg:
	# we don't want to deal with the space
	if(i == " "):
		cipher_text += " "
	# we get the new char from the index increased by the (key) value. (Notice the usage of mod "%" , to ensure that whenever we reach the last char num in the alphabet -which is number 26- we go again to index 0)
	else:
		cipher_text += alphabet[ (alphabet.index(i) + key) % 26  ]

print(cipher_text) # N QNPJ HFPJ

```

---
### ROT 13

This is the same as Caesar Cipher but with key of 13 (you can changed it if you want).

A good website for it is [this](https://rot13.com/).

---
#### Base64

It is not an encryption schema, but an encoding type. It changes the format of the data with the need to use a *key*. 

```Python
>> from base64 import b64encode, b64decode
>> b64encode(b"I like cake") # b'SSBsaWtlIGNha2U='
>> b64decode(b"SSBsaWtlIGNha2U=") # b'I like cake'
```

>The equal symbol (=) is a hint that tells us that this is a base64 encoded string.

There are also base32, base85, etc.

You can also also refer back to [CyberChef](https://gchq.github.io/CyberChef/) for quick decoding.