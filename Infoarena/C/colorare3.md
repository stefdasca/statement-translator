# Colorare3

In the Simple City, there were recent elections for the position of mayor. The winner was elected mainly due to his project to restore the facades of all buildings, and now he must implement it. Simple City consists of $N$ objectives connected by streets, such that for any $2$ such objectives, there is only one way to get from one to the other by traveling on streets. The mayor's plan consists of coloring all houses such that houses on the same street have the same color, and for any $2$ streets that meet at the same objective, the colors are different. Knowing that the mayor has $K$ colors available, he would like to know how many possibilities there are to carry out his coloring plan.

## Input data

The input file `colorare3.in` contains on the first line the numbers $N$ and $K$. There are $N - 1$ lines that follow, each containing $2$ numbers $a$ and $b$ indicating that there is a street between objectives $a$ and $b$.

## Output data

The output file `colorare3.out` will contain the number of coloring possibilities modulo $1\ 000\ 000\ 007$.

## Constraints

$1 \leq N \leq 100\ 000$

$1 \leq K \leq 1\ 000\ 000\ 000$

The objectives are numbered from $1$ to $N$.

## Example

`colorare3.in` 
```
5 3 
1 2 
1 3 
1 4 
3 5 
```

`colorare3.out` 
```
12 
```

## Explanation

It can be observed that after choosing the colors for the streets $(1,2)$, $(1,3)$, $(1,4)$ (having $6$ possibilities), the street $(3,5)$ can be colored in $2$ ways: with the same color as $(1,2)$ or $(1,4)$. With less than $3$ colors, the plan cannot be achieved. Therefore, $6 \times 2 = 12$.