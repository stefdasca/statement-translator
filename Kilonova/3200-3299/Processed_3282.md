> Big money is made easily, small money is made with difficulty.
> --- 'Claus

Vasile is the friend of **Lina**. Recently, Vasile created a _Pinance_ account to spend more time investing in cryptocurrencies than in church. His surprise came one day when, for no apparent reason, he noticed that his investments were fruitful. Surprised by this event, he decided to analyze the events that took place in the _Plockchain_ that brought him to these heights. Vasile explained to us that we can imagine the _Plockchain_ works as follows:

Initially, there are $N$ transaction requests in the system, indexed from $1$ to $N$, the $i$-th having a commission of $W_i$ and a unique other request on which it directly depends $P_i$. It is said that the request with index $1$ was primordial to the system and has no dependencies. Vasile observed the movements within the _Plockchain_ and classified them into three types:

1. A new request with an initial commission $C$ appears, whose direct dependency is $T$. The index of this request will be $N + t + 1$, where $t$ is the number of requests previously added through this process. Thus, the first added request has index $N + 1$. 
2. The commission of a request with index $a$ is modified from $W_a$ to $C$.
3. The request with index $a$ is completely removed from the register. It is guaranteed that no other request $j$ exists such that $P_j = a$ (no request depended on $a$).

**Lina**, amazed by Vasile's explanations, began to often ask the following question during these changes:

> Considering all the requests that currently exist in the system, what commission would a hacker be rewarded with if they executed all requests that are at **most** $H$ dependencies down from a request $X$?

We say a request $A$ is at most $x$ dependencies down from $B$ if and only if $x \ge 0$ and $A = B$, or $x \ge 1$ and $P_A$ is at most $x - 1$ dependencies down from $B$. We also consider that, as a result of executing some requests, the hacker receives the sum of the commissions of the requests. Of course, **Lina's** questions have no effect on the system, which remains unchanged after this operation. Due to the robust system of the _Plockchain_, $H$ **is the same** in any of **Lina's** questions.

# Task

Vasile knows that **Lina's** birthday will soon be, so he thought of giving her the best gift in the world: A list of numbers representing the answers to her questions. However, he is much too busy to do it himself, so he delegated you to find them.

# Input data

The first line contains the numbers $N$, $Q$, and $H$, representing the number of requests in the original system, the number of changes explained by Vasile or **Lina's** questions, and the constant $H$ from **Lina's** questions.

The second line contains $N$ numbers, the $i$-th representing $W_i$, the initial commission of the request with index $i$.

The third line contains $N - 1$ numbers, the $i$-th representing $P_{i+1}$, the request on which the request with index $i + 1$ directly depends.

Then follow $Q$ lines, the first number on each being $t$, representing the type of the operation. Then:

1. If $t = 1$, follow $C$ and $T$, representing the parameters of the newly appeared request.
2. If $t = 2$, follow $a$ and $M$, representing the index of the request whose commission is modified, and the value to which it is changed.
3. If $t = 3$, follow $a$, representing the index of the request that is now deleted from the system.
4. If $t = 4$, follow $X$, representing the index of the request for which {\\color{blue}Lina} asks the question.

# Output data

After each question (operation with $t = 4$), print a single number, namely the answer to {\\color{blue}Lina's} question for the current system.

# Constraints and clarifications

* $2 \le N \le 200\,000$;
* $1 \le Q \le 200\,000$;
* $1 \le H \le N$;
* $0 \le C, M \le 1\,000\,000\,000$ for all operations.
* $T < R$ for all operations of type $t = 1$, where with $R$ we have denoted the index of the newly added request following the operation.
* $1 \le P_i < i$ and $0 \le W_i \le 1\,000\,000\,000$, for any initial request $i$.
* It is guaranteed that for any operation, the requests involved in it exist at the time of the operation.
* It is guaranteed that no operation of type $t = 3$ will be performed on the request with number $1$.
* It is guaranteed that no operation of type $t = 3$ will be performed on a request $i$ for which at the time of execution there exists a $j$ such that $P_j = i$.

|#| Score | Constraints | 
|-|-------|-------------|
|1| 13    | $N, Q \le 5\,000$ |
|2| 11    | $P_i = i - 1$, for $2 \le i \le N$, and $t = 4$ for any operation |
|3| 16    | $t = 4$ for any operation |
|4| 10    | $H = 1$ |
|5| 14    | $P_i = i - 1$, for $2 \le i \le N$, and $t = 2$ or $t = 4$ for any operation |
|6| 10    | $P_i = \left\lfloor \frac{i}{2} \right\rfloor$, for $2 \le i \le N$, and $t = 2$ or $t = 4$ for any operation |
|7| 26    | Without additional restrictions. |

# Example

`stdin`
```
8 7 2
10 12 4 20 4 5 11 10
1 1 3 4 2 6 6
1 50 4
4 3
2 1 50
4 1
2 6 35
1 5 7
4 6
```

`stdout`
```
78
91
61
```

## Explanation

For the first query, the requests that are $2$ dependencies down from request $3$ are $3$, $4$, $9$, $5$ with the costs $4$, $20$, $50$, $4$. Therefore, we must print $4 + 20 + 50 + 4 = 78$.

~[graph-vs1.png|align=center]
$$
\text{Initial Structure}
$$

~[graph-vs2.png|align=center]
$$
\text{Structure after the first operation}
$$

~[graph-vs3.png|align=center]
$$
\text{Structure after the first 3 operations}
$$