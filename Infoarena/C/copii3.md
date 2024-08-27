# Children3

Marcel is a great director. In front of him are aligned from $1$ to $N$ some chairs. On a few of these chairs are seated children (extras in one of his films), at most one child on each chair. Being lazy by nature, Marcel thought it would look good to lounge on the interval $[L,R]$ of chairs. To do this, he will have to remove the children from that interval of chairs. Thus, each child in the interval $[L, R]$ will move to an empty chair outside the interval. Marcel will have to pay each moved child a salary bonus equal to the distance traveled (that is, the absolute difference between the start and stop chairs indices). Obviously, Marcel would like to pay as little as possible in total. As Marcel (an ingenious person) wants to quickly choose the best lounging spot, he will make several independent queries $[L, R]$. For each query, find the minimum amount Marcel can pay, or determine if Marcel cannot lounge in the given interval.

## Input data

The input file `copii3.in` contains on the first line the numbers $N$ and $Q$ (the number of queries). The second line contains a sequence of $N$ characters $0$ or $1$; the $i$-th character is $1$ if and only if there is a child on the $i$-th chair. On the following $Q$ lines, there will be two numbers $L$ and $R$, representing the ends of a query from Marcel.

## Output data

The output file `copii3.out` will contain $Q$ lines, the $i$-th line containing the answer to the $i$-th query. The answer to a query where Marcel cannot sit in the given interval is considered to be $-1$.

## Constraints and clarifications

All numbers in the input file are natural

Subtask $1$ (feedback test $3$) - $20$ points:
$1 \leq N, Q \leq 1\,000$

Subtask $2$ (feedback test $7$) - $20$ points:
$1 \leq N \leq 40\,000;$
$1 \leq Q \leq 20\,000$

Subtask $3$ (feedback test $9$) - $20$ points:
$1 \leq N \leq 80\,000;$
$1 \leq Q \leq 20\,000$

Subtask $4$ (feedback test $16$) - $20$ points:
$1 \leq N, Q \leq 80\,000$

Subtask $5$ (feedback test $17$) - $20$ points:
$1 \leq N \leq 320\,000;$
$1 \leq Q \leq 80\,000$

## Example

`copii3.in` 
```
12 3
011101111000
6 9
7 12
1 5
```

`copii3.out`
```
10
-1
24
```

`copii3.in`
```
10 12
0010111010
1 7
2 8
3 9
4 10
5 11
6 12
10 12
5 7
5 9
5 12
0 6
```

`copii3.out`
```
10
-1
17
16
15
14
15
-1
```

## Explanation

Let's consider the first example. We denote with capital letters the children, and we have the sequence $0ABC0DEFG000$.

First query: We want to clear the seats where $D$, $E$, $F$, and $G$ are. $D$ moves one position to the left, and $E$, $F$, and $G$ three positions to the right. The effort is $1 + 3 + 3 + 3 = 10$.

Second query: We want to clear more seats than possible. Therefore, the task cannot be accomplished, so `-1` is displayed.

Third query: We want to clear the first $5$ seats. The final sequence obtained will be $00000ABCDEFG$, or $00000DEFGABC$, or $00000DEFGCBA$, $\dots$, all obtaining the cost of $24$.