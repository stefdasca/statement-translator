# Task

Given $n$ and an array $a$ of $n$ integers, Majoritar wants to split the array into three non-empty parts (each containing at least one element), so that the sum of the *majority elements* of the three parts is maximal.

We define the majority element of an array $b$ as the value that appears the most frequently in $b$. If there are multiple such values (appearing the same number of times), the majority element will be the largest among them.

For more details, see the examples.

# Input data

The first line will contain an integer $n$, representing the number of elements in the array $a$. The next line will contain $n$ integers, representing the array $a$.

# Output data

The first line should contain a single integer, representing the maximal sum of the majority elements that can be obtained from a partition.

# Constraints and clarifications

* $3 \leq N \leq 2 \ 000$
* $1 \leq a_i \leq 1 \ 000 \ 000$
* For 40 points, $1 \leq N \leq 500$

# Example 1

`stdin`
```
7
1 2 2 3 3 3 1
```

`stdout`
```
8
```

## Explanation

The partition is $1 \ 2 \ 2 \ | \ 3 \ | \ 3 \ 3 \ 1$. The result is $2 + 3 + 3 = 8$. It can be demonstrated that there is no better partition than this.

# Example 2

`stdin`
```
6
4 4 5 5 5 6
```

`stdout`
```
16
```

## Explanation

The partition is $4 \ 4 \ 5 \ 5 \ | \ 5 \ | \ 6$. The result is $5 + 5 + 6 = 16$. It can be demonstrated that there is no better partition than this.