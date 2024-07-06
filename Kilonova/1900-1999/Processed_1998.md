Miruna has encountered a new challenge: in the citadel of Deva, she found $N$ knolls arranged in a line, each knoll having a certain height expressed in centimeters. The height of a knoll can be increased by $1$ centimeter, but this operation costs her exactly $1$ leu. The increase operation can be applied to the same knoll multiple times. With a budget of $B$ lei available, Miruna wonders how many subarrays of the knoll series can be transformed in such a way that they become monotonically increasing.

# Input data

The first line of the file `calancea.in` will contain the numbers $N$ and $B$, as described in the statement. The next $N$ lines will contain a series of length $N$ values representing the heights of the knolls.

# Output data

The file `calancea.out` will contain a single integer representing the number of subarrays that can be transformed into monotonically increasing sequences with the budget $B$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq B \leq 10^{15}$
* The initial heights of the knolls will be in the range $[0, 10^{9}]$

# Example

`calancea.in`
```
3 6
10 5 1
```

`calancea.out`
```
5
```

## Explanation

With the exception of the subarray $(1, 3)$, all subarrays satisfy the required property.
