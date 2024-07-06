> *Colegiul Național “Frații Buzești”* ~[logos.png|align=right|width=20rem]
> *Centrul de Pregătire pentru Performanță în Informatică*
> **InfoCNFB** - Second Edition, Seniors
> December 9, 2023

# Task

We say that a sequence $(a_1, a_2, \dots, a_t)$ is a plagiarism of the sequence $(b_1, b_2, \dots, b_t)$ if $a_1 - b_1 = a_2 - b_2 = \dots = a_t - b_t$.

Given two sequences: $A$ of length $N \ (A_1, A_2, \dots, A_N)$ and $B$ of length $M \ (B_1, B_2, \dots, B_M)$, we want to determine the longest subarray in $A$ for which there is a subarray in $B$ that is a plagiarism of it. In other words, if $L$ is the maximum length sought, there exist $i$ and $j$ such that $(A_i, A_{i+1}, \dots, A_{i+L-1})$ is a plagiarism of the subarray $(B_j, B_{j+1}, \dots, B_{j+L-1})$.

Display the triplet $(L, i, j)$. If there are multiple solutions with maximum length, we prefer the one with the smallest $i$, if there are still multiple solutions, we will prefer the one with the smallest $j$.

# Input data

The file `plagiat.in` contains on the first line the number $n$. The second line contains $n$ natural numbers separated by space, representing the elements of the array $A$. The third line contains a natural number $m$. The fourth line contains $m$ natural numbers separated by space, representing the elements of the array $B$.

# Output data

The first line of the file `plagiat.out` contains the three natural numbers $L$, $i$, $j$, separated by spaces, with the meaning described above.

# Constraints and clarifications

* $1 \leq n, m \leq 100\ 000$;
* $0 \leq A_i, B_i \leq 1\ 000$;
* For $36$ points, $n, m \leq 300$;
* For another $24$ points, $n, m \leq 4\ 000$;
* For another $16$ points, $n, m \leq 10\ 000$;
* For the remaining $24$ points, there are no additional constraints.

# Example

`plagiat.in`
```
13
10 12 20 6 4 5 7 6 4 5 21 11 12
17
13 14 12 7 6 7 9 8 6 7 9 8 6 7 1 1 2
```

`plagiat.out`
```
7 4 8
```

