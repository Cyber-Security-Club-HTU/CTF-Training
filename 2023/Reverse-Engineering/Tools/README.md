<div align="center">
<img src="https://hex-rays.com/wp-content/themes/hx2021/dist/img/how-it-works.png">
</div>

# Reverse Engineering Tools

**Welcome to the dynamic world of Reverse Engineering in Capture The Flag (CTF) challenges! If you're a beginner, you might be wondering what reverse engineering is.**

At its core, reverse engineering is the process of understanding and dissecting software, usually binaries, to uncover its internal workings or to find vulnerabilities. 

**In the context of CTFs, your primary goal is often to retrieve a hidden message or "flag" embedded within software or to understand how a program functions to exploit it.**

```
Most of the time your aim is to get a flag, but some challenges gives you a link or a clue for another challenge
(which is a completion of the first challenge) that will have the flag.
```

Now, diving straight into a binary without any tools would be like trying to read a book in the dark. To save time and work efficiently, we rely on a suite of specialized tools. 

These tools won't do the work for you, but they will shine a light on the code, making your task much more manageable. Remember, the end goal is to find the flag, and these tools, when used correctly, can significantly speed up that process.

```
Here are some of the fundamental tools categories that can help you:
```

- **Disassemblers:** These break down binary files (executables) into assembly code, making it readable and easier to understand. Examples include IDA Pro, `objdump` and Ghidra.
- **Debuggers:** They allow you to pause, inspect, and manipulate a running program, essential for understanding how software works and for identifying vulnerabilities. Popular choices are GDB and OllyDbg.
- **Hex Editors:** These are used to view and modify the binary data of a file directly. Tools like HxD or Hex Fiend come in handy.
- **String Extractors:** Often, binaries contain readable strings that can provide hints or even direct answers. The `strings` command on Linux is a simple yet effective tool for this.
- **Decompilers:** These attempt to translate binary files back into high-level source code. Ghidra and IDA Pro come with decompiler functionalities.
- **Dynamic Analysis Tools:** Tools like `strace` and `ltrace` on Linux can trace system calls made by a program, which can be instrumental in understanding its behavior.
- **Scripting and Automation:** Sometimes, repetitive tasks can be automated using scripting languages like Python. Tools like pwntools can aid in this.

## Initial Steps for Analyzing Binaries

**Before you begin, it's essential to note that the tools and techniques mentioned here are primarily focused on reversing ELF (Executable and Linkable Format) Linux binaries.**

**It won't cover EXE (Windows) or JVM-based binaries. It's highly recommended to use a Linux distribution such as Kali for these tasks.**

**To read the tools manual:**

```bash
man <tool-name>
```

**If you find that any tool is missing, you can easily install it using:**

```bash
sudo apt install <tool-name>
```

### When you first encounter a binary during a CTF or any reverse engineering task, there are a few immediate steps you should take to get a better sense of what you're dealing with.

### 1. Identify the Binary Type

Before diving into deeper analysis, understand what kind of file you're dealing with.

Usage:
```
file <binary-name>
```

The `file` command will provide you with essential information about the binary, like whether it's an ELF binary, a script, or some other format.

### 2. Check If the Binary Is Stripped

When a binary is "stripped", it means most of its debugging and symbol information (like function names) have been removed. 

This can make reverse engineering more challenging, as you won't have those helpful names as a reference.

Usage:
```
objdump -t <binary-name> | grep ".debug"
```

If you see no output, it's likely that the binary is stripped. If there's output, it means there are debugging symbols present.

### 3. Make the Binary Executable

Before you can run the binary, you need to ensure it has the necessary permissions.

Usage:
```
chmod +x <binary-name>
```

This command grants executable permissions to the binary, allowing you to run it.

### 4. Execute the Binary

Sometimes, running the binary can give immediate hints or feedback. Always do this in a controlled environment to avoid potential harm.

Usage:
```
./<binary-name>
```

### 5. Check for Readable Strings

As mentioned before, the `strings` command can be used to extract readable character sequences. This can sometimes provide immediate hints or even the flag.

Usage:
```
strings <binary-name>
```

### 6. Inspect Binary Headers

Examining the headers of an ELF binary can provide insights into its structure and various properties, such as its entry point, section headers, and more.

Usage:
```
readelf -h <binary-name>
```

### 7. Examine Dependencies

