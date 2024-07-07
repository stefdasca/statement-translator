
The Info(1)cup Kingdom hosts the largest cook-off in history. Two of the kingdom’s largest chefs, Lulu and Tanaka both want to prove that they are the best chef in the kingdom. However, the cooking contest is a bit strange: it involves breaking plates. Each contestant receives `n` plates of **distinct** sizes, where each has a certain value. Formally, you receive `n` plates, ordered from largest to smallest, and their values $v_1, \dots, v_n$. Now, each contestant stacks the plates in any order they want. When a plate is added to the stack, all plates that are **smaller** than it are broken and removed from the stack. The *score* of the current plate is calculated as $ \text{number\_of\_plates\_broken} \times v_i$, if the value of the plate is $v_i$. The total score of a contestant’s performance is the sum of the scores for each of the plates. 

After hearing about this task, Tanaka says to Lulu: “Beating you will be ez, Lulu�. Help Lulu beat Tanaka by finding the best possible order in which to put the plates on the stack.

# Task
The first line of the input contains `n`, the number of plates. The next line contains $v_1, \dots, v_n$.

# Input data
The first line of the input contains `n`, the number of plates. The next line contains $v_1, \dots, v_n$.

# Output data
The first line of the output contains a single integer which is the maximum score Lulu can make.

The second contains the order in which Lulu should insert the plates in order to achieve this score. For example, if the order is “add the third plate, then the first, then the second�, the output should contain `3 1 2`. If there are multiple orders you can print any one of them.

# Constraints and clarifications
* `1 \leq n \leq 200000`.
* $1 \leq v_i \leq 1\ 000\ 000\ 000$.
* If only the maximum score is correct, then only `50%` of the points for the test are awarded.

## Subtask 1 (12 points)
* $v_i = i$

## Subtask 2 (13 points)
* $v_i = n + 1 - i$

## Subtask 3 (22 points)
* `1 \leq n \leq 9`

## Subtask 4 (53 points)
* No further restrictions.

# Examples

`stdin`

```
3
1 2 3
```

`stdout`

```
3
3 2 1
```
Explanation
---

Firstly, we put the third plate on the stack. The second plate breaks the third one, with a score of `1 \cdot 2 = 2`. The first one then breaks the second one, with a score of `1 \cdot 1 = 1`.

`stdin`

```
3
3 2 1
```

`stdout`

```
6
2 3 1
```
Explanation
---

Firstly, we put the second plate on the stack. Then we put the third plate which doesn't break anything. Then the first one will break the first two with a score of `2 \cdot 3 = 6`.

`stdin`

```
10
2 2 1 24 13 15 20 10 29 29
```

`stdout`

```
155
3 5 6 7 8 10 9 4 2 1
```
Explanation
---

The explanation for this example is truly remarkable, but this margin is too small to contain it.
