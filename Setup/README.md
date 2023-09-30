<p align="center">
  <img src="https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/168e55c5-937d-4d2c-af62-be413d6702cd">
</p>

# Getting Started

**Kali Linux is a popular choice for cybersecurity professionals, enthusiasts, and those participating in Capture The Flag (CTF) competitions for several reasons:**

- ***Penetration Testing Tools:*** Kali Linux is specifically designed for penetration testing and ethical hacking. It comes pre-installed with hundreds of tools that are helpful for various tasks in CTFs, such as nmap, gdb, Metasploit, John the Ripper, Hydra, Wireshark, and many more.
- ***Regularly Updated:*** Kali Linux is updated regularly with new tools, patches, and fixes. This ensures that the user always has the latest tools and vulnerabilities at their disposal.
- ***Scripting & Automation:*** With Kali being based on Debian, it supports all the scripting and automation capabilities of a typical Linux distribution. 
- ***Customizable:*** Advanced users can customize Kali to their specific needs, adding or removing tools, and tweaking it as required.

## Why use Kali ?
Kali is a distribution of Linux built by hackers for hackers. This doesn't mean that you cannot use any other operating system. 
You can get the same work done on a Windows machine, and even an Apple computer. 
However, Kali comes loaded with almost all of the necessary tools to get started right out of the gate.
Install the VM on your machine.

## Virtual Machines
A virtual machine is just that, a virtual computer on your computer. Using a Virtual Machine ( VM ) allows you to run an entirely different operating system while continuing to use your main computer. 
There are numerous other reason including security as to why you should use a VM. But convenience is the simplest.
Installing a Virtual Machine

The biggest names in VM's are VirtualBox, and VMWare. They both provide free solutions, and have alot of the same functionality. 

**The steps for installing a VMWare are as follows:**

- Choose a VM ( https://www.vmware.com/ or https://www.virtualbox.org/ ).
- Download the correct version for your operating system.
- Install.
  
That's really it, for the rest of this tutorial we will demonstrate installing kali on virtualbox (https://www.virtualbox.org/).

## Installing & Setting Up Kali

- First thing, press to install the [windows version of kali](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-virtualbox-amd64.7z ) or the [mac (apple silicon) version of kali](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-arm64.iso) if you are on a macbook.

- We will proceed with the windows version, if you have a mac you can proceed with this [tutorial](https://www.youtube.com/watch?v=9zdjQ9w_v_4).

- After you installed it, you will see a file named "kali-linux-2023.3-virtualbox-amd64.7z", you can download [7zip](https://www.7-zip.org/a/7z2301-x64.exe) and extract it as shown below.

![image](https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/4989872d-d2d1-48a2-96ea-6c70d1b3eabf)

![image](https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/c55428d4-8dc4-470e-b9e8-af32209ea52d)


- After that you will see these 2 files inside the extracted folder, then press on the blue file (.vbox).

![image](https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/c180a262-ce55-4dd0-ad8f-abeb021d261b)


- The virtualbox will open up and will show the machine in a powered off state.

![image](https://github.com/Cyber-Security-Club-HTU/CTF-Training/assets/75253629/b28c2260-1981-4ee9-a0ae-bb733f15db83)

Double click on the machine and voila, here is your kali machine up and running.

**Login Default Credentials:**

```
USERNAME: kali
PASSWORD: kali
```

Finally, dont forget to run `sudo apt update` after you open your machine to make sure everything is up to date.

