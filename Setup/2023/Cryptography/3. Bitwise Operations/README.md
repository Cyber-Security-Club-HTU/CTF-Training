
These operations allows you manipulate the data binary, which results in a different value. We may use them for encrypting our data for example.

We will talk about some of them.

---
### XOR (`^` , ⊕)

We know the in binary: 0 is false, 1 is true. `XOR` works by comparing the binary bits and asks itself on each round: "*Are they different?*", if yes print 1, 0 otherwise.

**Example:**
```
01001100
01101010
------------
00100110
```

In Python, if we use the xor symbol operator `^`, we need to give it 2 integers values like this:
```Python
>> 41^9 # 56
>> 3^3  # 0
```

However, we can use the function `xor()` from `pwntools` library, and give it any 2 arguments, even different types and lengths, as it will do the work of converting them to binary and comparing them.
```Python
from pwn import xor

xor(b"apple", b"mange")
xor(b"banana", b"1337")
```

>make sure to supply the parameters in *bytes* format.

 >Note that integers will be treated in this function as an ASCII value, not the real integer value. You can xor integers directly through the `^` operator.
 
##### XOR Properties
```
- Commutative:  A ⊕ B = B ⊕ A  ...  order is not important.

				A ⊕ B = C
				A ⊕ C = B
				C ⊕ B = A


- Associative:  A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C  ...  same priority, brackets has no effect.

- Identity:     A ⊕ 0 = A   ...  xoring with 0 does nothing.

- Self-Inverse: A ⊕ A = 0   ...  xoring itself returns 0.
```

**Example**
```Python
from pwn import xor

# those given value are intended to be in hex
red = "a6c8b6733"
blue = "626c7565"

# so, we need to make them in bytes

red = bytes.fromhex(red)
blue = bytes.fromhex(blue)

# xoring itself
print(xor(red, red)) # 0

# first 2 return 0, then Identity case
print(xor(red, red, blue)) # blue (the ascii chars converted from the resulted hex)

# Replacing the places results the missing one
print(xor(red, blue)) # b'\xc4\xa4\xc3\x16^'
print(xor(red, b'\xc4\xa4\xc3\x16^')) # blue 
```

---

### Bit Shifting 

There are other methods used to manipulate the bits of some data. ***Left shifting*** (`<<`) and ***Right Shifting*** (`>>`) were used originally to fasten the mathematical calculations, however now, most programming languages do that by default behind the scene.

**Left shifting (`<<`)**

The idea is to convert a given value to binary, and then *adding* *one bit* (0) from the right.

```
101011  (Before left shifting)
1010110 (after left shifting)
```

- The resulted value is *larger*.
- It is preformed on *numbers*.

**Examples**
```Python
10 << 1  # 20
10 << 2  # 40
10 << 15 # 327680
```

>Mathematically, it is as same as multiplying the given number by  2<sup> shift_value</sup>  
>So, 10 * 2<sup> 1</sup> = 20
>      10 * 2<sup> 2</sup> = 40
>      10 * 2<sup> 15</sup> = 327680


**Right shifting (`>>`)**

The idea is to convert a given value to binary, and then *removing* *one bit* from the right.

```
1010110  (Before right shifting)
101011 (after right shifting)
```

- The resulted value is *smaller*.
- It is preformed on *numbers*.

**Examples**
```Python
100 >> 1  # 50
100 >> 3  # 12
100 >> 15 # 0
```

>Mathematically, it is the floor division (`//`) of the given number by  2<sup> shift_value</sup>  
>So, 100 // 2<sup> 1</sup> = 5
>      100 // 2<sup>3</sup> = 12 (originally 12.5, but we only get the integer)
>      100 // 2<sup>15</sup> = 0

