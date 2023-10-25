# Disk Image Analysis
Disk image analysis is the examination of a storage device, such as a hard drive, or a solid state drive. These images do not only contain user data, but also system files, unallocated space, and so on. 

Disk image analysis is crucial for forensics, as they could be used for many reasons, such as the following: 
1. Evidence: Disk image analysis is important for preserving the state of a system at a given point in time, this ensures that the digital evidence is not tampered with, which could be used for legal reasons.
2. Cybersecurity investigations: Forensic analysts rely on disk image analysis, to identify vulnerabilities, and to construct the timeline of the events. 
3. Data Recovery: When data is lost due to deletion or hardware failure, disk image analysis can be used to recover and restore the lost information. 
- Occasionally, a CTF forensics challenge consists of a full disk image, and the player needs to have a strategy for finding a needle (the flag) in this haystack of data. Triage, in computer forensics, refers to the ability to quickly narrow down what to look at. Without a strategy, the only option is looking at everything, which is time-prohibitive (not to mention exhausting). 

-There are lots of tools that are used in disk analysis, we are going to cover:

1. **grep**: Grep searches for PATTERNS in each FILE. PATTERNS is one or more patterns separated by newline characters, and grep prints each line that matches a pattern. 
2. **srch_strings**: srch_strings - display printable strings in files 
3. **sleuthkit**: The Sleuth Kit is a library and collection of command line tools that allow you to investigate disk images. In order to install it, run the following command:
	> apt install sleuthkit 
4.  **fls**: Fls is a command from the sleuthkit library, it lists the files and directory names in the image and can display file names of recently deleted files for the directory 
5. **mmls**: mmls is also a command from the sleuthkit library, mmls stands for "media management list structures," and it is used for listing and examining partition information on storage media, such as hard drives, disk images, and other storage devices. This tool is particularly helpful for forensic investigators and analysts when they need to understand the layout of partitions on a storage device. 
6. **icat**: (inode cat) - Output the contents of a file based on its inode number.
7. FTK Imager: A forensic software tool used for creating and analyzing disk images in digital forensics. It allows investigators to make exact copies of storage devices, preserving the original data, and then analyze these copies for evidence. This helps ensure data integrity and assists in investigating crimes involving digital evidence.

>**Disk, disk, sleuth!** 

In this challenge, we are downloading a gzip file, the first step in solving this challenge is to unzip the file. This is done using the following command: gzip -d [Filename] 

- In this command, -d means Decompressing or Uncompressing the file. 
After decompressing, we are left with a file called `dds1-alpine.flag.img`. 
In order to know what the file we are dealing with is, we can use the 'file' command, followed by the file's name. After executing this command, we get the following output: 


>dds1-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors 
![1.png](./files/Disk_Image_Analysis/1.png)

This is description of a boot sector and partition information for a storage device or disk image. Let's break down what each part of this description means: 
1. dds1-alpine.flag.img: This is likely the filename of the disk image or storage device in question.
2. DOS/MBR boot sector: This indicates that the disk is formatted with a Master Boot Record (MBR) partitioning scheme. MBR is an older partitioning style commonly used on BIOS-based systems. 
3. partition 1: This specifies that there is one partition on the disk. 
4. ID=0x83: This is the partition type identifier. In this case, it's set to 0x83, which typically represents a Linux file system partition. It's common for Linux systems to use partition type 0x83 for their primary partitions.
5. active: This suggests that this partition is set as the active (bootable) partition. On MBR disks, only one partition can be marked as active, and it's the partition from which the system will boot. 
6. start-CHS and end-CHS: These are the starting and ending cylinder-head-sector (CHS) values for the partition. CHS was an older way of specifying disk locations and is not commonly used today. 
7. startsector 2048: This indicates that the partition starts at sector 2048 on the disk. Sector 2048 is often used as the starting point for partitions to align them with modern storage devices efficiently. 
8. 260096 sectors: This is the length of the partition in sectors. 

One way to know what this disk file does, is to understand what's inside of it, to read what's inside, we can use the **'strings'** command, the strings command shows anything that's readable in this file. 

After executing the command **'strings dds1-alpine.flag.img'**, we get a lot of text, but we are looking for a specific flag, that starts with "Pico", in this case, we use the pipe | with the grep command, what this does is get the output of the strings command, then pipe it with grep. Grep only outputs the desired results from the strings. 

After executing this command: strings dds1-alpine.flag.img | grep 'pico' We get the following output: 

![2.png](./files/Disk_Image_Analysis/2.png)

Finally, we've found our flag, which is **picoCTF{f0r3ns1c4t0r_n30phyt3_a69a712c}.** 

>**Disk, disk, sleuth! II **

