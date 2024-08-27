## Task

At the kindergarten in the center of Suceava, there are $N$ children, numbered from $0$ to $N-1$. The mayor visits them and decides to give them marbles. Thus, he has a big bag full of marbles, each inscribed with a natural number. From time to time, the mayor asks the children questions about the marbles they have received. Here are the operations the mayor can perform:
- he gives each child with numbers in the interval $[a,b]$ a marble inscribed with the number $p$
- he asks what the number inscribed on the $k$-th marble in the sequence formed from the marbles of the children in the interval $[a,b]$ is, knowing that the marbles are arranged in ascending order of the numbers inscribed on them; if there are not $k$ marbles in the interval $[a,b]$, the answer will be $-1$

Help the children answer the mayor's questions.

## Input data

The first line of the file `bile4.in` contains a natural number $N$, representing the number of children.

The next line contains a natural number $M$, representing the number of operations performed by the mayor.

The next $M$ lines describe the operations performed by the mayor, one operation per line. A line describing an operation can have one of the following two formats:

## Explanation

$1\ a\ b\ p$ describes an operation of type $1$ (the mayor will give each child in the interval $[a,b]$ a marble inscribed with the natural number $p$)

$2\ a\ b\ k$ describes an operation of type $2$ (the mayor asks the children what the number inscribed on the $k$-th marble in the sequence formed from the marbles of the children in the interval $[a,b]$ is, knowing that the marbles are arranged in ascending order of the numbers inscribed on them)

## Output data

In the file `bile4.out`, you will print one line for each operation of type $2$ in the input file. On the $i$-th line there will be an integer representing the answer for the $i$-th operation of type $2$ in the input file.

## Constraints

$1 \leq N \leq 30000$ 

$1 \leq M \leq 30000$ 

$1 \leq$ number inscribed on the marbles $\leq 30000$ 

a child can have multiple marbles, possibly of the same value 

after an operation of type $2$, the configuration of the marbles remains unchanged 

initially all children have $4$ marbles 

## Example

`bile4.in`
```
10
10
1 8 9 5
1 6 6 2
2 8 8 1
2 5 7 1
1 1 6 7
2 2 1 8 3
2 6 7 1
2 5 5 1
1 1 9 9
1 2 7 8
```

`bile4.out`
```
1
1
2
2
-1
2
```