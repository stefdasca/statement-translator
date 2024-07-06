Gigel is a passionate hiker. He especially enjoys mountain hiking. At the end of this week, he plans to traverse a mountain near the city of Cluj. However, the local mountain rescue team has imposed some conditions:

* The length of the path must be exactly $2 \cdot n - 2$ meters, with the value $n$ given by the mountain rescuers;
* He must start from the foot of the mountain and must reach the foot of the mountain on the other side at the same altitude;
* He is not allowed to descend below the starting altitude;
* He can traverse the path using only three types of steps:
    * Horizontal step of length $2$, i.e., of type $(2, 0)$
    * "Up" step of length $1$, i.e., of type $(1, 1)$
    * "Down" step of length $1$, i.e., of type $(1, -1)$
* His path is not allowed to have a "peak" at altitude $1$, that is, he is not allowed, while at the starting altitude during his path, to take an up step immediately followed by a down step.

# Task

Given the value $n$, determine in how many ways Gigel can traverse the mountain while respecting the conditions imposed by the mountain rescue team.

# Input data

The input file `munte.in` contains a single line which contains the natural number $n$.

# Output data

The output file `munte.out` will contain a single line which will contain the number of ways in which Gigel can traverse the mountain.

# Constraints and clarifications

* $1 \leq n \leq 100$
* For $60 \%$ of the tests, the result is a $64$-bit integer.

# Example 1

`munte.in`
```
1
```

`munte.out`
```
1
```

## Explanation

Since the length of the path is $2 \cdot 1 - 2 = 0$, there is only one way to traverse the mountain (by staying in place).

# Example 2

`munte.in`
```
2
```

`munte.out`
```
1
```

## Explanation

Since the length of the path is $2 \cdot 2 - 2 = 2$, there is only one way to traverse the mountain, through a step of length $2$.

~[munte1.png]

The version on the right is not correct because it does not comply with the last condition.

# Example 3

`munte.in`
```
3
```

`munte.out`
```
3
```

## Explanation

The $3$ correct ways to traverse the mountain with a path length of $4$ are:

~[munte2.png]

Any other way of traversing the mountain with a path length of $4$ is incorrect.