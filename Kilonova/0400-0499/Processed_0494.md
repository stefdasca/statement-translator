Luka has started driving his truck on international routes. His biggest problem is the Hungarian border. The border is an entry point into the Schengen area, so each truck is thoroughly examined. Because of this, Luka always has to wait a few hours there. To avoid getting bored, he tries to solve various logic and math puzzles.

One day, Luka reads $N$ numbers from the license plates in front of him and writes them down on a piece of paper.

**Note: Input data is read from the keyboard, and output data is displayed on the console.**

# Task
1. Luka wants to find out what is the greatest common divisor of the $N$ numbers.
2. Luka tries to find a natural number $M$ greater than $1$ such that all the natural numbers on the paper give the same remainder when divided by $M$. Luka tries to find as many such numbers $M$ as possible. Write a program that, given Luka’s $N$ integers, determines all possible numbers $M$.

# Input data
The first line of input will contain a number $T$ equal to $1$ or $2$.
The second line of input contains the integer $N$, the number of integers on the paper.
Each of the next $N$ lines of input contains a natural number between $1$ and $10^9$. All these integers will be distinct. The input data will guarantee that there always exists an $M$.

# Output data
- If $T = 1$, print a single natural number, representing the greatest common divisor of the $N$ numbers.
- If $T = 2$, print all the integers $M$, separated by spaces, **in ascending order**.

# Constraints and clarifications
- $2 \le N \le 100$
- For tests worth 20 points, $T = 1$.
- For other tests worth 40 points, all $N$ numbers will be $\le 10\,000$.

# Example 1
  `stdin`
  ```
1
3
6
36
39
  ```

  `stdout`
  ```
3
```
  
# Example 2

  `stdin`
  ```
1
5
5
17
23
14
83
  ```
  
  `stdout`
  ```
1
  ```
  
# Example 3
  `stdin`
  ```
2
3
6
34
38
  ```

  `stdout`
  ```
2 4
```
  
# Example 4

  `stdin`
  ```
2
5
5
17
23
14
83
  ```
  `stdout`
  ```
3
  ```
