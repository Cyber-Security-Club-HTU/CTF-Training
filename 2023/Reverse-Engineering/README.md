# Welcome To Reverse Engineering Section

- **Reverse Engineering is one of the most interesting fields in cybersecurity and ethical hacking.** 
- **We’ll be focussing on simple ELF Linux executables for now, but feel free to discover reverse engineering windows exe executables and bytecode for JVM etc. So let’s get started!**

## What is Reverse Engineering?
```
In simple terms Reverse Engineering refers to the process of deconstructing any engineered object to figure out the internal mechanisms.

One example would be cracking games where crackers have to reverse engineer the game code on their PC in order to be able to distribute it for free.

Most software that is not open source (does not provide it’s source code) and instead we have the compiled executable code with us.

We have to in a way figure out what the soruce was (or a subset of it) from the executable code.

This in general is not easy to do so because machine/assembly code is far complex and also has a lot of compiler optimisations added to it.

In general the executable provided to us may not be binary or assembly instructions it could also be in the form of platform independent byte code that any virtual machine (say the Java virtual machine) executes.

We will however look at only Linux executables generated from C/C++ code in this tutorial as that provides a pretty great overview of the field. To do so however we must understand basic assembly.
```


