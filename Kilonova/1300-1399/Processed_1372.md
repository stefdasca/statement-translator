Here is the translated text:

```markdown
MicroPhone, a software applications producer for mobile phones, is developing the spreadsheet program MicroXL to include it in the basic software of the next generation of smartphones. In its current stage, the application allows work on a spreadsheet composed of $N \cdot N$ cells, each cell being able to contain a nonzero natural number or a formula.

A formula is preceded by the equal sign and contains an arbitrary number, possibly zero, of addition operations. The terms of a formula can be nonzero natural constants or references to other cells, as can be seen in the figure below. A cell reference is made by specifying the corresponding row and column number, separated by the `:` character. The formula contains no spaces.

~[0f577c0991586d150214599a025002d9.png]

# Task

Write a program that determines the value of each cell in a given spreadsheet.

# Input data

The file `mxl.in` contains on the first line the nonzero natural numbers $N$ and $K$, representing the number of rows and columns of the spreadsheet, respectively the number of cells containing data, and on the next $K$ lines two integers $lin, col$ and a string $s$, with the following meaning: $lin$ and $col$ represent the corresponding row and column of a cell, and $s$ is the content of that cell (a nonzero natural number or a formula).

# Output data

The file `mxl.out` will contain $N$ lines. Each line $i$ will contain $N$ natural numbers, separated by a space, representing the calculated values for each cell on line $i$ of the spreadsheet. If a cell does not contain data or formulas, the value $0$ will be printed.

# Constraints and clarifications

* $0 < N \leq 40$ 
* $0 < K \leq N \cdot N$
* The constants used are nonzero natural numbers less than or equal to $75$
* The formulas have a length of at most $255$ characters and can always be calculated
* There are no circular references

# Example

`mxl.in`
```
5 7
1 1 =1:2+5
1 2 =1:3+4
1 3 =3+1:4
1 4 =1:5+2
1 5 1
4 3 =1+2+3
3 1 =13
```

`mxl.out`
```
15 10 6 3 1 
0 0 0 0 0 
13 0 0 0 0 
0 0 6 0 0 
0 0 0 0 0
```
```

Double checked the statement for grammar and syntax: everything appears to be correctly translated and formatted according to the rules of the English language.