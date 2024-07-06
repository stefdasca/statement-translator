```markdown
We define an **expression** as a string of characters $e$ which follows one of the following:
* $e =$ `x`;
* $e$ represents a natural number (constant); (e.g. $e \in \{$`1`$, `2`$, `200`, \dots$\})
* $e = [e_1, e_2]$ or $e = (e_1, e_2)$, where $e_1$ and $e_2$ are (sub-)expressions. Here, $(\cdot, \cdot)$ denotes the greatest common divisor of two numbers, and $[\cdot, \cdot]$ denotes the least common multiple of two numbers. For example, we have that $(6, 8) = 2$, $[6, 8] = 24$.

For example, `x`, `13`, `(5,2)`, `[3,[x,(14,1)]]`, `[x,x]` are expressions, while `0`, `(5, 2, 3)`, `[x, 2)` are not expressions. **Note that expressions never contain spaces.**

For a given expression $e$ and a positive natural number $a$, we define $eval(e, a)$ as the result of evaluating the expression $e$, where all occurrences of $x$ are replaced with the value $a$. For example:

$eval($`([x,3],[x,2])`$, 10) =$ `([10,3],[10,2])` $=$ `(30,10)` $=$ `10`

$eval($`(6,14)`$, 5) =$ `(6, 14)` $=$ `2`

$eval($`x`$, 12) =$ `12`

Given an **expression** $e$ and two natural numbers $a, b$, compute $eval(e, a) + eval(e, a + 1) + \ldots + eval(e, b)$.

**The result will be displayed modulo $10^9 + 7$.**

# Task

The input file `expresii.in` contains on the first line an expression $e$. The second line contains the numbers $a, b$, separated by a space.

# Input data

The output file `expresii.out` will contain a single integer representing the required value.

# Constraints and clarifications

* In the following table, $|e|$ represents the length of the expression $e$ (number of characters), and $\max(e)$ represents the highest constant value in $e$ (or $0$ if $e$ does not contain constants).

|#|Score|Constraints|
|-|-|--------|
|1|9|$1 \leq a \leq b \leq 1\,000$ and $e = (x, t)$, where $1 \leq t \leq 1\,000$|
|2|10|$1 \leq a \leq b \leq 1\,000$, $1 \leq \lvert e \rvert \leq 1\,000$, $0 \leq \max(e) \leq 1\,000$ and the expression $e$ does not contain square brackets `[]`|
|3|15|$1 \leq a \leq b \leq 40$, $1 \leq \lvert e \rvert \leq 1\,000$, $0 \leq \max(e) \leq 40$|
|4|17|$1 \leq a \leq b \leq 10^5 \quad 1 \leq \lvert e \rvert \leq 10^5 \quad 0 \leq \max(e) \leq 10^5$ and all constants in $e$ are powers of $2$|
|5|17|$1 \leq a \leq b \leq 1\,000 \quad 1 \leq \lvert e \rvert \leq 1\,000 \quad 0 \leq \max(e) \leq 1\,000$|
|6|10|$1 \leq \bm{a = b} \leq 100\,000 \quad 1 \leq \lvert e \rvert \leq 250\,000 \quad 0 \leq \max(e) \leq 100\,000$|
|7|14|$1 \leq a \leq b \leq 100\,000 \quad 1 \leq \lvert e \rvert \leq 250\,000 \quad 0 \leq \max(e) \leq 100\,000$|
|8|8|$1 \leq a \leq b \leq 250\,000 \quad 1 \leq \lvert e \rvert \leq 2\,000\,000 \quad 0 \leq \max(e) \leq 250\,000$|

# Example 1

`expresii.in`
```
(x,6)
4 4
```

`expresii.out`
```
2
```

## Explanation

For the first example, $(4, 6) = 2$.

# Example 2

`expresii.in`
```
[x,6]
1 6
```

`expresii.out`
```
66
```

## Explanation

For the second example, $[1, 6] + [2, 6] + [3, 6] + [4, 6] + [5, 6] + [6, 6] = 6 + 6 + 6 + 12 + 30 + 6 = 66$.

# Example 3

`expresii.in`
```
(12,(x,(8,6)))
3 6
```

`expresii.out`
```
6
```

# Example 4

`expresii.in`
```
([x,3],[x,2])
10 10
```

`expresii.out`
```
10
```

# Example 5

`expresii.in`
```
[([(x,5),2],[12,5]),(x,16)]
28 33
```

`expresii.out`
```
36
```

## Explanation

For the last example, the answers for each value in the interval are $4, 2, 10, 2, 16, 2$ (in this order).

**Note!** Examples $2$, $3$, $4$, and $5$ do not follow the constraints of subtask $1$. Examples $2$, $4$, and $5$ do not follow the constraints of subtask $2$. Examples $2$, $3$, and $5$ do not follow the constraints of subtask $6$.
```