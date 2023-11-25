# Tools

This section will be a brief on tools that are used in the forensics section in our CTF training. You might find some tools that aren't mentioned in the training.

## Steganography tools

-   file: Identify the file type:
    ```
    file <file_name>
    ```

-   exftool: Display or modify metadata about a file. 

    To display information:
    ```
    exfitool <file_name>
    ```

    To modify metadata value:
    ```
    exiftool [OPTION] <file_name>
    ```

    For example, to add a comment:
    ```
    exiftool -Comment=<your_comment> <file_name>
    ```

-   binwalk: Extract/embed binaries from a file, hence the name.
    ```
    binwalk -e <file_name>
    ```

-   foremost: Extracting binary files from a file. The output is a bit better
than binwalk.

    ```
    foremost <file_name>
    ```

-   