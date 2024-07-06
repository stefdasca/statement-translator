On a plank, there are $N$ nails of different heights, measured in centimeters, and aligned. With each "hammer strike" on a nail, it penetrates the plank by $1$ cm. The carpenter wants to obtain the longest sequence of nails of the same height, after applying **at most** $M$ "hammer strikes".

# Task

Determine the maximum length - $L$ of a sequence of nails of the same height given the conditions, and the minimum number of "hammer strikes" - $K$ necessary to achieve it.

# Input data

The input file `cuie.in` contains on the first line two non-zero natural numbers $N$ and $M$, and on the next line $N$ non-zero natural values that represent the heights of the $N$ nails measured in cm.

# Output data

The output file `cuie.out` will contain on the first line, two non-zero natural numbers $L$ and $K$, separated by a space, representing: $L$ - the maximum length of a sequence of nails with the same height, respectively $K$ - the minimum number of "hammer strikes" needed to obtain the maximum sequence.

# Constraints and clarifications

* $1 \leq N \leq 500\ 000$
* $1 \leq M \leq 500\ 000$
* $1 \leq K \leq M$
* $1 \leq$ nail height $\leq 100\ 000$ cm
* The height of a nail represents the length of the part outside the plank.

# Example

`cuie.in`
```
8 5
3 2 4 3 3 5 3 1
```

`cuie.out`
```
5 3
```

## Explanation

The maximum length sequence is obtained after $3$ "hammer strikes", performed on nails $3$ and $6$. $3\ 2\ 3\ 3\ 3\ 3\ 3\ 1$.