Ștefan turned 15 years old. Being a passionate member of the Robotics Club, his family gave him many robots for his birthday, each equipped with a weapon of a certain power. He placed all the robots around him on the circumference of an imaginary circle, in a clockwise direction. These intelligent devices can communicate with each other, joining the powers of their weapons.

# Task
Knowing the number of robots and the power of each one, write a program that determines:
1. The size of the longest subarray of robots for which their weapon powers form a strictly increasing sequence.
2. An arrangement of the robots on the circle such that the sum of the products of each two neighboring powers is maximized. If there are multiple ways of arranging them such that the same maximum sum is obtained, the lexicographically smallest arrangement should be determined.

# Input data
The first line of the input file `roboti.in` contains a natural number $v$ whose value can only be $1$ or $2$.
The second line of the input file contains a single natural number $n$ representing the number of robots.
The third line of the input file contains $n$ natural numbers $p_1$, $p_2$, $\\dots$, $p_n$, separated by spaces, where $p_i$ represents the power of the $i$-th robot's weapon.

# Output data
If the value of $v$ is $1$, then the output file `roboti.out` will contain on the first line a single natural number representing the size of the longest subarray of robots for which the powers of their weapons form a strictly increasing sequence.
If the value of $v$ is $2$, then the output file will contain on the first line $n$ natural numbers separated by spaces, representing the powers of the $n$ robots arranged on the circle such that the sum of the products of each two neighboring powers is maximized, and the arrangement is lexicographically smallest.

# Constraints and clarifications
- $2 \\leq n \\leq 100\\ 000$
- For task 1, the longest subarray is chosen on the circle in a clockwise direction.
- If we have two sequences of numbers $[a_1, a_2, \\dots, a_n]$ and $[b_1, b_2, \\dots, b_n]$ and there exists $1 \\leq k \\leq n$ such that the smallest position for which $a_1 = b_1$, $a_2 = b_2$, $\\dots$, $a_{k-1} = b_{k-1}$ and $a_k < b_k$, then we say that the sequence $a$ is lexicographically smaller than sequence $b$.
- For correctly solving task 1, 30 points are awarded, for correctly solving task 2, 60 points are awarded, and 10 points are awarded automatically.
- For task 2, if the displayed solution is not lexicographically smallest but produces the correct maximum sum, $50\\%$ of the test points will be awarded.
- For task 2, tests worth a total of 36 points will have $n \\leq 1\\ 000$.
- $1 \\leq p_1, p_2, \\dots, p_n \\leq 1\\ 000$

# Example 1
`roboti.in`
```
1
7
4 7 2 6 5 1 3
```
`roboti.out`
```
4
```
## Explanation
$v = 1$, so **ONLY** the first task will be solved. $p = [\textcolor{red}{4}, \textcolor{red}{7}, 2, 6, 5, \textcolor{red}{1}, \textcolor{red}{3}]$.

The longest strictly increasing subarray is $[1, 3, 4, 7]$ and its length is $4$.

# Example 2
`roboti.in`
```
2
5
3 9 1 12 5
```
`roboti.out`
```
1 3 9 12 5
```
## Explanation
$v = 2$, so **ONLY** the second task will be solved.

$1 \\cdot 3 + 3 \\cdot 9 + 9 \\cdot 12 + 12 \\cdot 5 + 5 \\cdot 1 = 203$, and this is the maximum sum that can be obtained.

This arrangement is not the only one for which the maximum sum is obtained, but it is the lexicographically smallest.

# Example 3
`roboti.in`
```
2
4
1 2 1 1
```
`roboti.out`
```
1 1 1 2
```
## Explanation
$v = 2$, so **ONLY** the second task will be solved.

$1 \\cdot 1 + 1 \\cdot 1 + 1 \\cdot 2 + 2 \\cdot 1 = 6$, and this is the maximum sum that can be obtained.

This arrangement is not the only one for which the maximum sum is obtained, but it is the lexicographically smallest.