Macarie received the following problem statement as a homework task for Informatics: *“Consider a sequence $A$ with $N$ non-zero natural numbers, numbered starting from $1$ to $N$. We call a **subarray** a sequence of terms that are positioned on **consecutive positions** in the array, and the **length of the subarray** represents the number of terms it consists of. The **cost of a subarray** is equal to the product of the sum of prime values in the subarray and the sum of composite values. A composite number is a number that has at least one natural divisor other than $1$ and itself, and a number is prime if it has exactly two distinct natural divisors: $1$ and itself.”*.

We know that the number $1$ is neither a prime number nor a composite number, so it does not affect the cost of any subarray it is part of. Obviously, the cost of a subarray that contains no prime number or a subarray that contains no composite number is equal to $0$. Also, the sum of prime values in a subarray containing a single prime number $X$ is equal to $X$; similarly, the sum of composite values in a subarray containing a single composite number $Y$ is equal to $Y$.

# Task

Help Macarie solve the following two tasks for his homework:
1. Determine the maximum length of a subarray in the array $A$ for which its cost is less than or equal to a non-zero natural number $K$.
2. Assume that each **composite** number in the array $A$ is replaced with the product of its **smallest** prime factor and its **largest** prime factor. Determine the maximum length subarray in the newly obtained array, for which the greatest common divisor of the numbers it consists of is different from $1$. The positions of the first and last elements in the subarray should be displayed. If there are multiple such subarrays of maximum length, the one with the highest position of its first element will be displayed.

# Input data

The first line of the input file `tema.in` contains three non-zero natural numbers $C$, $N$, and $K$, in this order, separated by a space, where $C$ is the number of the task to be solved (1 or 2), and $N$ and $K$ have the meaning from the statement. The second line contains $N$ non-zero natural numbers, separated by a space, representing, in order, the terms of the array $A$.

# Output data

The first line of the output file `tema.out`:
1. contains a non-zero natural number, representing the maximum length determined for the first task, if $C=1$;
2. contains two non-zero natural numbers, separated by a space, representing, in order, the positions of the first and last elements from the maximum length subarray, determined according to the second task, if $C = 2$.

# Constraints and clarifications
* $2 \leq N \leq 100 \ 000$;
* $1 \leq K \leq 10^{18}$; **The number $K$ has no role for task $2**;
* $1 \leq A_i \leq 1 \ 000 \ 000$, for each $i$: $1 \leq i \leq N$;
* **In both tasks, there exists a solution subarray that has a length of at least $2$**;
* There exists at least one element different from $1$ in the array $A$.
* For $10$ points, $C = 1$ and $N = 2$;
* For $25$ points, $C = 1$ and $N \leq 4 \ 000$;
* For $15$ points, $C = 1$ and $5 \ 000 < N$;
* For $10$ points, $C = 2$ and $N = 2$;
* For $25$ points, $C = 2$ and $N \leq 4 \ 000$;
* For $15$ points, $C = 2$ and $5 \ 000 < N$.

# Example 1

`tema.in`
```
1 10 45
10 2 3 1 4 5 8 2 6 3
```

`tema.out`
```
5
```

## Explanation

$C=1$, $N=10$ and $K=45$. The subarray $(2, 3, 1, 4, 5)=(A_2, A_3, A_4, A_5, A_6)$ has a cost equal to $(2 + 3 + 5) \times 4 = 40$. There is no subarray in $A$ with a larger length and a cost less than or equal to $45$.

# Example 2

`tema.in`
```
2 10 20
1 2 32 4 42 49 7 21 1 63
```

`tema.out`
```
5 8
```

## Explanation

$C=2$, $N=10$ and $K=20$. After modifications, the array $A$ becomes: $(1,2,4,4,14,49,7,21,1,21)$. There are two maximum length subarrays for which the greatest common divisor (gcd) of the numbers it consists of is different from $1$: $(2, 4, 4, 14)$ (the position of the first element is $2$, and the gcd of its elements is $2$), and $(14, 49, 7, 21)$ (the position of the first element is $5$, and the gcd of its elements is $7$). Since there are two maximum length subarrays, the one where the position of its first element is the highest is chosen, in this case, $(14,49,7,21)=(A_5, A_6, A_7, A_8)$.