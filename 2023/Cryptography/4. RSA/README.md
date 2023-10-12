
### Introduction

RSA is a *Public Key cryptography* schema or *asymmetric*. *Asymmetric cryptography* means that the key used for encrypting the plain text originally, *isn't* the same key used for decrypting the cipher text back to the plain text.

- It is ok if you share the the *public key* with anyone (used for encryption).
- It is prohibited to share the *private key* with others (used for decryption).

RSA is based on many mathematical theories, such as Number Theory, such as prime numbers, GCD. As well as modular arithmetic.

>We won't discuss these topics here, you can refer to the resources sections for more details.

---
### RSA Elements

**Any RSA cryptography schema must have at least these elements:**

- `N`, a number to be used in the mod `%` .
	- It can be the product of 2 primes (p, q), `N = p * q` .
	- It can be a large prime number.
- `e` , a *public* exponent ( x<sup>e</sup> ).
	- Its value depends on how `N` was calculated.
	- Should be *relatively prime* with Φ(N), i.e. GCD(e, Φ(N)) = 1.
	- Range between ( 1 - Φ(N) ).
- `d`, *private* exponent ( x<sup>d</sup> ).
- `m` , the message or the plain text (in numbers).
- `c`, the cipher text (in numbers).

>The `d` value isn't provided to us in CTFs, as our task is to find it in order to decrypt the `c` .

---
### Encryption & Decryption

The cipher text (c) = m<sup>e</sup> mod N   ....   `pow(m, e, N)`
The plain text (m) =  c<sup>d</sup> mod N    ....   `pow(c, d, N)`

###### *How to find `d` ?*

- *`d` is the multiplicative inverse of `e` in Z<sub>Φ(n)</sub> .*

**The totient (Φ/phi) value's calculation includes these cases:**
- **If `N` is prime number:** Φ(N) = N - 1 .
- **If `N` is the product of `p` and `q`:**  Φ(N) = (p-1) * (q-1) .

**Then you can find `d` by one of the following:** 
- `pow(e, -1, totient)` .
- `inverse(e,phi)` .
- Custom code based on Extended Euclidean Algorithm (EEA).

##### Example

*Encryption*
```Python
# Importing necessary functions
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

# Convert our plain_text bytes into long integer
message = b"I like Knafa"
m = bytes_to_long(message)

# Initlizing (N)
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N = p*q

# A well-known value for (e)
e = 65537

# Calulateing the cipher text
c = pow(m, e, N)

print(c) # 441837959981949163835043777463786349350671322257423955619294
```

Decryption
```Python
# Importing necessary functions
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

e = 65537
c = 441837959981949163835043777463786349350671322257423955619294

# we need to find phi(N)
phi = (p-1) * (q-1)

# Calulate private key (d)
d = pow(e, -1, phi)
# d = inverse(e, phi)

# Retrieve the plain text
m = pow(c, d, N)
message = long_to_bytes(m).decode()

print(message) # I Like Knafa
```

>If `p` or `q` are not given, you can use Factordb library to get the primes factors of `N`.
>Keep in mind that it mightn't always be able to get the factors.

---
### Low exponent attack

We might encounter a small value for `e`, in this case we have 2 situations:
- **if (m<sup>e</sup> < N)** , so simply:
	c = m<sup>e</sup>,      thus,   m = <sqrt></sqrt> c<sup>1/e</sup> 
- **If (m<sup>e</sup> > N),** in this case we need to keep adding the value of `N` to `c` until we find the correct value for `c` .

*In python*
```Python
# Importing necessary functions
from gmpy2 import iroot

while True:
		try:	
			m = iroot(c,e)[0]
			print(long_to_bytes(m).decode())
			break
		except:
			c += N
```

>You can notice that we were able to retrieve `m` without the need to calculate `d` .