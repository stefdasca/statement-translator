# DNA

An important problem in biology in recent years has been finding the human DNA sequence. A DNA strand consists of two spirals of molecules, each molecule being briefly named $A$, $G$, $C$, or $T$. Therefore, a DNA strand can be represented as a string of characters from the set $A$, $G$, $C$, and $T$. The problem researchers face is that they cannot find the entire DNA sequence using chemical or biological methods but can determine sections of it. After determining a series of sections, the most likely sequence of molecules close to the real sequence is the shortest string of characters that contains all the determined sections as subarrays!

## Task

Write a program to help researchers determine the shortest string of characters that contains all the determined sections as subarrays.

## Input data

The input file `adn.in` will contain the number $N$ of DNA sequences on the first line, and on the next $N$ lines, each line will contain a string of characters containing only the letters $A$, $G$, $C$, and $T$.

## Output data

The output file `adn.out` will contain a single line with the shortest string that contains the sequences from the input as subarrays.

## Constraints and clarifications

$2 \leq N \leq 18$

The length of each string is less than $30\ 001$

If there are multiple solutions of minimum length, any one will be displayed

## Example

`adn.in`
```
5
GGATATAAAAAC
GATAACCGCGCAGTGATGAGA
TGATGAGATGGGGATATAAAA
AGATAGATGATAACCGCGCAGT
ATGGGGATATAAAAACTTTTTT
```

`adn.out`
```
AGATAGATGATAACCGCGCAGTGATGAGATGGGGATATAAAAACTTTTTT
```

## Explanation

$AGATAGATGATAACCGCGCAGT$

$GATAACCGCGCAGT$

$GATGAGA$

$TGATGAGA$

$TGGGGATATAAAA$

$ATGGGGATATAAAA$

$ACTTTTTT$

$GGATATAAAAAC$