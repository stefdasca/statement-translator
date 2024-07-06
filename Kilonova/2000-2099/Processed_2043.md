# Task

A number $x$ is *special* if it simultaneously satisfies the following conditions:

- $x$ is prime.
- There exist two prime numbers $y$ and $z$ such that $x = y + z$.

For example, $5$ is *special* because $5 = 2 + 3$, and $2$, $3$, and $5$ are prime numbers.

You are given two numbers $n$ and $q$, followed by $q$ queries of the type:

- `l r` ($1 \le l \le r \le n$): How many special numbers $x$ exist such that $l \le x \le r$? 

# Input data

The first line of the input file `sprime.in` will contain two natural numbers $n$ and $q$ - the maximum possible value of the numbers, respectively the number of queries.

Each of the following $q$ lines will contain two numbers $l$ and $r$ - the ends of the queries.

# Output data

The output file `sprime.out` will contain $q$ numbers, the answers to the $q$ queries.

# Constraints and clarifications

- $1 \le n \le 5 \cdot 10^6$;
- $1 \le q \le 2 \cdot 10^5$;
- $1 \le l \le r \le n$;
- A number $x$ is prime if it has exactly two divisors, $1$ and $x$. Therefore, $0$ and $1$ **are not** prime numbers.
- For $10$ points, $n,q \le 50$;
- For an additional $10$ points, $n,q \le 500$;
- For an additional $15$ points, $n,q \le 5\ 000$;
- For an additional $10$ points, $n \le 5\ 000$;
- For an additional $10$ points, $n,q \le 10^5$, and for all queries we have $l=r$;
- For an additional $10$ points, for all queries we have $l=r$;
- For an additional $20$ points, $n,q \le 10^5$;
- For the remaining $15$ points, no additional constraints are imposed.

# Example 1

`sprime.in`
```
10 5
5 5
7 7
1 10
1 4
6 10
```

`sprime.out`
```
1
1
2
0
1
```

## Explanation

The only special numbers from $1$ to $10$ are $5=2+3$ and $7=2+5$.

# Example 2

`sprime.in`
```
500 1
1 500
```

`sprime.out`
```
24
```

## Explanation

There are 24 special numbers less than or equal to $500$.