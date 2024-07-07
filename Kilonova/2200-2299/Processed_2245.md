
# Task

Given a number $x$ with $n$ digits. While thinking about various problems for the Runtime Terror Competition, the committee found the following _basic_ mathematical definitions:

A number $x$ is a **perfect square** if there exists a number $y$ such that $y^2 = x$. A number $y$ is a **prime number** if its only divisors are $1$ and $y$.

Similarly, a square digit is a digit that is a perfect square and a prime digit is a digit that is a prime number.

Now, you need to determine whether your number has more square digits, more prime digits, or if there is an equality.

# Input data

The first line will contain $n$, the number of digits of the number. The next line will contain the number, represented as a string of length $n$. The number will have digits from $0$ to $9$ and will not contain zeros at the beginning of the number.

# Output data

Print `Square` if $x$ has more square digits than prime digits, `Prime` if $x$ has more prime digits than square digits, or `Equal` if there is equality.

# Constraints and clarifications

* $1 \leq n \leq 100$;

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|30|$1 \leq n \leq 9$|
|2|30|$1 \leq n \leq 19$|
|3|40|No additional constraints|

# Example

`stdin`
```
6
402497
```

`stdout`
```
Square
```

## Explanation

The given number, $402497$ has $4$ square digits ($4$, $0$, $4$ and $9$) and $2$ prime digits ($2$ and $7$).
