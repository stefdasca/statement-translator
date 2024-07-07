
Consider an alphabet with $\Sigma$ characters. We denote $lcp(S, P)$ as the longest common prefix between a string $S$ and a string $P$. For a string $S$, we will denote $SuffixS[i]$ as the suffix of the string $S$ starting at position $i$. Given the string $S$, we will create the array $A[i] = lcp(S, SuffixS[i])$.

# Task

Knowing the array $A$ and the length of the alphabet $\Sigma$, determine how many strings $S$ generate the array $A$.

# Input data

The input file `reversez.in` will contain two natural numbers $N$ and $\Sigma$ on the first line, with the meaning stated in the problem. On the second line, it will contain $N$ natural numbers representing the array $A$.

# Output data

The output file `reversez.out` will contain a single natural number representing the number of strings $S$ required, modulo $666 \ 013$.

# Constraints and clarifications

* $ 1 \leq N \leq 300 \ 000$;
* $ 1 \leq \Sigma \leq 100 \ 000$;
* The number of solutions will be at least $1$.

# Example

`reversez.in`
```
4 3
4 1 0 1
```

`reversez.out`
```
6
```

## Explanation

If $\Sigma={1,2,3}$, the $6$ possible strings $S$ are:
`1121`, `1131`, `2212`, `2232`, `3313`, `3323`
