The given text translated into English according to the specified instructions:

Se dă $n$ și un șir de $n$ numere naturale.

# Task
Determine:
1. The largest two prime numbers in the given array;
2. The smallest number in the array with the maximum number of divisors;
3. The number of ways to form pairs of two numbers in the array that have the same number of divisors.

# Input data

The first line of the file `perechi.in` contains two natural numbers $C$ - representing the task that needs to be solved ($1$, $2$ or $3$) and $n$ - representing the number of numbers in the array. The second line contains the $n$ numbers representing the elements of the array separated by a space.

# Output data

The first line of the file `perechi.out` will contain:
- the largest two prime numbers, separated by a space, in descending order, if the task is $1$;
- the smallest number in the array with the maximum number of divisors, if the task is $2$;
- the number of pairs of values in the array that have the same number of divisors, if the task is $3$.

# Constraints and clarifications
- $2 \\leq n \\leq 10^5$;
- $1 \\leq \\text{nr} \\leq 10^9$;
- There are at least two prime numbers in the array;
- For correctly solving task $1$ you get $20$ points;
- For correctly solving task $2$ you get $30$ points;
- For correctly solving task $3$ you get $50$ points.

# Example 1

`perechi.in`
```
1 6
7 25 13 49 17 4 
```

`perechi.out`
```
17 13
```

## Explanation

In the file there are $3$ prime numbers: $7$, $13$, $17$.
The largest two are $17$ and $13$.

# Example 2

`perechi.in`
```
2 6
7 25 13 49 17 4 
```

`perechi.out`
```
4
```

## Explanation

* $7$, $13$ and $17$ each have $2$ divisors;
* $4$, $25$ and $49$ each have $3$ divisors.

# Example 3

`perechi.in`
```
3 6
7 25 13 49 17 4 
```

`perechi.out`
```
6
```

## Explanation
The pairs $(7,13)$, $(7,17)$, $(25,49)$, $(25,4)$, $(13,17)$, $(49,4)$ can be formed.