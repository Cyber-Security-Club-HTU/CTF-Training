<div align="center">
<img src="https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/235393be-0c20-4c77-b178-5850cc7f5dc0">
</div>

## Table of Contents

- [What is a CTF?](#what-is-a-ctf)
- [Jeopardy-style CTF](#jeopardy-style-ctf)
- [Team Strategy & Roles](#team-strategy--roles)
- [Python for CTF](#python-for-ctf)
  - [Why use Python?](#why-use-python)
  - [Essential Python Libraries](#essential-python-libraries)
  - [Tips for Python in CTF](#tips-for-python-in-ctf)
- [Linux Commands for CTF](#linux-commands-for-ctf)
  - [General Utilities](#general-utilities)
  - [Searching](#searching)
  - [Networking](#networking)
  - [Binary & Data Analysis](#binary--data-analysis)
  - [File Operations](#file-operations)
  - [System Inspection](#system-inspection)
  - [Tips for Linux in CTF](#tips-for-linux-in-ctf)
- [Tips & Tricks](#tips--tricks)
- [Common Questions & Answers](#common-questions--answers)


## What is a CTF?
**CTF, or Capture The Flag, is a type of computer security competition where participants solve challenges across various categories to find flags and earn points.**

## Jeopardy-style CTF
**Jeopardy-style CTFs have a board of challenges categorized by topic and difficulty. Players select a challenge, solve it, and submit the flag to earn points.**

## Team Strategy & Roles

```
To efficiently tackle a Jeopardy-style CTF, a team can distribute roles based on the challenge categories:
```

**Web:** Someone familiar with web vulnerabilities, HTTP, and web debugging tools.
**Crypto:** Someone who understands encryption, hashing, and cryptographic algorithms.
**Reverse Engineering:** An individual skilled in analyzing binaries, understanding assembly, and using tools like gdb.
**Forensics:** A member proficient in data recovery, steganography, and file analysis.

```
Tips:
```

- Cross-train members to cover multiple categories.
- Maintain communication to discuss challenges and combine expertise.

## Python for CTF
```
Python is often the go-to language for CTF enthusiasts due to its simplicity and wide range of libraries.
```

### Why use Python?
- Versatile: Can be used for scripting, web requests, and even binary exploitation.
- Batteries Included: Rich standard libraries, no need for extra installations for many tasks.
- Vibrant Ecosystem: Many third-party libraries developed specifically for hacking and CTF tasks.
  
### Essential Python Libraries:

**pwntools:**
- Crafting exploits
- Working with binaries
- Networking tasks
- 
Example:
```python
from pwn import *
r = remote('ctf.example.com', 1234)
r.sendline('Hello CTF!')
```

**binascii:**
- Convert between binary and ASCII.
  
Examples:
```python
binascii.hexlify('hello')
binascii.unhexlify('68656c6c6f')
```

**PyCrypto:**
- Cryptographic operations like encryption, decryption, and hashing.
  
Example:
```python
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = obj.encrypt('Hello CTF!')
```

**requests:**
- Make web requests.
  
Example:
```python
import requests
response = requests.get('http://ctf.example.com/challenge')
print(response.text)
```

### Tips for Python in CTF:

- Familiarize yourself with Python's built-in functions.
- Use Python's dir() and help() functions to explore libraries.
- Automate repetitive tasks with Python scripts.

## Linux Commands for CTF
```
A strong understanding of the Linux command line is imperative for tackling CTF challenges. Here's a more comprehensive list:
```
### General Utilities:

`ls`: List files in a directory.
`cat`: Display contents of a file.
`echo`: Display a line of text.
`man`: Manual pages for commands.

### Searching:

`grep`: Search for text patterns within files.

Example: 
```
grep "flag" file.txt
```
`find`: Find files or directories.

Example: 
```
find / -name secretfile.txt
```

### Networking:

`nc (netcat)`: Networking utility.

Example:
```
nc ctf.example.com 1234
```
`nmap`: Network scanning tool.

Example: 
```
nmap -sV ctf.example.com
```

### Binary & Data Analysis:

`hexdump`: Display file in hexadecimal.

Example:
```
hexdump -C file.bin
```

`strings`: Extract strings from binaries.

Example:
```
strings file.bin
```
`binwalk`: Binary file analysis tool.

Example:
```
binwalk file.bin
```
`dd`: Convert and copy files.

Example: 
```
dd if=file.bin of=newfile.bin bs=1 skip=10
```

### File Operations:

`chmod`: Change file permissions.
`chown`: Change file owner and group.

### System Inspection:

`ps`: List running processes.
`netstat`: Network connections, routing tables, etc.
`lsof`: List open files.

### Tips for Linux in CTF:

- Combine commands using pipes (|).
- Read manual pages (man) for deeper understanding.
- Familiarize yourself with bash scripting for automation.

## Common Questions & Answers
Q: What if we can't solve a challenge?
A: It's okay! Learn from others' write-ups after the CTF.

Q: How to avoid burnout during a CTF?
A: Take breaks, hydrate, and ensure you have adequate rest.

```
Remember: CTFs are about learning and having fun. Every challenge you face teaches you something new. Good Luck! 🚩
```
