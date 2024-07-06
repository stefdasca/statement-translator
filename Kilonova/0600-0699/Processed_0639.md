The latest attraction for the national informatics team is chess. So, Gimi decided to start a business selling chess collections. These collections contain unseen tactics, making the demand high.

In advance, he received the order list. Daily, for $N$ days, he will have to deliver $c_i$ collections at the end of day $i$. Gimi started his business by buying a factory that can produce $K$ collections per day, with the initial stock of collections being $S = 0$.

Daily, he can choose one of the following two options:
* Gimi stops production for the day and upgrades the factory. As a result of the improvements, the production capacity of the factory will increase by $1$ ($K \leftarrow K + 1$).
* Gimi closely monitors the printing process. Thus, the stock of collections will increase by $K$ ($S \leftarrow S + K$).

At the end of day $i$, he will deliver $c_i$ collections ($S \leftarrow S - c_i$). If he does not have at least $c_i$ collections in stock, his lack of punctuality will be highlighted, and the activity will not be able to continue.

# Task

Knowing the number of days in which the activity takes place, the initial daily production, and the list of the $N$ orders, solve the following tasks:
* If $T = 1$, then Gimi wants to know the maximum number of collections he can have in stock at the end of the last day (the $N$-th day).
* If $T = 2$, then Gimi wants to know the maximum number of collections he can have in stock at the end of the $i$-th day, for each $i$ from $1$ to $N$.

# Input data
The first line of the input file contains three numbers $T$, $N$, and $K$, separated by a space. The second line will contain $N$ numbers, where the $i$-th number represents $c_i$, the order of collections on day $i$.

# Output data 
* If $T = 1$, the output file will contain a single natural number representing the maximum possible number of collections left in stock at the end of the $N$-th day.
* If $T = 2$, the output file will contain, on a single line, $N$ natural numbers separated by a space, where the $i$-th number represents the maximum possible number of collections left in stock at the end of the $i$-th day.

# Constraints and clarifications

* $1 \leq N \leq 500\ 000$
* $0 \leq K \leq N$
* $0 \leq c_i \leq N \cdot K$
* It is guaranteed that there is a way for Gimi to continue his activity until the last day inclusive.
* The strategy used for day $i$ does not necessarily have to be continued on day $i + 1$. A different strategy can be used than that for the previous day.

|#|Score|Constraints|
|-|-|--------|
|1|7|$T = 1$ and $1 \leq N \leq 15$|
|2|14|$T = 1$ and $1 \leq N \leq 2\ 000$|
|3|19|$T = 1$ and $1 \leq N \leq 500\ 000$|
|4|8|$T = 2$ and $1 \leq N \leq 15$|
|5|21|$T = 2$ and $1 \leq N \leq 2\ 000$|
|6|31|$T = 2$ and $1 \leq N \leq 500\ 000$|

# Examples
`collections.in`
```
2 5 2
1 1 3 1 3
```
`collections.out`
```
1 2 1 2 2
```
\
`collections.in`
```
1 5 2
1 1 3 1 3
```
`collections.out`
```
2
```

# Explanations

For the first example, $T = 2$, so the second task is solved. We denote with "$P \ x$" the days in which we will produce $x$ collections, and with "$I \ 1$" the days in which we will increase the production by 1. The optimal strategies, for each day, might be:
* day 1: $P \ 2$
* days 1-2: $P \ 2 \rightarrow P \ 2$
* days 1-3: $P \ 2 \rightarrow P \ 2 \rightarrow P \ 2$
* days 1-4: $P \ 2 \rightarrow I \ 1 \rightarrow P \ 3 \rightarrow P \ 3$
* days 1-5: $P \ 2 \rightarrow I \ 1 \rightarrow P \ 3 \rightarrow P \ 3 \rightarrow P \ 3$

It is observed that the strategies differ depending on the day the experiments will end. For days 1-4, the production capacity will increase on the second day, but for days 1-3, the production capacity will not change.

Additionally, it is impossible to increase the production capacity on the first day because the stock would be zero, and Gimi needs to deliver one collection.
\
For the second example, $T = 1$, so the first task will be solved. Only the maximum possible stock at the end of the last day will be displayed.