```markdown
Daniel opened a "kindergarten" and he is taking care of $N$ puppies of different ages that he has trained to stand in a circle. The puppies are numbered from $1$ to $N$ and for each puppy $i$ with values between $1$ and $N$ we know its age $V_i$. Each puppy $i$ has as neighbors puppies $i - 1$ and $i + 1$. Since they stand in a circle, the puppies in positions $1$ and $N$ are also neighbors.

Daniel needs to keep the puppies concentrated for a few hours and decides to play a game with them. For the game chosen by Daniel, he needs to divide the puppies into teams of $K$ puppies placed in consecutive order in the circle. Since the puppies have different ages, he wants to choose a $K$ such that the teams are as balanced as possible. To evaluate how balanced the division into teams of $K$ is, he calculates a balance coefficient as follows:
* Choose all subarrays of $K$ consecutive puppies
* Choose the minimum of each subarray
* Choose the maximum of these minimums, the balance coefficient

He would like the respective coefficient to be as large as possible, but remain strictly less than a given value $S$.

Help Daniel find the number $K$ for which the largest balance coefficient strictly less than $S$ is obtained. If there are multiple values of $K$ for which the ideal result is obtained, the largest among them will be displayed.

# Task

Given $N$, $S$, and the ages of the puppies, find the largest number $K$ for which the ideal balance coefficient is obtained.

# Input data

The first line contains two natural numbers $N$ and $S$, separated by a space, with the meaning from the statement. The second line of the input file contains $N$ natural numbers separated by spaces, $V_1, V_2, \dots, V_N$, representing the ages of the puppies in the order in which they are placed in the circle.

# Output data

Print a single natural number, $K$, the required result.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq K \leq N$
* $0 \leq S, V_i \leq 1 \ 000 \ 000 \ 000$
* It is guaranteed that there is at least one puppy with an age less than $S$.
| # | Points | Constraints |
| - | ------- | ----------- |
| 1 | 26 | $1 \leq N \leq 1 \ 000$ |
| 2 | 31 | $1 \leq N \leq 100 \ 000$ |
| 3 | 43 | Without additional constraints |

# Example 1

`stdin`
```
5 3
1 2 3 4 5
```

`stdout`
```
4
```

## Explanation

~[catelusi1.png|width=30em]

Let's take all subarrays of puppies of length $4$:
$1 \ 2 \ 3 \ 4 \rightarrow$ the minimum is $1$
$2 \ 3 \ 4 \ 5 \rightarrow$ the minimum is $2$
$3 \ 4 \ 5 \ 1 \rightarrow$ the minimum is $1$
$4 \ 5 \ 1 \ 2 \rightarrow$ the minimum is $1$
$5 \ 1 \ 2 \ 3 \rightarrow$ the minimum is $1$
The maximum value of a minimum is $2$ which is strictly less than $3$.

# Example 2

`stdin`
```
4 3
2 4 2 4
```

`stdout`
```
4
```

## Explanation

~[catelusi2.png|width=30em]

Let's take all subarrays of puppies of length $4$:
$2 \ 4 \ 2 \ 4 \rightarrow$ the minimum is $2$
$4 \ 2 \ 4 \ 2 \rightarrow$ the minimum is $2$
$2 \ 4 \ 2 \ 4 \rightarrow$ the minimum is $2$
$4 \ 2 \ 4 \ 2 \rightarrow$ the minimum is $2$
The maximum is $2$ which is strictly less than $3$.
Let's take all subarrays of length $3$:
$2 \ 4 \ 2 \rightarrow$ the minimum is $2$
$4 \ 2 \ 4 \rightarrow$ the minimum is $2$
$2 \ 4 \ 2 \rightarrow$ the minimum is $2$
$4 \ 2 \ 4 \rightarrow$ the minimum is $2$
The maximum is $2$ which is strictly less than $3$.
Let's take all subarrays of length $2$:
$2 \ 4 \rightarrow$ the minimum is $2$
$4 \ 2 \rightarrow$ the minimum is $2$
$2 \ 4 \rightarrow$ the minimum is $2$
$4 \ 2 \rightarrow$ the minimum is $2$
The maximum is $2$ which is strictly less than $3$.
We notice that we obtain the ideal value for $K$ equal to $2$, $3$, and $4$, but since in the case of equality we choose the largest $K$, the final answer is $4$.
```