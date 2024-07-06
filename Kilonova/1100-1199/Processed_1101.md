A number is called triprime if it is the product of three distinct prime numbers. Examples of triprime numbers: $30 = 2 \times 3 \times 5$, $42 = 2 \times 3 \times 7$, $231 = 3 \times 7 \times 11$. Examples of numbers that are not triprime: $77 = 7 \times 11$ (too few prime numbers in the product), $3003 = 3 \times 7 \times 11 \times 13$ (too many prime numbers in the product), $18 = 2 \times 3 \times 3$ (the prime numbers are not distinct), $10241 = 7 \times 7 \times 11 \times 19$ (too many prime numbers in the product).

# Task

Given the numbers $A$ and $B$, display the number of triprime numbers in the interval [$A, B$] (including $A$ and $B$).

# Input data

The input file `triprime.in` contains on the first line two natural numbers $A$ and $B$, separated by a single space.

# Output data

The output file `triprime.out` will contain the number of triprime numbers in the interval [$A, B$].

# Constraints and clarifications

* $1 \leq A \leq B \leq 390 \ 000 \ 000$

|#|Score|Constraints|
|-|-|---------|
|1|18|$1 \leq B \leq 1 \ 500 \ 000$|
|2|6|$1 \ 500 \ 000 < B \leq 2 \ 500 \ 000$|
|3|20|$2 \ 500 \ 000 < B \leq 4 \ 500 \ 000$|
|4|31|$4 \ 500 \ 000 < B \leq 35 \ 000 \ 000$|
|5|25|There are no other constraints.|

# Example 1

`triprime.in`
```
1 50
```

`triprime.out`
```
2
```

## Explanation

There are two triprime numbers from $1$ to $50$: $30 = 2 \cdot 3 \cdot 5$ and $42 = 2 \cdot 3 \cdot 7$.

# Example 2

`triprime.in`
```
50 105
```

`triprime.out`
```
5
```

## Explanation

There are five triprime numbers from $50$ to $105$: $66 = 2 \cdot 3 \cdot 11$, $70 = 2 \cdot 5 \cdot 7$, $78 = 2 \cdot 3 \cdot 13$, $102 = 2 \cdot 3 \cdot 17$ and $105 = 3 \cdot 5 \cdot 7$.

# Example 3

`triprime.in`
```
1000 3000
```

`triprime.out`
```
348
```

## Explanation

There are $348$ triprime numbers in the interval [$1 \ 000, 3 \ 000$].