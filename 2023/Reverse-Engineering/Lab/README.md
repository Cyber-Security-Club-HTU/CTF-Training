<div align="center">
<img src="https://png.pngtree.com/png-vector/20220720/ourmid/pngtree-russian-bear-tireman-shield-mascot-head-identity-sporting-vector-png-image_32798422.png">
</div>

# ColdRoot CTF Challenge

Welcome to the ColdRoot CTF challenges. Unravel the mysteries set forth by the notorious Russian APT group, ColdRoot.

- To get started, wget the binary to your machine:

```bash
wget https://github.com/Cyber-Security-Club-HTU/CTF-Training/blob/main/2023/Reverse-Engineering/Lab/coldroot.bin
```

---

## Challenge 1 Part 1: ColdRoot

### Scenario
A large multinational corporation recently fell victim to a data breach. Initial forensics point towards the involvement of a Russian APT group named "ColdRoot". 

A binary was found on a compromised system is your starting point. 

### Objective
Dissect the provided binary to extract hidden messages.

### Hint
<details>
  <summary>Click to reveal hint</summary>
  
  - Sometimes, it's not about gaining access but understanding the process.
  - Strings can be useful, but they might also deceive.
</details>

### Suggested Tools
- `file`
- `strings`
- `strace`
- `ltrace`
- `objdump`
- `readelf`
- `ghidra`

---

## Challenge 1 Part 2: Bear1337

### Scenario

Navigating deeper into ColdRoot's systems, you've encountered another binary, which appears to be concealing encrypted information. 

There's a mention of colors, but what could they mean?

### Objective
Use dynamic analysis to decrypt the secret message within the binary.

### Hint
<details>
  <summary>Click to reveal hint</summary>
  
  The path ahead requires a trio of colors. Look to the north, where winters are fierce, and tales of bears and babushkas are abundant.
</details>

### Suggested Tools
- `gdb`
- `file`
- `strings`
- `strace`
- `ltrace`
- `ghidra`
- `objdump`
- `radare2`

---

**Good luck, and may the odds be in your favor!**
