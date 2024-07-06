```markdown
# Task

Andrei has an array of $n$ elements, as well as a number $k$. 

He wants to find out if there are two numbers $a$ and $b$ at **distinct** positions in the array such that their sum is $k$. 

# Input data

The first line will contain a number $n$, and another number $k$.  

The second line will contain $n$ numbers, representing the $n$ values.

# Output data

If such numbers exist, print the message `Da`. Otherwise, print the message `Nu`.

# Constraints and clarifications

* $1 \leq n \leq 10^3$
* $1 \leq k \leq 10^9$
* $1 \leq v_i \leq k$

# Example 1

`stdin`
```
4 6
1 1 3 5
```

`stdout`
```
Da
```

## Explanation

For the first example, $1$ + $5$ = $6$, so we have a solution. 

# Example 2

`stdin`
```
4 9
4 8 3 7
```

`stdout`
```
Nu
```

## Explanation

For the second example, no matter how we take two numbers from distinct positions, we will not be able to obtain the desired number.
```
