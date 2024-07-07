
A number is prime if it has exactly two natural divisors. By dividing a number into $p$ parts, we understand the division of the number into $p$ numbers, each with at least one digit, so that by concatenating the numbers from left to right we obtain the initial number.

For example, if we divide the number $12045$ into two parts, we have four possible divisions resulting in the numbers: $1$ and $2045$; $12$ and $045$; $120$ and $45$; $1204$ and $5$. If we divide it into three parts, we have six possible divisions resulting in the numbers $1$, $2$, and $045$; $1$, $20$, and $45$; $1$, $204$, and $5$; $12$, $0$, and $45$; $12$, $04$, and $5$; $120$, $4$, and $5$.

# Task

Consider an array of $N$ natural numbers.

1. Determine the largest prime number in the array of $N$ numbers.
2. Determine the largest prime number among those obtained by dividing each number in the array of $N$ into two parts.
3. Determine the largest prime number among those obtained by dividing each number in the array of $N$ into three parts.

# Input data

The first line of the `tai.in` file contains the number $C$ which can only have the values $1$, $2$, or $3$ and represents the task to be solved. The second line contains $N$, as defined in the statement, and the third line contains the array of $N$ natural numbers separated by a space.

# Output data

The `tai.out` output file should contain a natural number on the first line representing the answer to the specified task.

# Constraints and clarifications

* $1 \leq N \leq 100$;
* $0 \leq$ any number in the array $\leq 10^9$;
* For tasks $2$ and $3$, it is guaranteed that for all numbers in the array the division can be performed.
* For task $1$, if the array does not contain any prime numbers, print $0$.
* For tasks $2$ and $3$, if no prime number is obtained after the divisions, print $0$.
* Solving each task yields $30$ points.

# Example 1

`tai.in`
```
1
5
2 13 21 17 1
```

`tai.out`
```
17
```

## Explanation

The prime numbers in the array are $2$, $13$, and $17$, and the maximum is $17$.

# Example 2

`tai.in`
```
2
3
23 196 27
```

`tai.out`
```
19
```

## Explanation

From $23$ we obtain the numbers $2$ and $3$, from $196$ we can obtain the numbers $1$ and $96$ or $19$ and $6$, and from $27$ we obtain the numbers $2$ and $7$. The largest prime number that can be obtained is $19$.

# Example 3

`tai.in`
```
3
3
1234 17119 5678
```

`tai.out`
```
71
```

## Explanation

From the number $1234$ we can obtain the numbers: $1$, $2$, $34$ or $1$, $23$, $4$ or $12$, $3$, $4$. From the number $17119$ we can obtain the numbers: $1$, $7$, and $119$ or $1$, $71$, and $19$ or $1$, $711$, and $9$ or $17$, $1$, and $19$ or $17$, $11$, and $9$. 

From the number $5678$ we can obtain the numbers: $5$, $6$, and $78$ or $5$, $67$, and $8$ or $56$, $7$, and $8$. The largest prime number that can be obtained is $71$.
