A party is being organized where $N$ boys (numbered from $1$ to $N$) and $N$ girls (numbered from $1$ to $N$) participate. It has been decided that the party will last several minutes. Every minute, the girls and boys form a dance configuration, meaning $N$ pairs, according to one of the following rules:

* boy $i$ dances with girl $i$;
* boy $i$ dances with girl $j$, then necessarily boy $j$ dances with girl $i$.

The pair $(i, j)$ indicates that boy $i$ dances with girl $j$. Two configurations are distinct if they differ by at least one pair. For $N = 7$, two possible dance configurations are:

* $(1, 1), (2, 2), (3, 7), (4, 5), (5, 4), (6, 6), (7, 3)$
* $(1, 1), (2, 2), (3, 3), (4, 5), (5, 4), (6, 6), (7, 7)$

# Task

Knowing that distinct dance configurations must be formed every minute, determine how many minutes the party will last.

# Input data

The input file `petrecere.in` contains on the first line a single natural number $N$.

# Output data

The output file `petrecere.out` will contain a single line which will print a single natural number representing the duration of the party in minutes.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* The answer is a natural number with a maximum of $3\ 000$ digits.
* For $20$\% of the tests, we will have $N \leq 11$.
* For another $20$\% of the tests, the result can be represented in $64$ signed bits.

# Example 1

`petrecere.in`
```
2
```

`petrecere.out`
```
2
```

## Explanation

For the first example, the dance configurations are:
$(1, 1), (2, 2)$
$(1, 2), (2, 1)$

# Example 2

`petrecere.in`
```
3
```

`petrecere.out`
```
4
```

## Explanation

$(1, 1), (2, 2), (3, 3)$  
$(1, 1), (2, 3), (3, 2)$  
$(1, 2), (2, 1), (3, 3)$  
$(1, 3), (2, 2), (3, 1)$