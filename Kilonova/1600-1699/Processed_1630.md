## Task

Given a nonzero natural number **n**, $n > 1$. We define $n(p)$ as the decomposition of $n$ into a **sum** of **distinct natural powers** of the **prime number $p$**. Examples:
* for $n=10$ all possible $n(p)$ decompositions are: $10(2)=2^1+2^3$ and $10(3)=3^0+3^2$
* for $n=11$ all possible $n(p)$ decompositions are: $11(2)=2^0+2^1+2^3$ and $11(11)=11^1$.

## Task

Write a program that reads a natural number $n$ and determines all $n(p)$ decompositions of the number $n$.

## Input data

The input file `desc.in` contains in the first line the natural number $n$.

## Output data

The output file `desc.out` will contain on separate lines all $n(p)$ decompositions of the number $n$. Each line will contain, in order:
* a natural value $p$ representing the prime number associated with the decomposition;
* a natural value $k$, representing the number of terms in the decomposition;
* The next $k$ natural values, representing the exponents of the powers in the decomposition, written in ascending order.

## Constraints and clarifications

* $2 \leq n \leq 10 \ 000 \ 000$;
* For a fixed prime number $p$, there is a single $n(p)$ decomposition of a natural number $n$;
* The decompositions will be displayed in ascending order of the identified values for $p$;
* On each line of the output file, the values will be separated by a single space;

## Example 1

`desc.in`
```
10
```

`desc.out`
```
2 2 1 3
3 2 0 2
```

### Explanation

$10(2)=2^1+2^3$ ; $10(3)=3^0+3^2$. The first decomposition is done using the prime number $p=2$ and contains **2 terms** with the powers $1$ and $3$; The second decomposition is done using the prime number $p=3$ and contains **2 terms** with the powers $0$ and $2$.

## Example 2

`desc.in`
```
11
```

`desc.out`
```
2 3 0 1 3
11 1 1
```

### Explanation

$11(2)= 2^0+2^1+2^3$; $11(11)=11^1$. The first decomposition is done using the prime number $p=2$ and contains **3 terms** with the powers $0$, $1$ and $3$; The second decomposition is done using the prime number $p=11$ and contains **1 term** with the power $1$.