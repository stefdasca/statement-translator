During the vacation period, Bogdan got a job as a seller at a bakery. Here, candies are kept in $n$ jars, numbered from $1$ to $n$. Occasionally, out of boredom, Bogdan chooses two jars, takes a candy from each chosen jar, and then places the two candies in a third jar.

While waiting for customers, Bogdan studies the following problem: is it possible, through such moves, to gather all the candies into one single jar?

# Task

Given the number of jars and the number of candies in each jar, write a program to determine a sequence of moves such as the one described in the problem statement, through which all candies are gathered into one single jar.

# Input data

The input file `borcane.in` contains on the first line the natural number $n$, representing the number of jars. The second line contains $n$ natural numbers $b_1 \ b_2 \ \dots \ b_n$, separated by a space, representing, in order, the number of candies in each jar.

# Output data

The output file `borcane.out` will contain in order the executed moves, one move per line. A move is described by $3$ natural numbers separated by a space `a b c` with the meaning: "take one candy from jars $a$ and $b$ and place the two candies in jar $c$".

# Constraints and clarifications

* $4 \leq n \leq 100$
* $0 \leq b_i \leq 1\ 000$
* $b_1 + b_2 + \dots + b_n \geq 4$
* Initially, there are at least two jars containing candies.

# Example

`borcane.in`
```
4
2 2 2 2
```

`borcane.out`
```
1 2 4
2 3 4
1 3 4
```

## Explanation

Initially, there are $4$ jars containing $8$ candies. One possible solution is:
* Take one candy from jars $1$ and $2$ and put them in jar $4$: $1 \ 1 \ 2 \ 4$
* Take one candy from jars $2$ and $3$ and put them in jar $4$: $1 \ 0 \ 1 \ 6$
* Take one candy from jars $1$ and $3$ and put them in jar $4$: $0 \ 0 \ 0 \ 8$

In the end, all $8$ candies will be in jar $4$.