Checking the shared libraries the binary depends on can sometimes provide clues or help in understanding its functionality.

Usage:
```
ldd <binary-name>
```

Following these initial steps will give you a clearer understanding of the binary's nature and its potential behavior. 

---

Once you've gathered this foundational knowledge, you can proceed with deeper analysis and employ more advanced tools and techniques as needed.

Remember, reverse engineering is as much an art as it is a science. While these steps provide a starting point, your intuition, experience, and creativity will play crucial roles in your journey.

### 7. Ghidra

Ghidra is both a disassembler and a decompiler. While not run directly from the command line like the other tools, Ghidra provides an extensive GUI for analyzing binaries in-depth.


## Advanced Steps for Binary Analysis

After conducting the initial analysis and understanding the basic properties of the binary, it's time to dive deeper. 

The following steps will guide you further in your reverse engineering journey.

### 8. Dynamic Analysis

Dynamic analysis involves observing the binary while it's running. This method can provide insights into the binary's behavior and any runtime changes it might make.

#### a. Debugging with GDB

GDB, the GNU Debugger, is a powerful tool that allows you to pause, inspect, and manipulate a running binary.

Usage:
```
gdb ./<binary-name>
```

Within GDB, you can set breakpoints, inspect memory, modify values, and more.

#### b. Tracing System Calls

`strace` can be used to trace the system calls made by the binary, which can provide insights into its interactions with the OS.

Usage:
```
strace ./<binary-name>
```

### 9. Disassembly and Decompilation

Disassembly translates the binary into assembly code, while decompilation tries to produce higher-level code from the binary. 

These methods help you understand the binary's inner workings.

#### a. Using objdump for Disassembly

`objdump` provides a detailed disassembly of the binary.

Usage:
```
objdump -d <binary-name>
```

#### b. Ghidra for Decompilation

Ghidra provides an extensive GUI that facilitates both disassembly and decompilation, making it easier to analyze the binary.

### 10. Analyzing Memory and Binary Protections

Before attempting exploitation, it's crucial to understand any protections the binary might have.

#### a. Check for Stack Canary

Stack canaries are values placed on the stack to detect buffer overflows.

Usage:
```
objdump -R <binary-name> | grep "__stack_chk_fail"
```

If the command produces output, the binary might be using stack canaries.

#### b. Examine NX (No eXecute) Bit

The NX bit determines which parts of memory can be executed, providing protection against certain exploits.

Usage:
```
readelf -l <binary-name> | grep GNU_STACK
```

### 11. Manual Code Analysis

While tools are invaluable, sometimes manually examining the code is necessary. Look for patterns, familiar constructs, or any logic that stands out. 

Over time, as you gain experience, you'll develop an intuition for identifying areas of interest.

### 12. Reproduce and Exploit

If you identify vulnerabilities or potential exploit vectors, try to reproduce them consistently. Once you can reliably trigger certain behaviors, focus on how to leverage them to achieve your goal (like extracting the flag).

---

Throughout your reverse engineering journey, remember to maintain a systematic approach, document your findings, and always be on the lookout for clues, no matter how subtle. 

Each binary presents a unique puzzle, and your ability to adapt, learn, and think creatively will be the keys to your success.


## Deep Dive into GDB and Working with Stripped Binaries

GDB is a cornerstone tool for reverse engineers, especially when analyzing binaries. 

Even when the binary is stripped, there are methods to navigate and analyze it efficiently using GDB.

### 13. Setting Breakpoints in GDB

When you're debugging a program, setting breakpoints allows you to halt the program's execution at specific points, inspect its state, and observe its behavior from that point onward.

#### a. Breaking on `main`

Typically, the `main` function serves as the entry point for execution in programs written in languages like C and C++. Setting a breakpoint on `main` lets you start your analysis from the program's beginning.

Usage within GDB:
```
break main
run
```

Once the program hits the `main` breakpoint, it will pause, and you can use GDB commands to inspect and manipulate the program state.

### 14. Navigating Stripped Binaries

If a binary is stripped, the debugging symbols like function names are removed. This can make the analysis more challenging, but not impossible.

#### a. Finding the Entry Point

For stripped binaries, the `main` function's symbol might be absent. However, you can still locate the program's entry point.

Usage:
```
info files
```

Within the output, look for an "Entry point" value. This value represents the program's entry point in memory.

