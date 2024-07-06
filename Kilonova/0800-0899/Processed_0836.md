```markdown
Consider a sequence of numbers $a_1, a_2, \dots, a_N$. A non-empty subarray in this sequence is of the form $a_i, a_{i+1}, \dots, a_j$, where $i \leq j$. For example, for $N = 4$ and the sequence $2 \ 3 \ 4 \ 3$, the non-empty subarrays are: $2, 2 \ 3, 2 \ 3 \ 4, 2 \ 3 \ 4 \ 3, 3, 3 \ 4, 3 \ 4 \ 3, 4, 4 \ 3, 3$. We define the power of an element $a_i$ as the number of subarrays containing $a_i$ in which $a_i$ is strictly greater than the other elements in each of those subarrays. Thus, in the sequence $2 \ 3 \ 4 \ 3$, the power of element $a_1$ is $1$ (being the maximum only in the subarray formed by itself), the power of element $a_2$ is $2$ ($a_2$ being the maximum in the subarrays $2 \ 3$ and $3$), the power of element $a_3$ is $6$ (being the maximum in the subarrays $2 \ 3 \ 4, 2 \ 3 \ 4 \ 3, 3 \ 4, 3 \ 4 \ 3, 4$ and $4 \ 3$), and the power of element $a_4$ is $1$.

# Task

Write a program that determines the highest power of an element in the given sequence, as well as the number of elements in the sequence that have the highest power.

# Input data

The file `maxp.in` contains on the first line the natural number $N$, and on the second line, in order, the natural numbers $a_1, a_2, \dots, a_N$ separated by a space.

# Output data

The file `maxp.out` will contain on the first line a natural number representing the highest power of an element in the given sequence and on the second line will contain a natural number representing the number of elements in the sequence that have the highest power.

# Constraints and clarifications

* $2 \leq N \leq 200\ 000$;
* The elements of the sequence are natural numbers and have at most $6$ digits.
* 50% of the points are awarded for the correct determination of the highest power of an element in the sequence and 50% of the points for determining the number of elements in the sequence that have the highest power.

# Example 1

`maxp.in`
```
7
9 3 4 5 1 2 2
```

`maxp.out`
```
12
1
```

## Explanation

The element $5$ at position $4$ is the maximum in $12$ subarrays:

$3 \ 4 \ 5, 3 \ 4 \ 5 \ 1, 3 \ 4 \ 5 \ 1 \ 2, 3 \ 4 \ 5 \ 1 \ 2 \ 2, 4 \ 5, 4 \ 5 \ 1, 4 \ 5 \ 1 \ 2, 4 \ 5 \ 1 \ 2 \ 2, 5, 5 \ 1, 5 \ 1 \ 2, 5 \ 1 \ 2 \ 2$, so its power is $12$. It is the only element that has this power, the other elements having smaller powers.

# Example 2

`maxp.in`
```
6
1 0 7 7 2 6
```

`maxp.out`
```
3
2
```

## Explanation

The elements at positions $3$ and $4$ are the maxima in $3$ subarrays, so their power is $3$. The other elements have smaller powers.
```