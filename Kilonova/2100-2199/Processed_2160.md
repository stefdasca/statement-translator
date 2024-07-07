# Task

Given $a$ and $b$, Ionut wants to calculate $gcd(a,b)$. For this, he will use the following algorithm:

```
While a and b are both not 0:
    if a \geq b:
        a-=b // perform one operation
    else:
        b-=a // perform one operation
```

How many operations does the algorithm perform?

# Input data

The first line contains two integers, $a$ and $b$.

# Output data

The first line will contain the number of operations.

# Constraints and clarifications

* $1 \leq a, b \leq 10^{18}$

# Example 1

`stdin`
```
5 2
```

`stdout`
```
4
```

## Explanation

Numbers are:   
$(5,2)$ -> $(3,2)$ -> $(1,2)$ -> $(1,1)$ -> $(0,1)$  
A total of 4 operations.

# Example 2

`stdin`
```
1234 645933214
```

`stdout`
```
523464
