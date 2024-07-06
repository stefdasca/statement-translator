Algorel is very fond of sequences of natural numbers with as weird properties as possible. While looking for such oddities in computer science, he found in a dusty old book a new type of sequence called a fan. A fan is a sequence with an even number of terms, $E_1 \\ E_2 \\dots E_{2 \\cdot K}$, with the following property:

\[ E_1 + E_{2 \cdot K} > E_2 + E_{2 \cdot K - 1} > \dots > E_K + E_{K+1} \]

# Task

Given a sequence of distinct natural numbers $A_1 A_2 \\dots A_N$, Algorel wants to find how many of its subsequences are fans.

# Input data

The first line of the file `evantai.in` contains the integer number $N$, representing the number of elements in the sequence. The next $N$ lines contain, in order, the elements of the sequence $A$.

# Output data

The first line of the file `evantai.out` will contain a single integer $C$, representing the number of fan subsequences. The result will be printed modulo $30 \ 103$.

# Constraints and clarifications

* $2 \leq N \leq 700$
* The elements of the sequence are distinct integers between $1$ and $1 \ 000$
* A subsequence is any sequence of terms $A_{i_1} \\ A_{i_2} \\dots A_{i_k}$ such that $i_1 < i_2 < \dots < i_k$

# Example

`evantai.in`
```
4
1
2
3
6
```

`evantai.out`
```
7
```

