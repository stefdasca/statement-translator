Mara's grandma is knitting a carpet. Mara is carefully observing the pattern and trying to recreate it in her math notebook. The pattern consists of diamonds. The first diamond, with index $1$, has a side formed of two squares, the second diamond, with index $2$, has a side formed of three squares, etc. A diamond with index $i$ has a side formed of $i+1$ squares.

The diamonds are joined consecutively, as shown in the adjacent image. The arrows indicate the direction in which grandma knits the carpet. To not forget the pattern, Mara writes consecutive numbers starting with 1 in her notebook to indicate how her grandma knits the carpet. The following example shows how a pattern consisting of four diamonds is knitted.

~[covor.png]

~[covor1.png]

# Task

Given two numbers $n$ and $k$, determine:

* the maximum number of complete diamonds that can form the pattern of a carpet, described using a sequence formed of at most $n$ consecutive natural numbers (the first number in the sequence being $1$);
* the smallest index of a diamond that contains the number $k$.

# Input data

The input file `covor.in` contains:

* the first line contains two natural numbers separated by space: $n$ (representing the maximum number of consecutive numbers used to describe a pattern) and $k$ (representing a number from the sequence of those $n$ consecutive numbers).
* the second line contains one of the values $1$ or $2$:
  * $1$ if the task is to determine the maximum number of complete diamonds that can form the pattern of a carpet described using a sequence formed of at most $n$ numbers;
  * $2$ if the task is to determine the smallest index of a diamond that contains the number $k$.

# Output data

The output file `covor.out` contains:

* the first line contains a natural value representing the maximum number of complete diamonds that can form the pattern of a carpet described using a sequence formed of at most $n$ numbers if the task was $1$;
* a natural number representing the smallest index of a diamond that contains the number $k$ if the task was $2$.

# Constraints and clarifications

* $4 \leq n, k \leq 999\ 999\ 999$;
* $1 \leq k \leq n$;
* If the number $k$ is not on any of the complete diamonds that can be constructed using a maximum of $n$ numbers, then the answer for task $2$ is $0$;
* For the correct resolution of task $1$, $30$\% of the score is awarded, and for the correct resolution of task $2$, $70$\% of the score is awarded.

# Example 1

`covor.in`
```
40 32
1
```

`covor.out`
```
4
```

## Explanation

The largest number of diamonds that can form a pattern described with a maximum of $40$ numbers is $4$.

# Example 2

`covor.in`
```
40 32
2
```

`covor.out`
```
3
```

## Explanation

The number $32$ is on the third diamond.

# Example 3

`covor.in`
```
37 7
2
```

`covor.out`
```
2
```

## Explanation

The number $7$ is on both the second and third diamonds. The smallest index of a diamond that contains the number $7$ is $2$.

# Example 4

`covor.in`
```
14 12
2
```

`covor.out`
```
0
```

## Explanation

The number $12$ **is not** on any of the two diamonds that can form a pattern described with a maximum of $14$ numbers.