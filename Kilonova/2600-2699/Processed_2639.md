Here is the translated competitive programming problem statement:

---

Given $N$ natural numbers that contain in their representation only digits from the set $\{0, 1, 2, 3, 4\}$. Further, a **special number** is defined as a natural number in which there is at least one odd digit and each odd digit appears an even number of times.

# Task

1. Calculate the number of elements in the given array that are **special numbers**.
2. Calculate the number of subarrays in the given array that have a length at most equal to $K$ and contain exactly one element that is a **special number**.
3. Determine and display for each subarray of length $K$ the minimum number of elements that should be removed so that concatenating the remaining elements results in a **special number**, and if it is not possible to obtain a special number from the subarray, display $-1$.

# Input data

In the file `p13.in`, the first line contains, separated by a space, $C$, $N$, and $K$, where $C$ represents the task to be solved, $N$ the number of values to be read, and $K$ the required length for tasks $2$ and $3$. The second line contains the $N$ numbers, separated by a space.

# Output data

In the file `p13.out`, the first line will contain the value obtained for tasks $1$ and $2$, and for task $3$, the values obtained separated by a space.

# Constraints and clarifications

* $1 \leq C \leq 3$
* $1 \leq K \leq N \leq 100\ 000$
* Each number in the array is a natural number with at most $6$ digits.

|#|Score|Constraints|
|-|-|--------|
|1|21|$C = 1$|
|2|40|$C = 2$|
|3|39|$C = 3$|

# Example 1

`p13.in`
```
1 4 3
121 423 43 3003
```

`p13.out`
```
2
```

## Explanation

The special numbers are $121$ and $3003$.

# Example 2

`p13.in`
```
2 4 3
121 423 43 3003
```

`p13.out`
```
6
```

## Explanation

The subarrays of length at most $3$ which contain exactly one special number are: $121$, $121\ 423$, $121\ 423\ 43$, $3003$, $43\ 3003$, $423\ 43\ 3003$.

# Example 3

`p13.in`
```
3 4 3
121 423 43 3003
```

`p13.out`
```
0 0
```

## Explanation

By concatenation, both subarrays of length $3$ become special numbers $12142343$ and $423433003$.

---

Please let me know if there are any further clarifications needed.