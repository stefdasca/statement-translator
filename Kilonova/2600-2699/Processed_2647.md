Given a sequence $A$ with $N$ elements, non-zero natural numbers, and a natural number $K$.

A subarray of the sequence is a sequence formed from one or more elements found on consecutive positions in the initial sequence.

We say that a value $x$ is called a majority element of a sequence of length $m$, if it appears in it at least $\lfloor \frac{m}{2} \rfloor + 1$ times.

# Task

Display the values that are majority elements for at least one subarray of length greater than or equal to $K$ of the sequence $A$.

# Input data

The first line of the file `kmajo.in` contains the natural numbers $N$ and $K$, with the meaning from the statement, and the second line contains $N$ natural numbers, representing the elements of the array $A$. The values on the same line are separated by a space.

# Output data

The file `kmajo.out` contains on the first line the required values, in strictly increasing order, separated by a space, or the value $-1$ if there is not at least one value that meets the imposed constraints.

# Constraints and clarifications

* $1 \leq K \leq N \leq 1 \ 000 \ 000$
* $1 \leq A_i \leq N$, $\forall i$, $1 \leq i \leq N$

|#|Points|Constraints|
|-|-|--------|
|1|11|$K = N$|
|2|16|$N \leq 1 \ 000$|
|3|22|$N \cdot K \leq 30 \ 000 \ 000$|
|4|30|$N \leq 100 \ 000$|
|5|21|No additional constraints|

# Example

`kmajo.in`
```
12 3
2 2 1 3 4 2 2 3 3 3 4 4
```

`kmajo.out`
```
2 3 4
```

## Explanation

$2$ is a majority element in multiple subarrays of length greater than or equal to $3$, an example being: $2 \ 2 \ 1 \ 3 \ \textcolor{red}{4 \ 2 \ 2} \ 3 \ 3 \ 3 \ 4 \ 4$.

$3$ is a majority element in multiple subarrays of length greater than or equal to $3$, an example being: $2 \ 2 \ 1 \ 3 \ 4 \ \textcolor{red}{2 \ 2 \ 3 \ 3 \ 3} \ 4 \ 4$.

$4$ is a majority element in the following highlighted subarray of length greater than or equal to $3$. $2 \ 2 \ 1 \ 3 \ 4 \ 2 \ 2 \ 3 \ 3 \ \textcolor{red}{3 \ 4 \ 4}$.