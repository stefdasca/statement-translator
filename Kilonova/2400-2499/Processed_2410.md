Here's the translated and formatted problem statement:

---

The array $V$, **indexed from $0$**, is initially empty. The following types of operations are performed on it:

* `1 p val` — an element with the value $val$ is inserted at position $p$.
* `2 p val` — a black element with the value $val$ is inserted at position $p$.
* `3` — the sum of the elements between the position of the last red element inserted and the position of the last black element inserted is calculated.

It is guaranteed that all operations are valid: $p$ is less than or equal to the current length of the array, and an operation of type $3$ will only be performed after the array contains at least one red element and at least one black element.

# Task

Display the sum of all values calculated by operations of type $3$, modulo $666013$.

# Input data

The first line contains a natural number $Q$, representing the number of operations performed. The following $Q$ lines contain, in order, the operations performed. The first element on each line represents its type (`1`, `2`, or `3`). If the type of an operation is $1$ or $2$, that line also contains the values $p$ and $val$.

# Output data

Print the remainder when the sum of all values calculated by operations of type $3$ is divided by $666013$.

# Constraints and clarifications

* $1 \leq Q \leq 200\ 000$;
* $1 \leq val \leq 10^9$;
* The sums calculated within operations of type $3$ include the boundaries of the subarrays;
* For tests worth $36$ points, $1 \leq Q \leq 10\ 000$;
* For the remaining $64$ points, there are no additional constraints.

# Example

`stdin`
```
6
1 0 1
1 0 2
2 1 3
3
2 0 4
3
```

`stdout`
```
11
```

## Explanation

```
1 0 1   =>  V = [1]
1 0 2   =>  V = [2, 1]
2 1 3   =>  V = [2, 3, 1]
3       =>  S += 5
2 0 4   =>  V = [4, 2, 3, 1]
3       =>  S += 6
```

---

Please review and let me know if there are any further adjustments needed.