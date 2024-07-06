Ana and Mihai are two siblings passionate about mathematics. Ana likes numbers with all even digits, while Mihai likes numbers with all odd digits. The two children play with nine cubes, each cube having a digit written on it: $\{0, 1, 2, 3, 4, 5, 6, 7, 8\}$. From the nine cubes, Ana and Mihai each choose three cubes to form a number $N$ with exactly three digits. Then, the two look at each digit in order (hundreds, tens, units) and if the digit is even, Ana writes it as it is and Mihai writes the next odd digit, but if the digit is odd, Ana writes the next even digit and Mihai writes it as it is, each child thus forming a number with exactly three digits.

# Task

Write a program that reads from the keyboard the natural number $N$ with exactly $3$ distinct digits and determines:
1. The largest of the two numbers obtained by Ana and Mihai;
2. The difference between the largest and the smallest number among the two numbers obtained by Ana and Mihai.

# Input data

From the file `numere.in` read: the natural number $N$ formed by exactly $3$ distinct digits and a number $C$ representing the task number ($C$ can be $1$ or $2$).

# Output data

If $C$ is equal to $1$, the file `numere.out` will contain on the first line the largest of the two numbers obtained by Ana and Mihai.
If $C$ is equal to $2$, the file `numere.out` will contain on the first line the difference between the largest and the smallest number among the two numbers obtained by Ana and Mihai.

# Example 1

`numere.in`
```
725 1
```

`numere.out`
```
826
```

# Example 2

`numere.in`
```
725 2
```

`numere.out`
```
91
```

## Explanation

The hundreds digit is $7$, so Ana writes $8$ and Mihai writes $7$. The tens digit is $2$, so Ana writes $2$ and Mihai writes $3$. The units digit is $5$, so Ana writes $6$ and Mihai writes $5$. Therefore, Ana obtains the number $826$ and Mihai obtains the number $735$. Among them, $826$ is $91$ more than $735$.