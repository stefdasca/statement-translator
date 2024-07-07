
# Task

A string consisting of the letters `'a'`, `'b'`, and `'c'` is *good* if there are no `'a'` and `'b'` located at consecutive positions.

For example, `aaaa`, `c`, and `bcaacb` are *good*, while `bac` and `acab` are not *good*.

How many *good* strings containing $a$ of `'a'`, $b$ of `'b'`, and $c$ of `'c'$ are there? Since the answer can be very large, print the remainder of its division by $10^9+7$.

# Input data

The input file `abc.in` will contain three numbers $a$, $b$ and $c$ on the first line.

# Output data

The output file `abc.out` will contain the remainder of the division by $10^9+7$ of the number of *good* strings containing $a$ of `'a'$, $b$ of `'b'`, and $c$ of `'c'$.

# Constraints and clarifications
- $1 \le a,b,c \le 5 \ 10^5$;
- For $5$ points, $c = 1$;
- For another $20$ points, $c = 2$;
- For another $10$ points, $a,b,c \le 5$;
- For another $20$ points, $a,b,c \le 100$;
- For another $15$ points, $a,b,c \le 2\ 000$;
- For the remaining $30$ points, no additional constraints.

# Example 1

`abc.in`
```
1 1 2
```

`abc.out`
```
6
```

## Explanation

The 6 good strings are: `acbc`, `accb`, `bcac`, `bcca`, `cacb`, and `cbca`.

# Example 2

`abc.in`
```
2 2 2
```

`abc.out`
```
12
```

## Explanation

The 12 good strings are: `aacbbc`, `aacbcb`, `aaccbb`, `acacbb`, `acbbca`, `bbcaac`, `bbcaca`, `bbccaa`, `bcaacb`, `bcbcaa`, `caacbb`, and `cbbcaa`.

# Example 3

`abc.in`
```
21 35 29
```

`abc.out`
```
306014034
```

## Explanation

The answer must be displayed modulo $10^9+7$.
