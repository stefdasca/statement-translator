
At a contest, $N$ competitors participate. Each competitor receives a sheet of paper on which they will write a word of at most $100$ characters (lowercase letters of the English alphabet). The words will be distinct. For differentiation, the competitors appeal to an oracle. The oracle also produces a word. The competitor who has written the word "closest" to the oracle's word will win. The degree of "closeness" between two words is the length of the longest common subword. A subword of a given word is understood to be a word that can be obtained from the given word by deleting 0 or more letters while preserving the order of the remaining letters.

# Task

You are given the word $c_0$ produced by the oracle and the words $c_i, \\ i = 1, 2, ..., N$, written by the competitors. To help the committee designate the winner, for each $i$, you must identify the positions of the letters that need to be deleted from $c_0$ and from $c_i$ so that by deleting them, one of the longest common subwords is obtained.

# Input data

Input file: `oracol.in`

* Line $1$ contains $N$, a non-zero natural number, representing the number of competitors;
* Line $2$ contains $c_0$, the word produced by the oracle;
* Lines $3$, $\\dots$, $N+2$ contain the words written by the $N$ competitors, one word per line;

# Output data

The output file `oracol.out` will contain $2 \\cdot N$ lines, representing the positions of the letters that need to be deleted. On each line $i$ ($i$ = $1$, $3$, $\\dots$, $2 \\cdot N - 1$) it will contain non-zero natural numbers, separated by a space, representing the positions from which letters will be deleted from the word produced by the oracle; on each line $j$ ($j$ = $2$, $4$, $\\dots$, $2 \\cdot N$) it will contain non-zero natural numbers, separated by a space, representing the positions from which letters will be deleted from the word of the competitor number $\\frac{j}{2}$.

# Constraints and clarifications

* $2 \\leq N \\leq 100$
* If there are multiple solutions, only one solution will be written in the file.
* If no letter needs to be cut from a word, the respective line in the input file will remain empty.

# Example

`oracol.in`
```
3
abc
abxd
aabxyc
acb  
```

`oracol.out`
```
3
3 4

1 4 5
3
2
```