#### b. Setting Breakpoint at the Entry Point

Once you've identified the entry point, you can set a breakpoint in GDB using the memory address.

Usage within GDB:
```
break *0x<entry-point-address>
run
```

Replace `<entry-point-address>` with the address you found earlier.

#### c. Navigate Through the Code

Once you're at the entry point, you can step through the code using the `step` or `next` commands in GDB. 

These allow you to move line by line, diving into functions or skipping over them, respectively.

### 15. Examining Memory and Registers

When you hit a breakpoint, you can inspect the program's state, including its memory and registers.

#### a. Viewing Registers

To see the values of CPU registers:
```
info registers
```

#### b. Examining Memory

To view memory contents at a specific address:
```
x/<format> <address>
```

Replace `<format>` with your desired output format (e.g., `x` for hexadecimal, `s` for string) and `<address>` with the memory address you're interested in.

### 16. Dealing with Functions in Stripped Binaries

While function names are stripped, the function's code remains intact. You can identify function boundaries and behavior patterns by analyzing loops, calls, and jumps.

Using tools like Ghidra in tandem with GDB can help you map out these functions, even if they're nameless, by analyzing control flow and other code patterns.


Remember, stripped binaries pose a greater challenge, but with persistence, practice, and the right approach, you can still unravel their secrets. 

The absence of symbol names simply means you'll rely more on understanding code patterns, behaviors, and leveraging tools effectively.

## Navigating and Analyzing Binaries with Ghidra

Ghidra, developed by the NSA, is a free software reverse engineering suite which includes a decompiler. 

Once you've imported your binary into Ghidra, there's a myriad of features and information to explore.

### 17. Initial Analysis with Ghidra

Upon importing a binary, Ghidra will offer to analyze it. This process identifies functions, data structures, and more.

**Auto Analysis**: Allow Ghidra to perform its auto-analysis. It's comprehensive and will attempt to mark functions, identify loops, and more.
  
### 18. Exploring the Function List

On the left panel, you'll see a list of functions that Ghidra has identified.

- **Named vs. Unnamed Functions**: Even if the binary is stripped, Ghidra will attempt to identify functions based on common patterns. While you may not get meaningful names, you'll still have a list of potential points of interest.
- **Entry Point**: Look for the main function or the program's entry point to start your analysis.

### 19. Looking for Cryptographic Operations

One common task in reverse engineering, especially in CTF challenges, is identifying cryptographic operations.

**XOR Operations**: XOR is frequently used in simple encryption or obfuscation. In the Listing panel, search for `XOR` instructions. XOR loops or repeated XOR operations can indicate a decryption routine.
**Other Crypto Operations**: Look for operations or sequences that suggest more complex cryptographic algorithms, like substitutions, permutations, or mathematical operations.

### 20. Control Flow Graph

Ghidra provides a visual representation of the control flow within functions. This can be incredibly useful to understand the logic of the program.

**Branches and Loops**: Identify conditional operations, loops, and branches to understand the program's decision-making process.
**Unusual or Infrequent Paths**: Sometimes, the path to the flag or the interesting part of the code might be less frequently traveled. Look for conditions or branches that seem harder to reach.

### 21. Decompiler View

The decompiler translates assembly into higher-level pseudo-code, making it easier to understand.

**Readability**: Pseudo-code can be much more intuitive to read than raw assembly for those familiar with high-level programming languages.
**Variables**: Ghidra attempts to identify local and global variables, making the code's logic clearer.
  
### 22. Searching for Strings

Like the `strings` command in Linux, Ghidra can list all the readable strings in the binary. This can sometimes provide clues or even direct solutions.

### 23. Cross-References

If you find something of interest, whether it's a function, variable, or a particular piece of data, Ghidra can show you everywhere it's referenced or accessed in the code.

**Usage**: Right-click on the item of interest and look for the 'References' or 'Show References' option.

### 24. Annotations and Notes

As you explore, you can annotate the code, rename variables/functions for clarity, and leave notes. 

This is especially useful when working on complex binaries or if you need to step away and come back to your analysis later.

---

Ghidra is an intricate tool with a multitude of features. While the above guidelines offer a foundational approach to using it, the tool's true potential is unlocked as you become more familiar with its capabilities and nuances.

When coupled with hands-on practice and experience, Ghidra becomes an indispensable asset in the reverse engineer's toolkit.
