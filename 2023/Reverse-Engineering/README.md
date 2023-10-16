# Welcome To Reverse Engineering Section

**Reverse Engineering is one of the most interesting fields in cybersecurity and ethical hacking.**

Through this training we’ll be focussing on simple ELF Linux executables for now, but feel free to discover windows exe executables and bytecode for JVM etc...
So let’s get started!

## What is Reverse Engineering?

**In simple terms Reverse Engineering refers to the process of deconstructing any engineered object to figure out the internal mechanisms.**

One example would be cracking games where crackers have to reverse engineer the game code on their PC in order to be able to distribute it for free.

Most software that is not open source (does not provide it’s source code) and instead we have the compiled executable code with us.

We have to in a way figure out what the soruce was (or a subset of it) from the executable code.

This in general is not easy to do so because machine/assembly code is far complex and also has a lot of compiler optimisations added to it.

In general the executable provided to us may not be binary or assembly instructions it could also be in the form of platform independent byte code that any virtual machine (say the Java virtual machine) executes.

We will however look at only Linux executables generated from C/C++ code in this tutorial as that provides a pretty great overview of the field. To do so however we must understand basic assembly.


## Introduction to x86 Assembly

**x86 Assembly is the assembly instruction code used by the non ARM (Intel/AMD) processors and most CTF problems will use this instruction code.**

The instructions generated may vary from OS to OS and we will consider linux executables (ELF format). 

Also before proceeding note that there a variety of different assembly syntaxes, we will be using Intel Assembly syntax in this tutorial although the alternative AT&T syntax is also quite common.

Assembly language has very few constructs compared to higher level languages, instead having to rely on some primitive operations. 

Most assembly operations happen with respect to registers, which are special memory locations on the CPU which is way faster than directly accessing RAM and a lot of special values are stored here. 

```
We will first go through these registers and their naming conventions.
```

### Registers

**A register can be thought of as a special memory location in the CPU.**

**There are 6 general purpose registers and 2 special registers available.**

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

One more important thing to note is that ESP and EBP are used to store the memory location of the stack. 
ESP points to the top of the stack and EBP (generally) refers to the bottom.

Declaring variables on the stack would therefore be equivalent to adding and subtracting values from ESP and EBP. 

```
Note that you generally don’t need to know the exact specifics but having a vague idea works.
```

There are also a couple of FLAGS that are used by assembly. Think of a flag as a specific boolean variable which is set by assembly instructions. 

Some flags are the zero flag, the sign flag etc. 
We will mostly be needing the zero flag in reverse engineering since this flag is used many times to determine control flow.

### Basic Assembly Operations

`mov operation`

**The mov operation is one of the simplest operations and all it does is moves values (or assigns values).**

The syntax of mov is the following:

```assembly
mov destination, source
```

Suppose I want to set the value 12 in EAX then I would run the operation:

```assembly
mov eax, 12
```

One more thing to understand is dereferencing. This is similar to C. Suppose the register ECX holds the value 0x6665f which is a memory location. 

**ECX is therfore similar to a pointer. If I want to load the value stored at 0x6665f into EAX I will use the following command:**

```assembly
mov eax, [ecx]
```

**The brackets [] functions similar to * in C/C++ and it dereferences the memory location and outputs the value at that location.**

`add operation`

**This is pretty simple. Consider the following assembly code:**

```assembly
add eax, ebx
```

This is equivalent to:

```assembly
eax = eax + ebx
```

`sub operation`

**This is similar as well. Consider the following assembly code:**

```assembly
sub eax, ebx
```

This is equivalent to:

```assembly
eax = eax - ebx
```

`cmp operation`

**This is a very useful operation and is used for comparing values.**

**The result of this operation can be combined with jump operations to dictate control flow. Consider the following code:**

```assembly
cmp ecx, 15h
jz 0x7eb
```

**Let’s see what this does. The cmp command compares the values given to it, in this case it is the value stored in ecx and the value 21 given as hexadecimal.**

cmp essentially subtracts these two values and sets some FLAGS which we talked about before. Here if both the values are equal then the subtraction will be 0 and so the ZERO flag will be set.

The next instruction jz stands for “jump if zero”. 

Thus if the zero flag is set the program jumps to the code location charactersised by 0x7eb address (this is easily seen by using a debugger). 

Thus this is similar to an “if” statement.

Turns out we can use such commands clever to construct for, while and other loops. We will go through this in the next article. 

Instead of using jz if we used jle the jump would have happened if ecx <= 15h was satisfied. Indeed a variety of such conditionals can be used to simulate control flow.

`test operation`

**This is similar to cmp except it computes the binary AND instead of subtracting. Thus if the binary AND of the two inputs given is 0 then the zero flag is set.**

**The following C conditional can thus be easily translated into assembly:**

```c
if (eax == 0){
	// do stuff
}
```

**The corresponding assembly will be:**

```assembly
test eax, eax
jz location_to_do_stuff
```

`lea operation`

**This is the final operation that we will see here. This is similar to mov but instead of copying the value it copies the address.**

```assembly
lea eax, [ecx]
```

**The above code will copy the value stored in ecx (that is, the address) into eax. Observe that mov would have copied the value stored in the address stored in ecx.** 

Thus lea loads the address instead of the value. It stands for **load effective address**.

Now, because we wanna get work done and achieve the flag in CTFs, we will jump into tools and how to get the flag with several plans and scenarios that we are capable of doing with these tools.

[Continue Here](https://github.com/Cyber-Security-Club-HTU/CTF-Training/tree/main/2023/Reverse-Engineering/Tools)
