Mirko was visited by aliens from planet X3, where everyone's age is a natural number. All inhabitants of the planet are good friends. Two X3-ians calculate the strength of their friendship by transforming their ages into the binary system, aligning them one below the other, and writing a digit in each column: 0 if the two binary digits in that column are equal, 1 if they differ. The resulting binary is then converted back into the decimal system. For example, the friendship value between an inhabitant aged 19 and one aged 10 is equal to 25.
~[Capture.PNG]

# Task

1. Determine how many inhabitants have an even number of digits equal to 1 when their ages are transformed into the binary system.
2. The value of a planet in the Universe is defined as the sum of all friendship values. Mirko asked for your help to calculate the value of planet X3!

**Note: Input data is read from the keyboard, and output data is displayed in the console.**

# Input data
The first line will contain a number $T$ equal to $1$ or $2$.
The second line will contain the natural number $N$ (the number of inhabitants of planet X3, $1 \leq N \leq 10^6$). 
The next $N$ lines will contain the ages of the residents - natural numbers less than $10^6$, one per line.

# Output data
- If $T = 1$, the single line of output must contain the number of inhabitants whose age has an even number of digits equal to 1 when transformed into the binary system.
- If $T = 2$, the single line of output must contain the value of planet X3.

# Constraints and clarifications
- For tests worth 20 points, $T = 1$.
- For other tests worth 25 points, $N \leq 5000$.
- For the remaining 55 points, there are no other constraints.

# Example 1
  `stdin`
  ```
 1
 2
19
10
  ```

  `stdout`
  ```
1
  ```

# Example 2

`stdin`
  ```
 1
 3
7
3
5
  ```

  `stdout`
  ```
2
  ```

# Example 3
  `stdin`
  ```
 2
 2
19
10
  ```

  `stdout`
  ```
25
  ```

# Example 4

`stdin`
  ```
 2
 3
7
3
5
  ```

  `stdout`
  ```
12
  ```

## Explanation
The strength of the friendship between inhabitant $1$ and $2$ is 4, the strength of the friendship between inhabitants $1$ and $3$ is 2, and the strength of the friendship between inhabitants $2$ and $3$ is 6.
$4 + 2 + 6 = 12$

# Example 5

`stdin`
  ```
2
5
9
13
1
9
6
  ```

  `stdout`
  ```
84
  ```