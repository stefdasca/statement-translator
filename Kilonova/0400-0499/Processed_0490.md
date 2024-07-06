```markdown
Mirko's great-grandmother, Katica, is passionate about mathematics. She likes to challenge Mirko with math games. This time, she wrote down a sequence of numbers on a piece of paper and told Mirko that he can do the following:

- He can choose any two numbers from the sequence (let's call them $A$ and $B$) and a prime number $X$, such that $A$ is divisible by $X$. Then, Mirko deletes $A$ and replaces it with $A/X$. After that, he deletes $B$ and puts $B * X$ in its place.

Mirko can perform this operation as many times as he wants. His goal is to achieve the highest possible score. The score for a sequence is the greatest common divisor of all the numbers in the array.  
   
**Note: Input data is read from the keyboard, and output data is printed to the console.**

# Task
1. Write a program that determines the score of the initial sequence, before Mirko performs any operations.
2. Write a program that calculates the highest possible score. Also, you need to print the minimum number of operations Mirko needs to perform to achieve the highest possible score.

# Input data
The first line of input contains a number $T$ which is either $1$ or $2$.  
The second line of input contains an integer $N$, the number of elements in the initial sequence.  
The third line of input contains $N$ natural numbers less than or equal to $10^6$, the sequence Katica gave to Mirko.

# Output data
- If $T$ is $1$, the only line of output must contain a single natural number, representing the initial score, before Mirko performs any operation.
- If $T$ is $2$, the only line of output must contain two natural numbers. The first number is the highest possible score Mirko can achieve. The second number represents the minimum number of operations Mirko needs to perform for the highest possible score.

# Constraints and clarifications
- $1 \le N \le 100$
- For tests worth 40 points, $T = 1$.
- For other tests worth 20 points, the values of the numbers are $\le 10\ 000$.
- For the remaining 40 points, there are no other restrictions.

# Example 1
`stdin`
```
1
3
9 6 12
```

`stdout`
```
3
```

# Example 2
`stdin`
```
2
3
4 4 1
```

`stdout`
```
2 1
```

# Example 3

`stdin`
```
2
3
8 24 9
```
`stdout`
```
12 3
```

# Example 4

`stdin`
```
2
5
4 5 6 7 8
```
`stdout`
```
2 2
```
```
```