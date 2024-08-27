## Task

Vultur is an avid coin collector and currently his collection counts $N$ coins with natural number values between $1$ and $50\,000$. However, he wants to buy a new aquarium for his fish and therefore he is thinking of giving some of his coins to the bank. Being a sentimental person, he would still like to ensure that using the remaining coins, it is possible to obtain any value of the coins he gave to the bank. Choose for Vultur a minimum subset of coins from the $N$ such that any value from the $N$ can be written as a sum of the values of the coins from the chosen subset (the value of a coin from the chosen subset can be added multiple times).

## Input data

The file `economie.in` contains on the first line the number $N$ as described above, and on the next $N$ lines, it contains the value of Vultur's coins.

## Output data

The file `economie.out` contains on the first line the number $MIN$, representing the minimum number of coins in the chosen subset. On the next $MIN$ lines, it contains the values of the chosen coins. If there are multiple solutions, any one of them can be displayed.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq V_i \leq 50\,000$

## Example

`economie.in`

```
3
1
3
5
```

`economie.out`

```
1
1
```

## Explanation

If we choose the coin with value $1$, then the coins with values $3$ and $5$ can be obtained using $3$ coins with value $1$, respectively $5$ coins with value $1$.