After becoming the most renowned businessman in Europe, you moved to New York and want to show the Americans that you are *the best*. The strategy that brought you all your success is as follows: you buy a building, renovate it, and then sell it at a higher price. 

There are $N$ buildings for sale. The $i$-th building costs $a_i$ dollars, but according to your calculations, if you renovate and sell it later, you can earn $b_i$ dollars in profit. 

A building can be purchased at most once (because there would be nothing left to renovate a second time), and they can be bought and sold in any order. 

Furthermore, you must never have a negative amount of dollars in the account, so to purchase the $i$-th building, you must have at least $a_i$ dollars at the time of purchase.

**Attention!** You **do not** sell the building for $b_i$ dollars; rather, you earn $b_i$ dollars (in fact, you sell it for $a_i + b_i$ dollars).

# Task

After thorough research, you have identified $N$ buildings that could lead to a profit. You are still unsure exactly how costly moving to New York will be, so you ask yourself $Q$ questions of the form: If I were to arrive with $T$ dollars, what is the maximum wealth (in dollars) I could possess upon arrival in New York?

# Input data

The first line contains the number $N$, representing the number of buildings that could potentially bring you a profit.

The $i + 1$-th line ($1 \leq i \leq N$) contains the values $a_i$ and $b_i$, in that order.

The line $N + 2$ contains the number $Q$, representing the number of questions.

Each of the following $Q$ lines contains an integer $T$, representing the initial number of dollars.

# Output data

You must print $Q$ lines. The $i$-th line will contain the answer to the $i$-th question.

# Constraints and clarifications

$\textcolor{red}{Attention!}$ Due to the large number of input and output data, we recommend adding the following lines of code at the beginning of the `main()` function.

```c++
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
```

* $1 \leq N \leq 200 \ 000$
* $1 \leq Q \leq 1 \ 000 \ 000$
* $1 \leq a_i, b_i \leq 10^9$
* $1 \leq T \leq 10^9$

|#|Score|Constraints|
|-|-|--------|
|1|6|$N = 1, Q \leq 100$|
|2|21|$N, Q \leq 5 \ 000$|
|3|18|$N \leq 5 \ 000$|
|4|16|$a_i \leq 5 \ 000$|
|5|39|No other constraints|

# Example 1

`stdin`
```
3
3 4
1 1
9 6
10
1 2 3 4 5 6 7 8 9 10 
```

`stdout`
```
2
7
8
15
16
17
18
19
20
21
```

## Explanation

$T = 1$: I can buy and renovate building $2$. I can since $a_2 = 1$, so $T \geq a_2$. Initially, I had one dollar, and now I have $1 + b_2 = 1 + 1 = 2$

$T = 2$: Initially, I buy and renovate building $2$. Now, I have $3$ dollars, so I can also buy building $1$. After selling building $1$, I will have $3 + 4 = 7$ dollars.

$T = 3$: Similar to $T = 2$, I will buy buildings $2$ and $1$ in this order. I will have $3 + 1 + 4 = 8$ dollars.

$T = 4$: After buying buildings $2, 1$ I have $9$ dollars. Thus, I can buy building $3$, and finally, I will have $4 + 1 + 4 + 6 = 15$ dollars.