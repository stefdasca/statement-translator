# Task

We have a spreadsheet, similar to an Excel sheet, and we want to find the values of all its cells.
The spreadsheet is in the form of a matrix, with $N$ rows and $N$ columns, numbered from $1$ to $N$.
At the input, for some cells, the value (a natural number) or a formula is specified directly. The formula can represent either the sum or the product of two terms. The two terms can be constant natural values or cell names.

# Input data

The first line of the input file `calctab.in` contains a natural number $N$ representing the size of the square spreadsheet. 
Each of the following $N$ lines contains $N$ strings, separated by a space, representing, in order, the information about the cells on that line.
If the value is a single natural number, then it represents the value of the cell. For the cells indicated with formulas, the string is of the type `X+Y` or `X*Y` (without other spaces inside).
The value $X$ can only be a cell identifier, and the value $Y$ can be a natural number or a cell identifier. The cell identifier has $6$ digits, the first being `L`, followed by two digits indicating the row number, then `C` followed by two digits indicating the column number (for rows and columns from $1$ to $9$, the codes are written in the form $01, 02, \dots, 09$).

# Output data

The output file `calctab.out` will contain the numeric values of the matrix, in order, $N$ per line, separated by a space. If the matrix cannot be completely calculated, the value `-1` will be written in place of the values that cannot be calculated.

# Constraints and clarifications

* $1 \leq N \leq 99$;
* all values in the matrix, both given and calculated, have a maximum of $9$ digits and are positive;
* it is guaranteed that the input data format is correct, as described;
* for $72$ points tests, there are no multiplication formulas in the input file.

# Example 1

`calctab.in`
```
2
2 L01C01+3
L01C01+L01C02 11
```

`calctab.out`
```
2 5
7 11
```

# Example 2

`calctab.in`
```
2
2 L02C01+L02C02
L01C02+L02C02 L01C02+L02C01
```

`calctab.out`
```
2 -1
-1 -1
```

Please double-check the statement and fix potential grammar and/or syntax errors according to the rules of the English language.