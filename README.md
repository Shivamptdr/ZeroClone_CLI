# ZeroCloneFiles_CLI

ZeroClone is a Python tool for managing duplicate files. It can detect, delete, and calculate space used by duplicate files in a directory.

Features
--------
- Find duplicate files in a directory and its subdirectories.
- Delete duplicate files while keeping one copy.
- Calculate the disk space occupied by duplicate files.
- Calculate the disk space freed after deleting duplicates.

Installation
------------
1. Clone the repository:
   git clone https://github.com/Shivamptdr/ZeroClone_CLI.git
2. cd ZeroClone

Usage
-----
1. Find duplicates:
   python main.py /path/to/directory

2. Delete duplicates:
   python main.py /path/to/directory --delete

3. Calculate space occupied by duplicates:
   python main.py /path/to/directory --space

4. Calculate space freed after deleting duplicates:
   python main.py /path/to/directory --space-freed
