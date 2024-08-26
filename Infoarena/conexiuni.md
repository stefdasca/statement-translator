# Connections

Recently, it was discovered that there might be certain connections between extraterrestrial civilizations and strings of the English alphabet. The king of the planet asks you to investigate these connections. He provides you with two strings $A$ and $B$ that contain only letters of the English alphabet (from $a$ to $z$) and asks you to tell him for each subsequence in string $A$ how many times it appears in string $B$. Let $NR_{i,j}$ denote the number of appearances in string $B$ of the subsequence found between positions $i$ and $j$ in string $A$. The king of the planet asks you to calculate for each pair $(i, j)$ with $i \leq j$ the value $NR_{i,j} \oplus i \oplus (j+1)$ and sum these values.

## Input data

The input file `conexiuni.in` contains on the first line two numbers separated by a single space, $N$ and $M$ representing the length of string $A$, respectively of string $B$. The next line contains a string of $N$ characters representing string $A$, and the last line contains a string of $M$ characters representing string $B$.

## Output data

In the output file `conexiuni.out` you will print a single number, the sum of the values requested by the king of the planet.

## Constraints and clarifications

$1 \leq N$  
$N \leq M$  
$M \leq 5000$  
The operator $\oplus$ has the same meaning as the operator $^$ in C/C++ or xor in Pascal  
The formula used in calculating the values to be summed has no peculiarity; the commission's solution solves the problem regardless of the formula used

## Example

`conexiuni.in`  
```
5 6  
abaaa  
ababaa  
```

`conexiuni.out`  
```
73  
```

## Explanation

The subsequence $aba$ from string $A$ found between positions $1$ and $3$ appears twice in string $B$. The first time it is found between positions $1$ and $3$ of the string, and the second time between positions $3$ and $5$. Thus, we must add to the result the value $2 \oplus 1 \oplus 4$.