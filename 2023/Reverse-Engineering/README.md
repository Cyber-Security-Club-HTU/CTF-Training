# Welcome To Reverse Engineering Section

*Reverse Engineering is one of the most interesting fields in cybersecurity and ethical hacking.*

*Through this training we’ll be focussing on simple ELF Linux executables for now, but feel free to discover windows exe executables and bytecode for JVM etc...*
*So let’s get started!*

## What is Reverse Engineering?


In simple terms Reverse Engineering refers to the process of deconstructing any engineered object to figure out the internal mechanisms.

One example would be cracking games where crackers have to reverse engineer the game code on their PC in order to be able to distribute it for free.

Most software that is not open source (does not provide it’s source code) and instead we have the compiled executable code with us.

We have to in a way figure out what the soruce was (or a subset of it) from the executable code.

This in general is not easy to do so because machine/assembly code is far complex and also has a lot of compiler optimisations added to it.

In general the executable provided to us may not be binary or assembly instructions it could also be in the form of platform independent byte code that any virtual machine (say the Java virtual machine) executes.

We will however look at only Linux executables generated from C/C++ code in this tutorial as that provides a pretty great overview of the field. To do so however we must understand basic assembly.


## Introduction to x86 Assembly

x86 Assembly is the assembly instruction code used by the non ARM (Intel/AMD) processors and most CTF problems will use this instruction code. 

The instructions generated may vary from OS to OS and we will consider linux executables (ELF format). 

Also before proceeding note that there a variety of different assembly syntaxes, we will be using Intel Assembly syntax in this tutorial although the alternative AT&T syntax is also quite common.

Assembly language has very few constructs compared to higher level languages, instead having to rely on some primitive operations. 

Most assembly operations happen with respect to registers, which are special memory locations on the CPU which is way faster than directly accessing RAM and a lot of special values are stored here. 

```
We will first go through these registers and their naming conventions.
```

### Registers

A register can be thought of as a special memory location in the CPU. 
There are 6 general purpose registers and 2 special registers available. 

We can do all possible assembly operations on these registers like adding values, subtracting etc.

```
The 8 registers are named as EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP.
```

However if you go through any assembly code you will see various variations in the register names. 

There are different ways in which you can call different registers. 
The above naming provides you access to the 32 bits associated with every register. 

Nowadays in 64 bit systems each register is allocated 64 bits which can be called by using the names RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP.

Similarly if you want only 16 bits you will call them as AX, BX, CX.. and so on. To get eight bits you will use AL, BL, CL.. and so on. 

```
The following diagram explains this better:
```
![image](https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/bfab3919-3404-4cbb-bf55-943b16bcddf6)
