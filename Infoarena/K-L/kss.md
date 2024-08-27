## Task

Miriam likes words in alphabetical order. This time she is asking questions such as: having a string $S$ of length $N$, what is the $K$-th subsequence of it in lexicographical order? Of course, Miriam is not good at programming, so she needs help.

## Input data

The input file `kss.in` will contain the number $T$ of tests on the first line. The following lines will have the following format: line $2 * i$ will contain the numbers $N$ and $K$ and line $2 * i + 1$, the string $S$.

## Output data

In the output file `kss.out` you will print $T$ lines, each line $i$ containing the answer to question $i$.

## Constraints and clarifications

$1 \leq T \leq 1\ 000$

$1 \leq N \leq 1\ 000$

$1 \leq K \leq 10^{18}$

The string $S$ will contain lowercase English alphabet letters.

Note: two subsequences are not considered distinct if the positions of their characters in the initial string are distinct. If there are not $K$ distinct subsequences in the string $S$, the answer will be $-1$.

## Example

`kss.in`
```
13
4 1
aabc
4 2
aabc
4 3
aabc
4 4
aabc
4 5
aabc
4 6
aabc
4 7
aabc
4 8
aabc
4 9
aabc
4 10
aabc
4 11
aabc
4 12
aabc
25 12345
abcafedfdseasfesdfdfdfega
```

`kss.out`
```
a
aa
aab
aabc
aac
ab
abc
ac
b
bc
c
-1
aaddeafedfddea
```