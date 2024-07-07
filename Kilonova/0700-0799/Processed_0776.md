In a room, there are $n \cdot m$ identical aquariums arranged in $n$ rows, with $m$ in each row, side by side. In each aquarium is a single fish. The fish can be red (color coded with $r$) or blue (color coded with $a$). At each moment in time $t = 1,2,3,\dots$, the fish simultaneously change color as follows: each fish is colored in the color that the majority of the fish in the neighboring aquariums had at moment $t-1$ (as in the adjacent drawing, there are at most $8$ neighboring aquariums noted with $V_1,V_2,V_3,\dots,V_8$). If the number of red neighboring fish is equal to the number of blue neighboring fish, the studied fish will keep its color.

~[culori.png|width=17em]

# Task

Write a program that reads the natural numbers $n,m,t$ and the $n \cdot m$ color codes of the fish (those from the initial moment $t=0$) and determines and displays the color codes of the fish at moment $t$.

# Input data

The file `culori.in` contains:

- the first line contains the natural numbers $n \ m$ and $t$, separated by a single space, with the meaning:
    - $n =$ number of rows on which the aquariums are arranged
    - $m =$ number of columns on which the aquariums are arranged
    - $t =$ moment in time
- the next $n$ lines each contain $m$ characters $r$ or $a$, for each row of aquariums, obtained as follows:
    - if the fish in the aquarium with the order number $i$ in the current row is red, then the $i$-th character in the input file line corresponding to the current row is `r`
    - if the fish in the aquarium with the order number $i$ in the current row is blue, then the $i$-th character in the input file line corresponding to the current row is `a`

# Output data

The file `culori.out` will contain $n$ lines, each line will contain $m$ characters $r$ or $a$, representing the color codes of the fish from the row corresponding to the current line number in the file.

# Constraints and clarifications

* $2 \leq n \leq 50$
* $2 \leq m \leq 50$
* $1 \leq t \leq 2\ 300\ 000$

# Example 1

`culori.in`
```
3 3 1
rar
rra
arr
```

`culori.out`
```
rra
rrr
rrr
```

## Explanation

The file `culori.in` contains $4$ lines. There are $9$ aquariums arranged in three rows, with three aquariums in each row. The fish in the first row have, in this order, the colors: red(`r`), blue(`a`), red(`r`). Those in the second row have the colors: red(`r`), red(`r`), blue(`a`), and those in the third row: blue(`a`), red(`r`), red(`r`). The colors of the fish at moment $t=1$ change according to the clarifications in the statement. Thus for the first row of aquariums, the fish in the first aquarium will be red having $2$ red neighbors and $1$ blue neighbor; the fish in the second aquarium will be red having $4$ red neighbors and $1$ blue; the fish in the third aquarium will be blue having $1$ red neighbor and $2$ blues.

# Example 2

`culori.in`
```
4 5 3
rrara
aarra
aarrr
rrraa
```

`culori.out`
```
aarrr
aarrr
rrrrr
rrrrr
```

## Explanation

The successive transformations of the fish colors are:

$t=1$
```
aarar
aarrr
arrra
arrrr
```

$t=2$
```
aaarr
aarrr
arrrr
rrrrr
```

$t=3$
```
aarrr
aarrr
rrrrr
rrrrr
