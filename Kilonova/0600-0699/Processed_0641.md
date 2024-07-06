```markdown
King George VI of the United Kingdom faced an unusual problem for a person who had to give speeches: he stuttered. He stuttered even when he said numbers. Interestingly, when he said a number, he repeated only one of the digits of that number, immediately after pronouncing the respective digit.

For example, the number $70243$ could be pronounced when he stuttered as $770243$ or as $700243$ or as $702243$ or as $702443$ or as $702433$.

A ***palilindrome*** is a natural number for which there is a stutter of the king that transforms it into a palindrome.

For example, $25373552$ is a *palilindrome*, because after a stutter it can become $255373552$, which is a palindrome.

# Task
Given a non-zero natural number $X$, determine:
1) How many different numbers can $X$ generate after a stutter and how many different numbers can become $X$ after a stutter.
2) The largest *palilindrome* that can be formed with the digits of $X$. It is not mandatory to use all the digits of $X$.

# Input data
The first line of the input file contains the number $C$, which can be $1$ or $2$ and represents the task that needs to be solved.
The second line contains the number $N$, representing the number of digits of the number $X$.
The next line contains, in order, the digits of $X$, separated by a space.

# Output data
If $C = 1$, the output file will necessarily have two lines, each line containing exactly one number.

The first line will contain a natural number representing how many different numbers can $X$ generate after a stutter.
The second line will contain a natural number representing how many different numbers can become $X$ after a stutter.

If $C = 2$, the first line of the output file will contain the largest *palilindrome* that can be created with the digits of $X$.

# Constraints and clarifications
- $1 \leq N \leq 10^5$
- The number $X$ is a non-zero natural number with a maximum of $100\ 000$ digits.
- A palindrome is a number that has the same value if read from left to right or right to left.
- For the correct resolution of task 1, 40 points will be awarded. For each correctly displayed number, half of the points associated with the test will be awarded.
- For the correct resolution of task 2, 60 points will be awarded.

# Example 1
`balba.in`
```
1
8
7 0 2 2 4 3 3 3
```
`balba.out`
```
5
2
```

## Explanation

The different numbers that can be generated from $70224333$ through a stutter are: $770224333$, $700224333$, $702224333$, $702244333$, $702243333$.
The different numbers from which $70224333$ can be generated through a stutter are: $7024333$, $7022433$.

# Example 2

`balba.in`
```
1
25
1 2 3 1 2 3 4 1 2 3 4 5 1 2 3 4 5 6 1 2 3 4 5 6 7
```
`balba.out`
```
25
0
```

## Explanation

There are 25 different numbers that can be generated from $X$ through a stutter, but $X$ cannot be generated by any number through a stutter.

# Example 3

`balba.in`
```
2
11
2 4 7 8 1 4 8 7 4 2 1
```
`balba.out`
```
87442112478
```

## Explanation

There are also other *palilindromes* that can be formed with the digits of $24781487421$, but
$87442112478$ is the largest among them. The number $87442112478$ is a *palilindrome* because it can transform after a stutter into a palindrome, namely $874421124478$.

# Example 4

`balba.in`
```
2
7
1 2 3 4 0 0 0
```
`balba.out`
```
4
```

## Explanation

It is not possible to form a *palilindrome* that includes all the digits of $X$. Thus, the largest *palilindrome* that can be created using the digits of $X$ is $4$. The number $4$ is a *palilindrome* because it can transform after a stutter into a palindrome, namely $44$.
```