
# Task

Gary was in math class, learning about prime factorization, when his teacher gave him a problem: given $a$ and $b$; find their greatest common divisor, their least common multiple, and their product. Gary solved the problems quickly, writing the three answers on three different sheets of paper. Then, the bell rang, and Gary went to the lunch line to grab as much food as possible.

However, when he returned, one of the papers was missing. One of his classmates punished him for his greed. Furthermore, he no longer knows which paper has which number, nor does he remember the values $a$ and $b$.

Given the two values from the remaining papers, find all possible **distinct** values for the third value for each of the $T$ test cases.

# Input data

The first line contains $T$, the number of test cases. Each of the following $T$ lines contains two numbers $a_i$ and $b_i$, representing the two numbers he has left.

# Output data

For each of the $T$ test cases, the answer will be displayed as follows:

The first number represents the number of possible values for the third value (let's denote it $n_i$), and the next $n_i$ values on that line represent the different values for that value, in ascending order.

If there is no valid solution, print $0$.

# Constraints and clarifications

* $1 \leq T \leq 10^5$;
* $1 \leq a_i, b_i \leq 10^9$;
* The test cases will be evaluated **individually**.

# Example

`stdin`
```
8
5 7
4 2
10 3
9 3
6 12
2 2
2 256
3 7
```

`stdout`
```
0
2 2 8
0
2 3 27
2 2 72
2 1 4
2 128 512
0
```
