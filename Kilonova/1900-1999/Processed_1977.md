
# Task

You are given a number $t$ and $t$ natural numbers. For each of them, check whether it is a _palindrome_ or not.

A number is a _palindrome_ if its writing from left to right is identical to its writing from right to left. For example, the numbers $8$, $5995$, $101$ and $76967$ are _palindrome_ numbers, but the numbers $59343$, $19120$, $100$ or $3592923$ are not _palindrome_ numbers.

# Input data

The first line contains $t$, the number of numbers for which we need to check the required property stated in the task. The next $t$ lines will contain the numbers for which we need to check the given property.

# Output data

The $i$-th line will contain `YES` if the $i$-th term out of the $t$ is a _palindrome_, or `NO` otherwise.

# Constraints and clarifications

* $1 \leq t \leq 100 \ 000$;
* The $t$ numbers will be less than or equal to $9 \ 999 \ 999 \ 999$.
* For tests worth $60$ points, the $t$ numbers will be less than or equal to $999 \ 999 \ 999$.

# Example

`stdin`
```
5
401
54345
99
102919201
58353
```

`stdout`
```
NO
YES
YES
YES
NO
```

## Explanation

The mirror images of the numbers in the sequence are $104$, $54345$, $99$, $102919201$, and $35383$.
```
