# A permutation with $N$ elements is a sequence $a_1, a_2, \dots, a_N$ that contains all the natural numbers $1, 2, \dots, N$, each number exactly once.

An example of a permutation with $6$ elements can be the following sequence: $[3, 1, 6, 4, 5, 2]$.
  
We say that a permutation is of mountain type, if among its $N$ elements there exists an element with index $M$ such that $1 < M < N$, and the sequence formed from the first $M$ elements is strictly increasing, while the sequence formed from the last $N-M+1$ elements is strictly decreasing. That is, using mathematical notation, we have $a_1 < a_2< \ldots < a_{M - 1}< a_M > a_{M+1} > \ldots > a_N$.

An example of a mountain with 6 elements can be the following sequence: $[1, 2, 4, 5, 6, 3]$. 

In our problem, we will consider that we have a permutation with $N$ elements indexed from $1$ to $N$. Upon the elements of the permutation, we can apply two types of symmetric swap operations:

* $swap(P, N-P+1)$ -- in the permutation $a$, the elements at positions $P$ and $N-P+1$ are swapped, equally distant from the two ends of the permutation. The operation requires $1 \leq P \leq N$ and $P \neq N-P+1$.
* $dswap(P, Q, N-P+1, N-Q+1)$ –- in the permutation $a$, two pairs of elements are swapped simultaneously. The elements at positions $P$ and $Q$, respectively the elements at positions $N-P+1$ and $N-Q+1$ are swapped simultaneously. The operation can be applied if and only if all four positions are distinct in pairs. In other words, the operation requires $1 \leq P, Q \leq N$ and the set $\{P, Q, N-P+1, N-Q+1\}$ to have a cardinality of four.

Starting from our permutation and successively applying these two types of operations, each type can be used *zero or more times*, various permutations can be obtained.

# Task

* Specify whether, for the given permutation, a mountain type permutation can be obtained by applying any number of swap or dswap operations.
* Starting from the given permutation, how many distinct mountain type permutations can be obtained by applying any number of swap or dswap operations?

# Input data

The file `munte.in` contains on the first line two natural numbers $C \in \{1, 2\}$ and $N$, representing the task to be solved, and the number of elements of the permutation $a$, respectively.

The second line contains $N$ natural numbers separated by a single space, representing the permutation $a$.

# Output data

The file `munte.out` will contain a single line, depending on the task:

* for $C = 1$, if at least one mountain type permutation can be obtained starting from the sequence $a$, print `YES`, otherwise `NO`;
* for $C = 2$, print a single natural number, representing the number of distinct mountain type permutations that can be obtained by applying only swap and dswap operations to the read permutation. Since this value can be very large, print the result modulo $111 \ 181 \ 111$.

# Constraints and clarifications

* $C \in \{1, 2\}$
* $4 \leq N \leq 200\ 000$

|#|Score|Constraints|
|-|-|--------|
|1|3|$C = 1$ and $N \leq 8$|
|2|3|$C = 2$ and $N \leq 8$|
|3|9|$C = 1$ and $N \leq 15$|
|4|9|$C = 2$ and $N \leq 15$|
|5|5|$C = 1$ and $N \leq 30$|
|6|6|$C = 2$ and $N \leq 30$|
|7|6|$C = 1$ and $N \leq 2\ 000$, $N$ odd and $a_{\frac{N+1}{2}} = N$|
|8|7|$C = 2$ and $N \leq 2\ 000$, $N$ odd and $a_{\frac{N+1}{2}} = N$|
|9|7|$C = 1$ and $N \leq 2\ 000$, $N$ even and $a_{\frac{N}{2}} = N$ and $a_{\frac{N}{2} + 1} = N-1$|
|10|8|$C = 2$ and $N \leq 2\ 000$, $N$ even and $a_{\frac{N}{2}} = N$ and $a_{\frac{N}{2} + 1} = N-1$|
|11|8|$C = 1$ and $N \leq 2\ 000$|
|12|9|$C = 2$ and $N \leq 2\ 000$|
|13|10|$C = 1$|
|14|10|$C = 2$|

# Example 1

`munte.in`
```
2 7
3 4 2 7 1 6 5
```

`munte.out`
```
4
```

## Explanation

$N = 7$ and $a = [3, 4, 2, 7, 1, 6, 5]$. We can obtain $4$ distinct mountain type permutations:

1. $dswap(1, 5, 7, 3)$ – $[\textcolor{red}{3}, 4, \textcolor{blue}{2}, 7, \textcolor{red}{1}, 6, \textcolor{blue}{5}]$ becomes $[1, 4, 5, 7, 3, 6, 2]$
$dswap(2, 5, 6, 3)$ – $[1, \textcolor{red}{4}, \textcolor{blue}{5}, 7, \textcolor{red}{3}, \textcolor{blue}{6}, 2]$ becomes $[1, 3, 6, 7, 4, 5, 2]$
$swap(3, 5)$ – $[1, 3, \textcolor{red}{6}, 7, \textcolor{red}{4}, 5, 2]$ becomes the mountain type permutation $[1, 3, 4, 7, 6, 5, 2]$

2. $dswap(1, 3, 7, 5)$ – $[\textcolor{red}{3}, 4, \textcolor{red}{2}, 7, \textcolor{blue}{1}, 6, \textcolor{blue}{5}]$ becomes $[2, 4, 3, 7, 5, 6, 1]$
$dswap(2, 3, 6, 5)$ – $[2, \textcolor{red}{4}, \textcolor{red}{3}, 7, \textcolor{blue}{5}, \textcolor{blue}{6}, 1]$ becomes the mountain type permutation $[2, 3, 4, 7, 6, 5, 1]$

3. $dswap(7, 2, 1, 6)$ – $[\textcolor{blue}{3}, \textcolor{red}{4}, 2, 7, 1, \textcolor{blue}{6}, \textcolor{red}{5}]$ becomes $[6, 5, 2, 7, 1, 3, 4]$
$dswap(5, 7, 3, 1)$ – $[\textcolor{blue}{6}, 5, \textcolor{blue}{2}, 7, \textcolor{red}{1}, 3, \textcolor{red}{4}]$ becomes the mountain type permutation $[2, 5, 6, 7, 4, 3, 1]$

4. $dswap(2, 5, 6, 3)$ – $[3, \textcolor{red}{4}, \textcolor{blue}{2}, 7, \textcolor{red}{1}, \textcolor{blue}{6}, 5]$ becomes $[3, 1, 6, 7, 4, 2, 5]$
$dswap(2, 1, 6, 7)$ – $[\textcolor{red}{3}, \textcolor{red}{1}, 6, 7, 4, \textcolor{blue}{2}, \textcolor{blue}{5}]$ becomes $[1, 3, 6, 7, 4, 5, 2]$
$swap(2, 6)$ – $[1, \textcolor{red}{3}, 6, 7, 4, \textcolor{red}{5}, 2]$ becomes the mountain type permutation $[1, 5, 6, 7, 4, 3, 2]$

# Example 2

`munte.in`
```
1 6
6 3 4 5 1 2
```

`munte.out`
```
YES
```

## Explanation

The following mountain type permutations can be obtained:
$1 \ 2 \ 4 \ 5 \ 6 \ 3$
$3 \ 6 \ 5 \ 4 \ 2 \ 1$

# Example 3

`munte.in`
```
1 6
1 2 3 5 4 6
```

`munte.out`
```
NO
```

## Explanation

There is no way to transform the permutation into a mountain.

# Example 4

`munte.in`
```
1 7
2 3 4 1 7 6 5
```

`munte.out`
```
NO
```

## Explanation

There is no way to transform the permutation into a mountain.