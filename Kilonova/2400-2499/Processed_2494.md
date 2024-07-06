Three friends, Anna, Bob, and Charlie, are playing ping-pong. Ping-pong is a game for two players, therefore when two of them play, the third one simply watches. After the game is over, the player who won remains at the table and plays together with the person who was watching. For example, if Anna defeats Bob, then she plays the next match with Charlie.

One day, their computer science teacher posed the following question to them: In how many ways can the three of them play ping-pong, such that Anna wins _exactly_ $a$ matches, Bob _exactly_ $b$ matches, and Charlie _exactly_ $c$ matches? Since this number can be very large, the teacher is satisfied with the answer modulo $10^9 + 7$.

We will explain when we consider two ways of playing different. For a way of playing $P$, let $Win(P)$ be the list of players who win each match and $Watch(P)$ the list of players who watch each match. Then, two ways of playing $P$ and $Q$ are considered different if there is a match $i$, such that $1 \leq i \leq a + b + c$ and $Win(P)_i \ne Win(Q)_i$ or $Watch(P)_i \ne Watch(Q)_i$.

This question seems quite difficult for them. Can you help?

# Implementation Details

You need to implement the following function:

```cpp
int solve(int a, int b, int c);
```

This function should return the answer for the given values of $a, b$ and $c$. The function will be called _only once_ for a run of the committee's grader.

You can use the following function in your solution implementation.

```cpp
int combinations (int n, int k);
```

This function will return in constant time ${N}\choose{K}$ mod $10^9 + 7$, i.e., the binomial coefficient that corresponds to $n, k,$ or the number of ways to choose $k$ objects from a pile of $n$ objects, all modulo $10^9 + 7$. Note that the parameters $n$ and $k$ must satisfy the condition $0 \leq k \leq n \leq 5 \ 000 \ 000$. 

**Do not forget to include the header `ping-pong.h!`**

# Grader Behavior

The grader will read three integers, $a, b$ and $c$ from the keyboard. Then it will call $solve(a, b, c)$, and will print the returned value to the screen. The input/output files below work for this grader.

# Constraints and Clarifications

* $0 \leq a, b, c \leq 1 \ 000 \ 000$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 9      | $a + b + c \leq 12$ |
| 2 | 4      | $a + b \leq 20, c = 0$      |
| 3 | 7      | $a \leq 1 \ 000, b \leq 1 \ 000, c = 0$      |
| 4 | 11      | $c = 0$      |
| 5 | 21      | $1 \leq a, b, c \leq 100$      |
| 6 | 22      | $1 \leq a, b, c \leq 1 \ 000$      |
| 7 | 26      | No additional constraints.      |

# Example 1

To compactly represent all different scenarios that can happen, we will use the following notation. If in a match player $x$ defeats player $y$, we will write $x \rightarrow y$. Anna is player $\\color{red}{a}$, Bob is player $\\color{cyan}{b}$ and Charlie is player $\\color{blue}{c}$. We will show a sequence of matches as a list of such statements: for example, if Anna defeats Bob, Charlie defeats Anna and then Bob defeats Charlie, we will write $a \rightarrow b, c \rightarrow a, b \rightarrow c$.

`input`
```
1 1 1
```

`output`
```
6
```

## Explanation

There are only $6$ possible scenarios:

1. $\\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
2. $\\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
3. $\\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}$
4. $\\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}$
5. $\\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}$
6. $\\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}$

# Example 2

`input`
```
2 2 2
```

`output`
```
24
```

## Explanation

1. $\\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
2. $\\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
3. $\\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
4. $\\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
5. $\\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
6. $\\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
7. $\\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
8. $\\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}$
9. $\\color{red}{a} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}$
10. $\\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}$
11. $\\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}$
12. $\\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}$
13. $\\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}$
14. $\\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
15. $\\color{blue}{c} \rightarrow \\color{red}{a}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}$
16. $\\color{blue}{c} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}$
17. $\\color{cyan}{b} \rightarrow \\color{blue}{c}, \\color{red}{a} \rightarrow \\color{cyan}{b}, \\color{red}{a} \rightarrow \\color{blue}{c}, \\color{cyan}{b} \rightarrow \\color{red}{a}, \\color{blue}{c} \rightarrow \\color{cyan}{b}, \\color{blue}{c} \rightarrow \\color{red}{a}$
18. $\\color{cyan}{b} \rightarrow \\color