Gigel, a 7th-grade student passionate about computer applications, thought of developing a program that simulates the well-known Excel product. He quickly got to work, and in an hour, he managed to create a program similar to Excel but which, unlike the original, can only perform one operation in its cells: sum. Try to accomplish Gigel's feat yourself!

We remind you that an Excel spreadsheet is presented in the form of a gridded surface with horizontal and vertical lines. Their intersection results in rectangles (called cells), each cell having a name consisting of a letter and a number, representing the column and the row it is on.

~[excel.png|align=center|width=45em]

For example, the cell in the top-left corner is $A1$, followed by $B1, C1$, etc., on the line. Entering a formula in a cell always begins with the `=` sign. For example, if we write `=A2+B2` in cell `C2`, it means that the result of adding the values from cells $A2$ and $B2$ will be written in this cell. There can also be cells with the formula `=A5`, which means that the result in that cell will be equal to the result in cell $A5$. Being new both to programming and the Excel application, Gigel's idea is for his program to fill the cells starting with the first column, then the second, and so on, so that the formulas that can appear in the cell ($col$, $lin$) can use data from columns $1$ to $col-1$ and from cells on rows $1$ to $lin-1$ of column $col$.

# Task

Given a spreadsheet, replace all formulas that appear with the results obtained according to the conditions specified in the text.

# Input data

The `excel.in` file contains on the first line two values $m \\ n$, separated by a space, representing the number of columns and rows of the spreadsheet. The next $n$ lines describe the $m$ columns of the sheet. A description can consist of positive integer values or formulas separated by a single space. Formulas are strings that always begin with the `=` sign. The input file is considered correct, meaning that the operations that appear can be executed, and the spreadsheet can be completed.

# Output data

The `excel.out` file will contain $n$ lines, each line containing $m$ values representing the final result of the operations performed in the spreadsheet.

# Constraints and clarifications

* $0$ < number of columns $\\leq 26$, noted from `A` to `Z`;
* $0$ < number of rows $\\leq 50$;
* each line describing the Excel sheet has a maximum length $< 256$;
* each numerical value in the initial spreadsheet is a positive number $\\leq 100$;
* the formulas that may appear in cells only refer to the addition operation.

# Example

`excel.in`
```
4 3
11 21 =A1+A2 =A3
10 15 =B1+B2 =A2+B1
=A1+A2 14 21 3
```

`excel.out`
```
11 21 21 21
10 15 36 31
21 14 21 3
```

## Explanation

The element in column $1$ and row $3$ is obtained as $11 \\ (A1) + 10 \\ (A2) = 21$;
The element in column $3$ and row $1$ is obtained as $11 \\ (A1) + 10 \\ (A2) = 21$;
The element in column $3$ and row $2$ is obtained as $21 \\ (B1) + 15 \\ (B2) = 36$; etc.