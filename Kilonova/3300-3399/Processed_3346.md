
# Task

You are at a game show for ambitious computer scientists. After passing multiple difficult rounds, you have reached the final. Here, the host asks you the following question:

For a natural number $n$, using only the operations of adding $1$ and multiplying by $2$, what is the minimum number of steps required to go from the number $0$ to $n$?

Will you manage to win the grand prize (a state-of-the-art graphics card)?

# Input data

The program reads from the file `fast.in` the number $n$, a natural number.

# Output data

The program will write to the file `fast.out` the minimum number of steps taken to reach the number $n$.

# Constraints and clarifications

* $0 \leq n \leq 10^{12}$ ($10$ to the power of $12$).

# Example 1

`fast.in`
```
4
```

`fast.out`
```
3
```

## Explanation

To obtain the number $4$, starting from $0$, we add $1$ to reach $1$, then multiply by $2$ to reach $2$, and multiply by $2$ again to reach $4$.

# Example 2

`fast.in`
```
7
```

`fast.out`
```
5
```

# Example 3

`fast.in`
```
13
```

`fast.out`
```
6
```
