Gigel and Ionel are playing spies! Therefore, they imagine a way to encode a message so that no one can decipher it. All their messages have a length that is a power of $2$. They number the letters of the message starting from $1$. Then they separate the letters into two categories: those with odd-order numbers on the left, and those with even-order numbers on the right, keeping their order intact. This process continues for each newly resulting group starting with the left one until each obtained group contains only one character. After finishing the operations, they concatenate the single-character groups from left to right to obtain the encoded message.

For example, for the message `MESAJNECODIFICAT`, they proceed as follows:

1. numbering

```
MESAJNECODIFICAT
123456789...
```

2. separate

```
MSJEOIIA EANCDFCT 
12345678 12345678 
```

then repeat steps $1$ and $2$ for each resulting group

```
MJOI SEIA ENDC ACFT
1234 1234 1234 1234
```

```
MO JI SI EA ED NC AF CT
12 12 12 12 12 12 12 12
```

```
M O J I S I E A E D N C A F C T
1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
```

until a single character is obtained in each group and by concatenating the letters from left to right, the encoded message is obtained: `MOJISIEAEDNCAFCT`.

# Task

Write a program to solve the following two requirements:
1. Given a message, determine its encoding;
2. Given an encoded message, determine its decoding.

# Input data

The first line of the input file `spioni.in` contains a character $C$ or $D$, indicating whether the message from the second line is to be encoded or decoded. The second line of the input file contains a string of characters.

# Output data

The output file `spioni.out` will contain a single line that will contain the encoded message (if the first line of the input file contains $C$), or the decoded message (if the first line of the input file contains $D$).

# Constraints and clarifications

* The string of characters in the input file contains characters with ASCII codes between $33$ and $127$, the length of the string being a power of $2$ between $2$ and $4\ 096$.
* For tests worth $50\%$ of the points, the input file contains $C$ on the first line.

# Example 1

`spioni.in`
```
C
MESAJNECODIFICAT
```

`spioni.out`
```
MOJISIEAEDNCAFCT
```

# Example 2

`spioni.in`
```
D
MOJISIEAEDNCAFCT
```

`spioni.out`
```
MESAJNECODIFICAT
```