We will start by unzipping the gzip, using the same command used above, 
> gzip -d dds2-alpine.flag.img

After that, we will use the mmls command, it is done to analyze the disk image file, and list the partitions found in it. We will run the following command: 
>mmls dds2-alpine.flag.img 

![3.png](./files/Disk_Image_Analysis/3.png)

To breakdown the output, there are two partitions on the disk image: 
1. Partition 001: This is a Linux partition that starts at sector 2048 and ends at sector 26,2143. 
2. Partition 002: This space is unallocated and spans from sector 0 to sector 2047. It's unused space. 

The output tells you that the disk image has two parts: one with a Linux file system and another that's empty and not used for anything. Knowing this information is important, since we now know which sector it starts with, which is **2048**, we can use it in the fls command to go on. 

We will now run the following command: 
>fls -o 2048 dds2-alpine.flag.img 

Breaking down the command: 

- **fls**: This is the command itself, and it stands for "File System Layer." fls is part of The Sleuth Kit (TSK) suite of digital forensic tools and is used for listing files and directories within a file system. 

- **-o 2048**: This specifies the offset in sectors where the file system structure begins. In this case, it's set to 2048 sectors, which is what we’ve gotten from the mmls command. This is important because some disk images may have a certain number of reserved sectors or metadata at the beginning before the actual file system structure. By specifying the offset, you're telling fls to start its analysis from sector 2048.
 
After running it, we get the following output: 

![4.png](./files/Disk_Image_Analysis/4.png)

The number represents the **inode number** of the directory. An inode is a data structure in Unix-like file systems that stores metadata about files and directories, such as permissions, timestamps, and pointers to the data blocks.

Since we’ve found the root file, at inode number 18290, we will run the same command, to dive deeper into it: 
>fls -o 2048 dds2-alpine.flag.img 18290 

![5.png](./files/Disk_Image_Analysis/5.png)

This tells us that at 18291, we will find the text file that the challenge is asking is to read from. 
We will now have to use icat, in order to read this text file, we will use this command
>icat ./dds2-alpine.flag.img -o 2048 18291 

Let’s breakdown this command: 
- **icat**: This is the command itself, and it stands for "inode cat." icat is a command provided by The Sleuth Kit (TSK) and is used to extract the contents of a file by specifying its inode number. 
- **./dds2-alpine.flag.img**: This is the path to the disk image file you want to extract data from. The icat command will operate on this disk image. 
- **-o 2048**: This specifies the offset in sectors where the file system structure begins within the disk image. In this case, it's set to 2048 sectors. You're telling icat to start its operation from sector 2048.
- **18291**: This is the inode number of the file you want to extract. Inodes are data structures in Unix-like file systems that store metadata about files, including their data block pointers and other attributes. 

After executing the command, we will get the following output:

![6.png](./files/Disk_Image_Analysis/6.png)

We have found the flag!

**Operation Oni**
We are going to launch the application called "FTK Imager". First of all, we start by downloading the disk image. After downloading it, we unzip it, and click on "File" "Add Evidence Item" As shown here:
![[7.png]]
After this, we click on "Image File" as shown here:
![[8.png]]
We then choose the image file, and click on "Finish", as we can see, we now have full access to the disk image files, and we can browse all of them. The challenge has asked us to search for a ssh file in order to log in remotely using it.
![[9.png]]
From these 2 partitions, we can start searching by pressing the "+" icon, and browsing through the directories.

>After browsing, I have found the ssh file at Partition 2 -> NONAME -> root -> root -> .ssh
![[10.png]]

We can now export the file, by right clicking on it, pressing "Export File", then choosing a destination.

After this, we can open Windows Powershell or CMD, in order to complete the challenge, and connect using SSH. We are going to use the following command, which was provided by picoctf:
>`ssh -i id_ed25519 -p 64368 ctf-player@saturn.picoctf.net`

We then after connecting, will use "ls" to list the directories and available files.
![[Pasted image 20231024204358.png]]
We will now use cat, to preview the flag.txt file.
![[12.png]]
We have found our flag! **"picoCTF{k3y_5l3u7h_af277f77}"**


**Root-me Challenge: Deleted Files**

This challenge starts with giving us a .tar file, which when decompressed, gives us a file called "usb.image".

We are going to follow the same steps, open the "FTK Imager" file, "Add Evidence File", then choosing the given file. After completing these steps, we have the following:
![[13.png]]

After clicking on "Root", we can see a file called "anonyme.png", as follows:
![[14.png]]

In order to view the file in text format, we click on the "Text" icon, which is shown here:

![[15.png]]

We then, can see the following:
![[16.png]]

We have solved the challenge, the answer is javier_turcot.
