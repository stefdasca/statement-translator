
# Task

After 5 minutes of continuous work, the famous mathematician brothers Srep and Pep proposed the concept of *distance* between two natural numbers with the same number of digits.

This *distance* is defined as the number of positions where the corresponding digits of the two numbers differ. For example, the distance between $10234$ and $20431$ is equal to $3$, as they differ at the unit digit, the hundred digit, and the ten-thousands digit.

Following the success of this concept, the two brothers thought of studying the *p-distance* of $t$ natural numbers. The *p-distance* of a natural number $x$ is defined as the minimum distance between $x$ and any prime number $p$ with the same number of digits as $x$.

Unfortunately, *p-distance* is difficult to calculate on paper. For this reason, you have been hired to join their research team to write a program that can calculate the *p-distance* of the given $t$ numbers.

# Input data

The input file `pdist.in` will contain:

- The first line contains a number $t$ ($1 \le t \le 10$) — the length of the list of numbers studied by the brothers.
- Each of the following $t$ lines contains a number $n$ ($1 \le n < 1\,000\,000\,000$), for which you need to calculate the *p-distance*.

# Output data

The output file `pdist.out` will contain $t$ numbers, the \texttt{p-distances} of the $t$ numbers from the input file.

# Constraints and clarifications
|#|Points|Constraints                             |
|-|-------|---------------------------------------|
|1| 10    | $n < 10$                              |
|2| 30    | $n < 1\,000$                          |
|3| 25    | $n < 100\,000$                        |
|4| 20    | $n < 1\,000\,000$                     |
|5| 15    | No additional restrictions            |

# Example 1

`pdist.in`

```
5
1
200
89
95
8878
```

`pdist.out`
```
1
2
0
1
2
```

## Explanation 

- The minimum distance between $1$ and another single-digit prime number, such as $2$, $3$, $5$, or $7$, is equal to $1$.
- The minimum distance between $200$ and another three-digit prime number is equal to $2$. Examples of three-digit prime numbers at a distance of $2$ from $200$ are $107$, $211$, and $293$.
- $89$ is a prime number, so its *p-distance* is equal to $0$.
