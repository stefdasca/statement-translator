Here's the translated problem statement in English:

---

We have an array $V$ consisting of $n$ nonzero digits as well as two natural numbers $L$ and $K$. We can perform the following operation: we choose $L$ elements that are next to each other in the array, then select $K$ of them to remove. The $L - K$ digits are placed next to each other forming a number whose value interests us (digits cannot change their relative order, i.e., they are placed in the increasing order of their indices in the original array).

We need to determine the value with the maximum number of occurrences that we obtain with this process. If there are multiple values that appear the maximum number of times, we will choose the smallest one. Two possibilities are considered distinct if they differ by the index in the given initial array of at least one of the digits of the same rank in the associated numbers.

# Input data

The input file `selectare.in` contains on the first line the values of $n, L, K$, in this order, separated by a space. The second line contains the $n$ digits, separated by a space.

# Output data

The output file `selectare.out` will contain on the first line the smallest value that has the maximum number of occurrences.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$
* $1 \leq L \leq 6$
* $L \leq n$
* $0 \leq K \leq 2$
* $K \leq L - 1$
* $1 \leq V_i \leq 9$

# Example 1

`selectare.in`
```
8 4 0
2 1 2 1 2 1 2 3
```

`selectare.out`
```
1212
```

## Explanation

We need to select sequences of $4$ digits and we do not need to remove anything. The numbers formed are: $2121$, $1212$, $2121$, $1212$, and $2123$. We have two values that can be formed and appear twice, and one value that can be formed once. The value $1212$ can be formed twice and is the smallest among those with this number of occurrences.

# Example 2

`selectare.in`
```
4 3 1
1 2 3 2
```

`selectare.out`
```
12
```

## Explanation

We need to select sequences of length $3$ from which we remove one digit, leaving numbers with two digits. These have values: $12, 23, 32, 13, 22$. All these values are formed once. Thus, we display the smallest value: $12$.

# Example 3

`selectare.in`
```
5 4 2
1 1 1 1 1
```

`selectare.out`
```
11
```

## Explanation

Obviously, the obtained value can only be $11$. It can be obtained $9$ times, with the digits at positions: $(1,2)(2,3)(3,4)(4,5)(1,3), (2,4)(3,5)(1,4)(2,5)$.

---

This translation maintains the structure, format, and mathematical details of the original problem statement while ensuring clarity and correctness in English.