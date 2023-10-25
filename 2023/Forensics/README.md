# CTF Forensics tutorial

This directory will be for the forensics CTF category training. It'll cover beginner to intermediate skills required to solve anything related to forensics challenges

## Prerequisites

Before diving into CTF, you should have some background in those:
-   Googling. You'll use google most of the time. You have to get used to doing research on different topics. (most of the time you might end up having 50 tabs open during 1 ctf challenge)
-   A programming/scripting language. Go with Python. [Python As Fast as Possible](https://www.youtube.com/watch?v=VchuKL44s6E&pp=ygULcHl0aG9uIGFzYXA%3D). To make sure you grasp that language, you could go to [CodeWars](https://www.codewars.com) where you can solve problems with your programming skills.
-   Basic networking info.
-   Dealing with linux shell and command line in general. You can go to TryHackMe Linux Fundamentals [1](https://tryhackme.com/room/linuxfundamentalspart1) [2](https://tryhackme.com/room/linuxfundamentalspart2) [3](https://tryhackme.com/room/linuxfundamentalspart3) for the very basics, then you can visit [OverTheWire Bandit](https://overthewire.org/wargames/bandit) to advance knowledge about important linux utilities that might be helpful in CTF in general.

-   Tools not installed on kali:
    apt:
    - foremost
    - steghide
    - stegseek
    - imagemagick
    
    github/other sources:
    - stegsolve:
        Copy the following box into your terminal.
        ```bash
        mkdir -p ~/bin
        wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
        echo '#!/bin/zsh
        java -jar ~/bin/stegsolve.jar' | sudo tee /bin/stegsolve
        sudo chmod +x /bin/stegsolve
        ```


## Table of contents

-   **Some Basic info**
-   **Steganography**
    -   File type
    -   Metadata
    -   File carving/extracting
    -   strings
    -   Image steganography
    -   Audio/video steganogrphy
    -   Other forms of steganography
-   **PCAP Analysis**
    -   Wireshark
    -   Filtering data with Tshark
-   **Memory Analysis**
    -   Voliatility
    -   Where to look
    -   Dumping files, registries, hashes(cracking)
-   **Disk analysis**
    -   Autopsy
    -   FTK

