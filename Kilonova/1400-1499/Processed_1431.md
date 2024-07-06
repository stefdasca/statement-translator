The Babylonians developed a positional number system where any natural number can be represented using the following symbols:

| Symbol | Digit  |
| ------ | ------ |
| ~[unu.png] | one   |
| ~[zece.png] | ten   |

Values $k$ from {$2$, $3$, $\dots$, $9$} are obtained by writing the symbol for one $k$ times.
Example: the Babylonian representation of $3$ is
~[3.png]

Numbers $11$, $12$, $\dots$, $59$ are obtained as sequences of symbols followed by symbols.
Example: $43$ is represented as
~[43.png]

The system uses grouping of units in sixties. Thus, to write the number sixty, the same symbol as for one is used, but its value is given by its position.
The Babylonians did not use the digit $0$. For correct positioning of the symbols, space was used:
~[spatiu.png]

Examples:

| Number | Representation |
| ------ | ------------- |
| $60$   | ~[60.png]      |
| $3600$ | ~[3600.png]    |

The Babylonian writing of a number is encoded as follows:

| Digit | Symbol      |
| ----- | ----------- |
| $1$   | ~[unu.png]  |
| $2$   | ~[zece.png] |
| $3$   | ~[spatiu.png] | 

Examples:

| Babylonian Writing | Babylonian Encoding | Decimal Value of the Number       |
| ------------------ | ------------------- | --------------------------------- |
| ~[62.png]          | $1311$              | $1 \cdot 60 + 2 = 62$             |
| ~[12.png]          | $12$                | $1 \cdot 60 + 10 = 70$            |
| ~[84.png]          | $1221111$           | $1 \cdot 60 + 20 + 4 = 84$        |
| ~[4203.png]        | $1231111$           | $1 \cdot 60 \cdot 60 + 10 \cdot 60 + 3 = 4203$ |

# Task

Given a natural number $n$ and a sequence of $n$ digits from {$1$, $2$, $3$}, representing the encoding of the Babylonian writing of a natural number, determine:

1. the maximum number of consecutive $1$ digits in the given Babylonian writing encoding;
2. the natural number in the decimal system corresponding to the given Babylonian writing.

# Input data

The input file `babilon.in` will contain:

* The first line contains a natural number $p$ ($1 \leq p \leq 2$);
* The second line contains a natural number $n$;
* The third line contains $n$ digits separated by a space, representing the encoding of the Babylonian writing of a natural number.

# Output data

If the value of $p$ is $1$, only point $1$ from the task will be solved. In this case, the output file `babilon.out` will contain on the first line a natural number representing the maximum number of consecutive $1$ digits in the given Babylonian writing encoding.
If the value of $p$ is $2$, only point $2$ from the task will be solved. In this case, the output file `babilon.out` will contain on the first line the natural number corresponding to the given Babylonian writing.

# Constraints and clarifications

* $2 \leq n \leq 109$;
* It is guaranteed that the number of digits of the result from point $2$ (the decimal number) is less than $20$;
* $30\%$ of the tests will have the first line value as $1$, and the remaining $70\%$ of the tests will have the first line value as $2$.

# Example 1

`babilon.in`
```
1
8
1 1 3 2 1 1 1 2
```

`babilon.out`
```
3
```

# Explanation

$1 \  1 \  3 \  2$ **1 1 1** $2$
The longest sequence of $1$ digits has a length of $3$.

# Example 2

`babilon.in`
```
2
7
1 1 3 2 1 1 1
```

`babilon.out`
```
7213
```

# Explanation

~[7213.png]
$2$ is multiplied by $60$ twice (once because it is followed by space and once more because it precedes a group starting with the symbol for ten), then the value $13$ is added.
$2 \cdot 60 \cdot 60 + 10 + 3 = 7213$

# Example 3

`babilon.in`
```
2
9
1 1 1 2 1 1 2 2 1
```

`babilon.out`
```
11541
```

# Explanation

~[11541.png]
$3$ is multiplied by $60$ twice because it is preceded by two groups starting with the symbol for ten, then $12$ is multiplied by $60$ and finally $21$ is added.
$3 \cdot 60 \cdot 60 + 12 \cdot 60 + 21 = 11541$