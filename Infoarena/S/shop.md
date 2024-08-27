## Task

Zaharel is once again shopping at the store owned by Nargy and Fumeanu. After purchasing products worth $L$ lei, Zaharel must pay exactly $L$ lei at the counter using the coins he has. It is known that in Zaharel's country, all coins are in the form $C \cdot P$ where $C$ is a value fixed by the government. Thus, Zaharel has at his disposal $N$ types of coins, the coin of type $i$ being worth $C \cdot A_i$ lei, and Zaharel possesses $B_i$ such coins. Of course, Zaharel wants to pay the amount of $L$ lei with the minimum number of coins.

## Input data

The input file `shop.in` contains on the first line the natural numbers $N$, $C$, $L$ separated by spaces. The following $N$ lines contain pairs of numbers $A_i$ $B_i$ as described above.

## Output data

The output file `shop.out` will contain a single natural number, representing the minimum number of coins needed to pay the amount of $L$ lei. The next line will contain $N$ natural numbers, the $i$-th number representing how many times the coin of type $i$ was used.

## Constraints and clarifications

$1 \leq N \leq 30$

$1 \leq C \leq 10$

$0 \leq L \leq 10^{16}$

$0 \leq A_i \leq 32$

$1 \leq B_i \leq 10^9$

It is guaranteed that the value of any coin is less than or equal to $L$

The $N$ types of coins have distinct values

For 50% of the tests $L \leq 1\ 000\ 000$

It is guaranteed that a solution exists; if there are multiple solutions, any one of them can be displayed

## Example

`shop.in`

```
4 2 47
0 5
3 2
2 4
1 9
```

`shop.out`

```
3 
2 3 1 
```

## Explanation

$47 = 2 \cdot 0 + 2 \cdot 0 + 2 \cdot 0 + 2 \cdot 3 + 2 \cdot 3 + 2 \cdot 2 + 2 \cdot 2 + 2 \cdot 2 + 2 \cdot 4 = 1 + 1 + 1 + 8 + 8 + 4 + 4 + 4 + 16$