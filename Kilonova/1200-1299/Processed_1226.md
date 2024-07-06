Vacanța de primăvară îi oferă elevului Ionuț prilejul de a se odihni, a citi și a se juca. Este prea scurt timpul pentru a-și mai face și teme... Printre "jocurile clasice" ale părinților a descoperit și un joc cu bețișoare. Tabla de joc are pe mijloc, de-a lungul ei, un șanț cu poziții numerotate de la $1$ la $L$. Pe tablă sunt plasate, în șanț, bețișoare cu capătul stâng într-o anumită poziție. Bețele au lungimi diferite. Regula jocului este de a elimina cât mai puține bețe pentru a obține un număr maxim de bețe care nu se ating.

# Task

Write a program that determines the maximum number of sticks that Ionuț can obtain.

# Input data

The input file `bete.in` contains on the first line an integer value $n$ representing the number of sticks placed on the game board, and on the next $n$ lines, two values $p$ and $l$, separated by a single space, representing the position on the board and respectively the length of each stick.

# Output data

The output file `bete.out` will contain a single value representing the maximum number of sticks remaining on the board such that they do not touch.

# Constraints and clarifications

* $1 < p + l < 2^{15}-1$
* $1 \leq L \leq 2^{15}-1$
* $1 < n < 5 \ 000$

# Example 1

`bete.in`
```
4
1 1
2 1
3 1
4 1
```

`bete.out`
```
2
```

## Explanation

One solution could be: the stick which starts from position $1$ and has a length of $1$ remains on the board along with the stick which starts from position $3$ and has a length of $1$.

# Example 2

`bete.in`
```
4
4 5
3 6
4 4
5 2
```

`bete.out`
```
1
```

## Explanation

Any stick can remain on the board, the other $3$ being eliminated.

# Example 3

`bete.in`
```
4
6 1
1 1
4 1
8 1
```

`bete.out`
```
4
```

## Explanation

All $4$ sticks remain on the board.

