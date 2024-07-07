In the time of the Moors, the transmission of encoded messages between two people was done using a cipher called **node**. The two people secretly chose a story. This was written in a book using uppercase and lowercase letters of the English alphabet, on $P$ pages, numbered from $1$ to $P$, each containing exactly $R$ rows, numbered within each page from $1$ to $R$, and each row consisting of exactly $C$ words, numbered within each row from $1$ to $C$.
A word of the message to be transmitted was encoded by its position in the story chosen by the two, using three numbers written in Roman numerals, indicating in order: the page number, the row number within the page, and the word number within the row.
The coded message was written on three lines. The first line contained the page numbers, the second line contained the row numbers, and the third line contained the word numbers.
Assuming that the message consists of the first word on the fifth row of the second page and the fourth word on the second row of the first page. The message could be transmitted on three lines as follows:
'II I' (page numbers)
'V II' (row numbers)
'I IV' (word numbers)
The Roman numerals are written with uppercase letters $\\text{M}$, $\\text{D}$, $\\text{C}$, $\\text{L}$, $\\text{X}$, $\\text{V}$, $\\text{I}$, and their corresponding values are in order: $1000, 500, 100, 50, 10, 5, 1$. The value of a number written in Roman numerals is calculated by traversing the number from left to right as follows:
* the current numeral is added to the obtained value until that moment if the next numeral is smaller than or equal to it
* the current numeral is subtracted from the obtained value until that moment if the next numeral is greater than it
* the last numeral is always added to the obtained value until that moment

For example, for the number $\\text{MCDXLVI}$ written in Roman numerals, the value $1446$ is obtained in the decimal system as follows: $1000 - 100 + 500 - 10 + 50 + 5 + 1$, and for the number $\\text{XXI}$ written in Roman numerals, the value $21$ is obtained in the decimal system as $10 + 10 + 1$.

# Task

Given the text of the story chosen by the two and their encoded message, write a program that solves the following two tasks:
a) Rewrite the encoded message using decimal numerals.
b) Display all the decoded words of the message in the order they appear in the story.

# Input data

The input file `nod.in` contains:
* The first line contains the number $1$ if only task $a)$ is required or the number $2$ if task $b)$ is required;
* The next three lines contain the encoded message according to the rules described in the statement;
* If the first number in the file is $2$ then the fifth line contains three natural numbers $P$, $R$ and $C$, separated by a space, with the meaning given in the statement;
* The next $P \\times R$ lines contain the text of the story, each line containing $C$ words, separated by a space.

# Output data

If the first number in the input file is $1$ then the output file `nod.out` will contain, in the same order, on three lines, the numbers from the encoded message written in the decimal system. The numbers will be separated within the lines by a space.
If the first number in the input file is $2$ then the output file `nod.out` will contain on a single line the decoded words of the message, in the order from the story. The words will be separated by a space.

# Constraints and clarifications

* $1 \\leq P \\leq 2\\ 000$
* $1 \\leq R \\leq 25$
* $1 \\leq C \\leq 15$
* $1 \\leq \\text{length of a word from the story} \\leq 12$
* any number written in Roman numerals has at most $10$ uppercase letters
* the decoded message will contain at most $20$ words

# Example 1

`nod.in`
```
1
III II I
II V II
VI I IV
```

`nod.out`
```
3 2 1
2 5 2
6 1 4
```

## Explanation

The input test indicates the resolution of the first task, i.e., task $a)$.
The numbers on each line are written in the same order, in the decimal system.

# Example 2

`nod.in`
```
2
I III II I II
I I II I II
I II II II IV
3 2 4
At the Olympics problems can
have one or more
requirements For some
problems the committee can decide
that the first requirement should
be evaluated separately
```

`nod.out`
```
At the Olympics committee decide first
```

## Explanation

The input test indicates the resolution of the second task, i.e., task $b)$.
The words identified in the story are:
`At` - by (`I`, `I`, `I`)
`first` - by (`III`, `I`, `II`)
`committee` - by (`II`, `II`, `II`)
`Olympics` - by (`I`, `I`, `II`)
`decide` - by (`II`, `II`, `IV`)
The decoded words of the message, in the order from the story, are:
`At the Olympics committee decide first