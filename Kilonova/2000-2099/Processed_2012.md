```markdown
At Eden Academy's art class, Anya has to construct a string of pearls. Initially, Professor Henderson gives Anya two numbers, $Q$ and $K$. Then, the professor gives Anya $Q$ instructions of the following types:
* Addition: Anya has to add a pearl with price $x$ at the right end of the string.
* Deletion: Anya has to remove the pearl at the right end of the string and state its price.
* Special Deletion: Anya has to remove (using a hammer-breaking method) the **$K$-th least valuable** pearl in the string and state its price. A pearl $A$ is considered more valuable than another pearl $B$ if $A$ has a higher price than $B$, or if $A$ has the same price as $B$ but was added to the string at a later time than when pearl $B$ was added to the string.

If Anya cannot perform a deletion operation (because the string is empty), or a special deletion (because there's not at least $K$ pearls in the string), it is considered that the operation cannot be performed, and Anya does not remove any pearl from the string.

At the end, Anya has to present in front of the class the string of pearls obtained after performing the $Q$ operations.

# Input data

The first line contains $2$ natural numbers $Q$ and $K$, separated by a space, with the meaning from the statement.
The next $Q$ lines contain the $Q$ operations that Anya has to perform, coded as follows:
* $1 \\ x$: addition of a pearl with price $x$;
* $2$: deletion;
* $3$: special deletion.

# Output data

Print, in order, for each deletion or special deletion operation, one line containing a number $x$ representing the price of the pearl removed from the string following the respective operation. If the operation cannot be performed, the value of $x$ will be $−1$.
On the last line, print, in order, from left to right, the prices of the pearls in the string obtained after performing the $Q$ operations.

# Constraints and clarifications

* $1 \\leq Q, K \\leq 500 \\ 000$
* The prices of the added pearls are positive natural numbers less than or equal to $1 \\ 000 \\ 000 \\ 000$.
* It is guaranteed that the string obtained after performing the $Q$ operations contains at least one pearl.
| # | Points | Constraints |
| - | ------- | ---------- | 
| 1 | 8 | $1 \\leq Q \\leq 1 \\ 000$ and all pearls added to the string have distinct prices. |
| 2 | 4 | $1 \\leq Q \\leq 1 \\ 000$ |
| 3 | 12 | $K = 1$, and all pearls added to the string have distinct prices. |
| 4 | 8 | $K = 1$ |
| 5 | 20 | There are no type $2$ operations (deletion), and all pearls added to the string have distinct prices. |
| 6 | 15 | There are no type $2$ operations (deletion). |
| 7 | 19 | All pearls added to the string have distinct prices. |
| 8 | 14 | No additional constraints |

# Example

`stdin`
```
10 2
1 2
1 3
1 5
1 2
1 4
2
1 1
3
2
1 6
```

`stdout`
```
4
2
1
3 5 2 6
```

## Explanation

After the first $5$ addition operations, the string has the form $2 \\ 3 \\ 5 \\ 2 \\ 4$.
Operation $6$ is a deletion operation, and the removed pearl has a price of $4$. The string is now in the form $2 \\ 3 \\ 5 \\ 2$.
Operation $7$ is an addition operation, and the string becomes $2 \\ 3 \\ 5 \\ 2 \\ 1$.
Operation $8$ is a special deletion operation, and the removed pearl has a price of $2$. Since the first pearl with price $2$ was the second least valuable and was removed, the string is now in the form $3 \\ 5 \\ 2 \\ 1$.
Operation $9$ is a deletion operation, and the removed pearl has a price of $1$. The string is now in the form $3 \\ 5 \\ 2$.
Operation $10$ is an addition operation, and the string becomes $3 \\ 5 \\ 2 \\ 6$, which we also print.
```