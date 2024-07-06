Sure, here is the translated and processed competitive programming problem statement according to your instructions:

---

We consider a sequence of $N$ non-zero natural numbers arranged in ascending order $a_1 \leq a_2 \leq \dots \leq a_N$. In connection with this sequence of numbers, we are interested in the pairs of positions $(i, j)$ with $1 \leq i < j \leq N$ and $a_i \neq a_j$ or we are interested in the _sum of the elements of certain subarrays_.

# Task

You are required to write a program that reads a number $C$ representing the type of task, a sequence of $N$ non-zero natural numbers arranged in ascending order $a_1 \leq a_2 \leq \dots \leq a_N$ and $T$ pairs of natural numbers $(p_k, q_k)$ with $1 \leq p_k < q_k \leq N$ and $1 \leq k \leq T$ and then:

* If $C = 1$, then for each given pair of natural numbers $(p, q)$ you need to determine the sum $a_p + a_{p+1} + \dots + a_q$.
* If $C = 2$, then for each given pair of natural numbers $(p, q)$ you need to determine the number of pairs $(i, j)$ that simultaneously meet the conditions $p \leq i < j \leq q$ and $a_i \neq a_j$.

# Input data

The input file `pp.in` contains on the first line the natural number $C$. The second line contains the number $N$. The third line contains $N$ non-zero natural numbers arranged in ascending order and separated by a space. The fourth line contains the natural number $T$, and each of the following $T$ lines contains two natural numbers separated by a space.

# Output data

If $C = 1$, then the output file `pp.out` will contain on each of the first $T$ lines a natural number. The $k$-th number will represent the sum of the elements between positions $p_k$ and $q_k$ inclusive.  
If $C = 2$, then the output file `pp.out` will contain on each of the first $T$ lines a natural number. The $k$-th number will represent the number of pairs of indices between positions $p_k$ and $q_k$ inclusive.

# Constraints and clarifications

* $1 \leq p_i < q_i \leq N \leq 100 \ 000$
* $1 \leq a_1 \leq a_2 \leq \dots \leq a_N \leq 100 \ 000$
* $1 \leq T \leq 1 \ 000$

# Example 1

`pp.in`
```
1
5
1 2 3 3 3
2
1 4
2 5
```

`pp.out`
```
9
11
```

## Explanation

We are in case $C = 1$. The first pair $(p, q)$ is $(1, 4)$. The sum of the values in the subarray is $1$ + $2$ + $3$ + $3$ = $9$. The second pair $(p, q)$ is $(2, 5)$. The sum of the values in the subarray is $2$ + $3$ + $3$ + $3$ = $11$.

# Example 2

`pp.in`
```
2
5
1 2 3 3 3
2
1 4
2 5
```

`pp.out`
```
5
3
```

## Explanation

We are in case $C = 2$. The first pair $(p, q)$ is $(1, 4)$. The pairs of positions that contain different numbers between them are $(1, 2)$, $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$. Thus, there are $5$ pairs.  
The second pair $(p, q)$ is $(2, 5)$. The pairs of positions that contain different numbers are $(2, 3)$, $(2, 4)$, $(2, 5)$. Thus, there are $3$ pairs.

---

I have reviewed the translation and ensured that there are no grammar or syntax errors according to the rules of the English language.