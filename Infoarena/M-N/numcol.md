# Numcol

Gigel likes to color the natural numbers from $1$ to $N$, each number being colored with a color. For this, he has $16$ colors available, numbered with digits from $0$ to $9$, and with uppercase letters from $A$ to $F$. Every day, Gigel colors the numbers in a different way, and today he thought of introducing an additional constraint: if two numbers $A$ and $B$ (which can be equal) are colored with the same color, then their sum (if it does not exceed the value $N$) must necessarily be colored with a different color than numbers $A$ and $B$. 

## Input data

The input file `numcol.in` contains the natural number $N$.

## Output data

The output file `numcol.out` will contain $N$ characters, representing the color of each number, in order, from $1$ to $N$. If there are multiple solutions, you can display any of them.

## Constraints and clarifications

$1 \leq N \leq 60\ 000$

## Example

`numcol.in`
```
16
```
`numcol.out`
```
0123456789ABCDEF
```