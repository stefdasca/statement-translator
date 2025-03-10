
# Task

You are a monkey made up of ones and zeros, and like any monkey, your goal is a simple one: to reach a banana, of course, in your case, a virtual banana. The fruit is at the top of a virtual pole that has multiple virtual bars on its left or right. You, as a virtual monkey, have a maximum arm span of $K$, which means that the distance between two bars you will hold onto will be less than or equal to this $K$.

The bars on the left can only be grabbed with the left hand, and similarly for those on the right. **You cannot grab a bar on the right with your left hand or vice versa**. Each bar has a difficulty, and you, as a lazy virtual monkey, can skip some of them. However, you wonder what is the most difficult bar you must take to reach the virtual banana.

As everyone knows that virtual monkeys know how to code, write a program to calculate your answer.

You start with both hands at height $0$, holding the base of the virtual pole. If the top cannot be reached, $-1$ will be displayed. It is considered that you have reached the top if you can reach height $N+1$ with either hand. It can be considered that at heights $0$ and $N+1$, you have a bar of difficulty 0 that can be grabbed with both hands.

# Input data

The pole has a height $N$, and at each unit there is a bar on the left or on the right with difficulty $X$.
The first line will contain the variables $N$ and $K$ separated by a space, and on the following $N$ lines, the description of the bars in the form: $P$ (the character `S`, or `D`, representing left or right), $X$ (difficulty).

# Output data

The answer should be a single number $R$, which is the answer to the problem.

# Constraints and clarifications

* $1 \leq N, K \leq 10^6$
* $1 \leq X \leq 10^9$

|#| Score | Constraints                                    | 
|-|-------|------------------------------------------------|
|0|   0   | Examples                                       |
|1|   15  | $N \le 100$                                    |
|2|   19  | $N \le 1 \ 000$                                   |
|3|   66  | without additional constraints                 |

# Example

`stdin`
```
10 4
D 1
D 2
S 7
S 4
D 1
D 4
S 9
S 3
S 8
D 5
```

`stdout`
```
4
```

## Explanation
There are multiple possible solutions, but one possible order to grab the bars is: right hand at height $2$, left at $4$, right at $6$, left at $8$, and then with the right hand you can reach $N + 1$, so you can reach the banana. Therefore, the answer is $4$ because no route can be found in which the maximum bar is less than $4$.
