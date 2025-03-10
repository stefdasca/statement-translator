
# Task

David needs to pay for his order from Tenu. He ordered $a$ identical products, each priced at $b$. Unfortunately, he only has banknotes with values of the form $5^k$. Knowing the numbers $a$ and $b$, which have $n$ and $m$ digits respectively, and the number $k$, find the change the courier owes David, assuming he pays the minimum amount necessary to settle the order.

# Input data

The first line contains the numbers $n$, $m$, and $k$ with their meaning as described in the problem statement.  
The second line contains $n$ digits separated by space, representing the number $a$.  
The third line contains $m$ digits separated by space, representing the number $b$.

# Output data

The first line will contain a single integer, representing the change that David should receive.

# Constraints and clarifications

* $1 \leq k \leq 12$;  
* $1 \leq n, m \leq 100 \ 000$;  
* **This problem differs from the one in the competition, having banknote values of the form $5^k$ instead of $2^k$. We made this change to evaluate solutions in the way we desired.**  
* For fast input and output, it is recommended to use these lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```

| # | Score |            Constraints           |
| - |:-----:|:-------------------------------:|
| 1 | 10    |    $n, m \leq 9$                |
| 2 | 20    |    $n, m \leq 18$               |
| 3 | 30    |    $n, m \leq 1 \ 000$          |
| 4 | 40    |    $n, m \leq 100 \ 000$        |

# Example 1

`stdin`
```
2 3 2
3 0
1 3 5
```

`stdout`
```
0
```

## Explanation

David will have to pay a total amount of $30 \cdot 135 = 4050$. He only has banknotes with the value $5^2 = 25$, so he can pay the exact amount without needing any change.

# Example 2

`stdin`
```
7 8 3
7 6 2 0 5 7 5
6 8 6 7 6 7 5 4
```

`stdout`
```
75
```

## Explanation

David will have to pay a total amount of $7 \ 620 \ 575 \cdot 68 \ 676 \ 754 = 523 \ 356 \ 354 \ 613 \ 550$, with banknotes valued at $5^3 = 125$, so he will have to receive a change of $75$.

# Example 3

`stdin`
```
18 17 9
4 2 2 2 6 1 0 0 3 3 1 0 1 4 2 2 3 5 
9 1 0 5 8 0 9 6 4 8 1 5 1 3 2 1 6 
```

`stdout`
```
1862865
```
