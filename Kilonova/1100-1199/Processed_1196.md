For homework, Alina needed to check her knowledge about prime numbers. Alina will read a value $N$ which signifies the number of natural numbers that will be processed and a value $C$ which can be $1$ or $2$. Next, she will read the $N$ natural numbers. Each natural number $A$ read will be processed as follows:

* if $A$ is a prime number, it will be displayed unchanged;
* if $A$ is not a prime, the closest prime number will be determined and displayed. We consider the closest number to the value $A$ to be the one for which the absolute difference between the number and the value $A$ is the smallest. Let $X$ be the largest prime number smaller than $A$, and $Y$ be the smallest prime number larger than $A$. If the two numbers are equally "close" to $A$ then $X$ will be displayed if $C=1$ and $Y$, if $C=2$.

# Task

Display the processed values of each number $A$.

# Input data

The input file `prime.in` contains on the first line two numbers, $N$ representing the number of numbers to be read and $C$, the value that will decide if the closest smaller or larger prime value corresponding to the processed value will be displayed. The second line contains $N$ numbers separated by space, each noted with $A$; the natural numbers that will be processed.

# Output data

In the output file `prime.out` write on a single line the $N$ natural numbers, separated by space representing the prime numbers "close" to the initial ones.

# Constraints and clarifications

* $0 \leq N \leq 100 \ 000$;
* $1 < A \leq 4 \ 000 \ 000$;
* $1 \leq C \leq 2$.

# Example 1

`prime.in`
```
15 1
3 6 8 2 3 5 7 9 2 5 3 7 11 22 21
```

`prime.out`
```
3 5 7 2 3 5 7 7 2 5 3 7 11 23 19
```

# Example 2

`prime.in`
```
13 2
3 6 7 11 21 9 5 7 14 29 24 25 16
```

`prime.out`
```
3 7 7 11 23 11 5 7 13 29 23 23 17
```

