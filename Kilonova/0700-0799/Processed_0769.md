Costel must develop, together with his team, a _software_ application for managing files on the hard disk. His task is to write a module for determining the paths of all data files located in the tree structure of folders on the disk. The team members have established their own encoding for storing the file structure on the disk, using a string of characters. The technical specifications are as follows:

- A folder is a special type of file that can contain files and/or folders (these being considered subfolders of the respective folder);
- Folder names start with a letter, have a maximum of 30 characters, and are written in uppercase;
- Data file names start with a letter, have a maximum of 30 characters, and are written in lowercase;
- The characters used for file and folder names are the letters of the English alphabet and Arabic numerals;
- The representation of the file structure in the form of a character string is achieved according to the following rule: `FOLDER_NAME(list_of_folders_and_files)` where `list_of_folders_and_files`, possibly empty, contains the files and/or subfolders of the `FOLDER_NAME` folder, separated by commas. Subfolders are represented according to the same rule.

For example, the file and folder structure in the figure below

~[clip_image001.png]

is represented by the string: `FOLDER1(FOLDER2(),FOLDER3(FOLDER4(poveste,basm),basm))`

# Task

Write a program that, given the string encoding a file structure on disk, determines the path for each data file in the structure. A file path is understood as a sequence of folders, each folder followed by the _\\(backslash)_ character, starting from the highest level folder in the structure (the first specified in the string encoding the file structure), up to the subfolder in which the respective data file is located, ending with the name of the file. The determined paths will be displayed in lexicographic order.

# Input data

The input file `dir.in` contains on the first line the string encoding the file structure on disk.

# Output data

The output file `dir.out` will contain on the first line a natural number $N$ representing the number of found data files. On the next $N$ lines, the paths that allow identification of the found files will be written in lexicographic order, in the format: `F1\\F2\\...\\Fn\\file`, one path per line.

# Constraints and clarifications

* The string encoding the file structure is non-empty and contains a maximum of $1\ 600$ characters.
* The folder structure contains at least one folder and at least one file.
* The number of data files is at most $100$.
* The length of a file path is at most $255$ characters.
* The string $x_1x_2…x_n$ is lexicographically smaller than the string $y_1y_2…y_m$, if there exists $k$ such that $x_1=y_1,x_2=y_2,…,x_{k-1}=y_{k-1}$ and ($x_k<y_k$ or $k=n+1$).

# Scoring

For correctly determining the number of data files, $30\%$ of the score is awarded. If the number of data files is correctly determined and the paths are correctly displayed in lexicographic order, the full score is awarded.

# Example

`dir.in`
```
FOLDER1(FOLDER2(),FOLDER3(FOLDER4(poveste,basm),basm))
```

`dir.out`
```
3
FOLDER1\\FOLDER3\\FOLDER4\\basm
FOLDER1\\FOLDER3\\FOLDER4\\poveste
FOLDER1\\FOLDER3\\basm
```