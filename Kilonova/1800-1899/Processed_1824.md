Given a sequence $s = s_0, s_1, \ldots, s_{n-1}$ of $n$ lowercase letters. By $s[i..j]$ we mean the subsequence $s_i, s_{i+1}, \ldots, s_j$. The sequence undergoes several $switch(i, j, c_1, c_2)$ operations, which transform any occurrence of the letter $c_1$ into the letter $c_2$ in the subsequence $s[i..j]$. For example, if $s = abcdaabcdaaab$, then $switch(0,5,'a','z')$ results in the sequence becoming $s = zbcdzzbcdaaab$.

# Task

Given the sequence $s$ and $m$ switch operations, display the sequence $s$ after performing all $m$ operations.

# Input data

The file `switchletters.in` contains on the first line the sequence $s$, on the second line the natural number $m$, and on the following $m$ lines, there are two natural numbers and two lowercase English alphabet letters, separated by a space $i \ j \ c_1 \ c_2$, representing the $switch(i,j,c_1,c_2)$ operation.

# Output data

The file `switchletters.out` contains the sequence $s$ after performing all $m$ operations.

# Constraints and clarifications

* The sequence $s$ contains at most $1 \ 000 \ 000$ lowercase letters: $1 \le n \le 1 \ 000 \ 000$.
* The sequence $s$ contains only lowercase letters.
* In a $switch(i, j, c_1, c_2)$ operation, always $0 \leq i \leq j < n$, and $c_1 \ne c_2$.
* $1 \leq m \leq 2^{17}$.

|#|Points|Constraints|
|-|-|--------|
|1|16|$1 \le n, m \leq 2^{10}$|
|2|48|$2^{10} < n, m \leq 2^{16}$|
|3|36|No other constraints.|

# Example 1

`switchletters.in`
```
aaaabbbbcccc
3
0 2 a y
5 9 b c
1 3 a z
```

`switchletters.out`
```
yyyzbccccccc
```

## Explanation

For the first example, After the $switch(0,2,’a’,’y’)$ operation, $s=yyyabbbbcccc$.
After the $switch(5,9,’b’,’c’)$ operation, $s=yyyabccccccc$.
After the $switch(1,3,’a’,’z’)$ operation, $s=yyyzbccccccc$

# Example 2

`switchletters.in`
```
anaaremere
2
3 6 z y
2 7 o x
```

`switchletters.out`
```
anaaremere
```

## Explanation

For the second example, $s$ remains unchanged because the letters $z$ and $o$ do not appear in the sequence.
