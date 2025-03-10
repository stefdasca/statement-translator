
# Task

It is a beautiful spring day, and while you were reading memes on [RoAlgo](https://discord.gg/roalgo), you found out about the existence of a mysterious and ancient cartoon channel called Minimax. While nostalgically watching what your parents used to watch when they were little, you remembered the following problem:

You are given two numbers $n$ and $k$. We will run the following algorithm $k$ times:

Take the digits of $n$, find the minimum and maximum digits, and add the product of the minimum and maximum digits to $n$.

If the number is $633$, the minimum digit is $3$ and the maximum digit is $6$, so we add $18$, and the number becomes $651$. After another step, the number would become $657$ because we would add $6$ (the minimum digit is $1$ and the maximum digit is $6$).

Find the final value of $n$ after $k$ steps of this algorithm. Since this is too easy, it asks you to solve the problem for $t$ such pairs.

# Input data

The first line of the input file `minimax.in` contains $t$, the number of pairs.

The next $t$ lines contain two numbers each, $n$ and $k$, representing the initial number and the number of necessary steps.

# Output data

The output file `minimax.out` will have $t$ lines, containing the answers for the $t$ pairs of data.

# Constraints and clarifications

* $1 \leq t \leq 1 \ 000$;
* $1 \leq n, k \leq 1 \ 000 \ 000 \ 000$;
* For tests worth $40$ points, $1 \leq t \leq 10$ and $1 \leq k \leq 100 \ 000$.

# Example

`minimax.in`
```
5
581 1
581 2
581 3
581 4
581 5
```

`minimax.out`
```
589
634
652
664
688
```

## Explanation

In the first step, $581$ has the minimum digit $1$ and the maximum digit $8$, so we add $8$ to the result, reaching $589$.

In the second step, $589$ has the minimum digit $5$ and the maximum digit $9$, so we add $5 \cdot 9 = 45$.

We will let you analyze the other steps yourself.
