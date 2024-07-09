Given a number $N$, and a sequence of $N$ non-zero natural numbers.

# Task
1. Determine the sum of the values located in the last $K$ positions of the sequence (where $K$ represents the value of the rightmost non-zero digit of the first value in the sequence).
2. Imagine dividing the sequence into segments as follows: the first segment consists of the first $L$ elements, the second consists of the next $L - 1$ elements, the third consists of the next $L - 2$ elements, and so on, the last segment consists of a single element and this **coincides with the last element of the sequence**. Considering the sum of the values of each segment, determine the greatest among these sums.

# Input data

The first line of the `sss.in` file contains two values $C$ and $N$ separated by a space. The second line contains $N$ natural numbers separated by a space. For $C = 1$ only task $1$ needs to be solved, and for $C = 2$ only task $2$ needs to be solved.

# Output data

The file `sss.out` contains a single number representing the value calculated according to the task.

# Constraints and clarifications

* $1 \\leq n \\leq 100\ 000$;
* The values in the sequence are non-zero natural numbers $\\leq 100\ 000$;
* It is guaranteed that for tests with $C = 1$ the sequence has at least $K$ elements;
* It is guaranteed that the value of $N$ allows decomposition according to the description for tests with $C = 2$;
* For tests worth $51$ points we have $C = 1$;
* For $27$ points among the tests with $C = 1$, the first number in the sequence has a single digit;
* For tests worth $49$ points we have $C = 2$;
* For tests worth $22$ points among those with $C = 2$, the value of $N$ is less than or equal to $10$.
* The name of the problem is an abbreviation of "sums and sequences."

# Example 1

`sss.in`
```
1 6
120 4 21 5 31 6
```

`sss.out`
```
37
```

## Explanation

The last non-zero digit of the first element in the sequence is $2$. The sum of the last two values in the sequence is $37$.

# Example 2

`sss.in`
```
2 10
1 4 2 1 3 6 1 6 5 3
```

`sss.out`
```
11
```

## Explanation

The decomposition can be realized into segments of lengths $4$, $3$, $2$, and $1$. The sums obtained for each are: $8$, $10$, $11$, $3$.