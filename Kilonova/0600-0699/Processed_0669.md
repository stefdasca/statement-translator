Given an array of length $n$ and a number $k$, we need to process $q$ queries of the following types:

$1 \\ a \\ b$: Change the value of the number at position $a$ to $b$

$2 \\ l \\ r \\ s$: Find how many arrays exist which can be formed with the numbers from positions $l$ to $r$, such that the value of each of the numbers is at least $k$ and the sum of the values is equal to $s$, if the only operation we can make is to increase values of the numbers from the array. Since the number of arrays can be really big, print the answer mod $10^9 + 7$

# Input

The first line will contain three integers, $n$, $q$ and $k$, which represent the length of the array, the number of queries we need to process and the minimal threshold for the value of each number with respect to the second type of query.

The second line of the input will contain the initial array $v$.

The next $q$ lines of the input will contain the description of the queries. 

# Output

The output will contain a line for each query of type $2$, with the answer for each query of type $2$.

# Constraints and clarifications

* $1 \leq n \leq 5 \cdot 10^4$
* $1 \leq q \leq 2 \cdot 10^5$
* $1 \leq k \leq 20$
* $1 \leq v[i], b \leq 100$
* $1 \leq a, l, r \leq n$
* $1 \leq s \leq 2 \cdot 10^6$
* For tests worth 20 points, $1 \leq n \leq 20$
* For tests worth 40 additional points, $1 \leq n \leq 2\ 000$, $1 \leq q \leq 5\ 000$

# Example

`stdin`
```
4 5 2
0 0 0 3
2 1 4 10
1 1 2
2 2 3 3
1 2 4
2 1 2 6
```

`stdout`
```
4
0
1
```

## Explanation

For the first query, the arrays we can get are [$2$, $2$, $3$, $3$], [$2$, $3$, $2$, $3$], [$3$, $2$, $2$, $3$], [$2$, $2$, $2$, $4$].