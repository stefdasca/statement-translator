# Task

Among Mihai Eminescu's sketches, this problem was found (just kidding, we made it).

## Task

Given $n$ and an array $a$ of natural numbers, we define an operation as follows:

Choose two positions $i$ and $j$. Swap the **digits in the even positions** of $a_i$ and $a_j$. What is the maximum and minimum number that can be obtained in the array after a certain number of operations?

For example, for the number $14 \ 563$:

* digit $3$ is in position $1$
* digit $6$ is in position $2$
* digit $5$ is in position $3$
* digit $4$ is in position $4$
* digit $1$ is in position $5$

## Input data

The first line contains an integer $n$. The next line contains $n$ integers, representing the array $a$.

## Output data

The first line will contain two integers, the maximum number, and respectively the minimum number, that can be obtained after any number of operations.

## Constraints and clarifications

* $2 \leq n \leq 100 \ 000$;
* $10 \leq a_i < 1 \ 000 \ 000 \ 000$, for $i$ from $1$ to $n$;
* For $4$ points, $n=2$
* For $4$ points, $n=3$
* For $5$ points, $n=4$
* For $40$ points, $n \leq 5 \ 000$;
* **Attention!** All numbers in the array have the same number of digits.
* **Attention!** The maximum number and the minimum number do not need to be obtained after the same operations. For example, we can first obtain the maximum number after a few operations, and after a few other operations, modify this maximum number and obtain a minimum number.

## Example 1

`stdin`
```
5
1938 1929 9575 3938 7261
```

`stdout`
```
9979 1221
```

### Explanation

We can perform the operation on $1 \ 929$ and $7 \ 261$, after which they will become $7 \ 969$ and $1 \ 221$, then perform the operation on $7 \ 969$ and $9 \ 575$, becoming $9 \ 979$ and $7 \ 565$. It can be demonstrated that $1 \ 221$ is the smallest number that can be obtained, and $9 \ 979$ is the largest number that can be obtained.

## Example 2

`stdin`
```
2
644 312
```

`stdout`
```
644 312
```

### Explanation

We can leave the numbers as they are.

## Example 3

`stdin`
```
4
140 200 665 923
```

`stdout`
```
963 100
```

### Explanation

I'm lazy, do it yourself. 😊