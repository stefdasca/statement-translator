Macarie received the following problem statement as a homework for Informatics: *"Consider an array $A$ with $N$ non-zero natural numbers, numbered starting from $1$ to $N$. We define a **subarray** as a sequence of terms positioned on **consecutive positions** within the array, and the **length of a subarray** is the number of terms that it is made up of. The **cost of a subarray** is equal to the product of the sum of prime values in the subarray and the sum of composite values. A composite number is a number that has at least one natural divisor different from $1$ and itself, while a number is prime if it has exactly two distinct natural divisors, $1$ and itself."*

We know that the number $1$ is neither prime nor composite, so it does not influence the cost of any subarray it is part of. Obviously, the cost of a subarray that contains no prime number or a subarray that contains no composite number is equal to $0$. Also, the sum of prime values in a subarray that contains a single prime number $X$ is equal to $X$; similarly, the sum of composite values in a subarray that contains a single composite number $Y$ is equal to $Y$.

# Task

Help Macarie solve the following two tasks:

1. Determine the maximum length of a subarray in array $A$ for which its cost is less than or equal to a non-zero natural number $K$.
2. Assume each **composite** number in array $A$ is replaced by the product of its **smallest** prime factor and **largest** prime factor. Determine the subarray of maximal length in the newly obtained array, for which the greatest common divisor of the numbers it is made up of is different from $1$. Display the positions of the first and last element of the subarray. If there are multiple such subarrays of maximal length, display the one for which the position of its first element is the greatest.

# Input data

The first line of the input file `tema.in` contains three non-zero natural numbers $C$, $N$, and $K$, in this order, separated by a space, where $C$ is the number of the task that needs to be solved (1 or 2), while $N$ and $K$ have the meanings described in the statement. The second line contains $N$ non-zero natural numbers, separated by a space, representing in order, the terms of array $A$.

# Output data

On the first line of the output file `tema.out`:
1. write a non-zero natural number representing the maximum length determined for the first task, if $C=1$;
2. write two non-zero natural numbers, separated by a space, representing, in order, the positions of the first and last element of the subarray of maximal length, determined according to the second task, if $C = 2$.

# Constraints and clarifications

* $2 \leq N \leq 100 \ 000$;
* $1 \leq K \leq 10^{18}$; **The number $K$ does not have any role for task $2$**;
* $1 \leq A_i \leq 1 \ 000 \ 000$, for each $i$: $1 \leq i \leq N$;
* **In both tasks, there is a solution subarray that has a length at least equal to $2$**;
* There is at least one element different from $1$ in array $A$.
* For 10 points, $C = 1$ and $N = 2$;
* For 25 points, $C = 1$ and $N \leq 4 \ 000$;
* For 15 points, $C = 1$ and $5 \ 000 < N$;
* For 10 points, $C = 2$ and $N = 2$;
* For 25 points, $C = 2$ and $N \leq 4 \ 000$;
* For 15 points, $C = 2$ and $5 \ 000 < N$.

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

$C=1$, $N=10$ and $K=45$. The subarray $(2, 3, 1, 4, 5)=(A_2, A_3, A_4, A_5, A_6)$ has a cost equal to $(2 + 3 + 5) \times 4 = 40$. There is no subarray in $A$ with a longer length and a cost less than or equal to $45$.

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

$C=2$, $N=10$ and $K=20$. After modifications, array $A$ becomes: $(1,2,4,4,14,49,7,21,1,21)$. There are two subarrays of maximal length for which the greatest common divisor (gcd) of the numbers they are made up of is different from $1$: $(2,4,4,14)$ (the position of the first element in the array is $2$, and the gcd of its elements is $2$), respectively $(14, 49, 7, 21)$ (the position of the first element in the array is $5$, and the gcd of its elements is $7$). Since there are two subarrays of maximal length, the statement specifies that the one for which the position of its first element is maximal will be chosen, meaning, in this case, $(14,49,7,21)=(A_5, A_6, A_7, A_8)$.