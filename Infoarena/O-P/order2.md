# Order 2

Gigel, an avid computer games player, recently found a new game that challenges his intelligence. He receives $N$ numbers that he needs to sort in ascending order by performing the following operations: he fixes a position $X$, and the computer automatically reverses the sequences $1 , 2 \dots X-1$ and $X+1 , X+2 \dots N$, leaving the element $X$ in its position.

## Task

Gigel, being highly addicted to this game, spends a lot of time in front of the computer trying to solve game levels. Therefore, his parents ask you to make a program that tells Gigel which positions he needs to fix and in what order to arrange the elements in ascending order.

## Input data

The first line of the file `order2.in` contains the number $N$, and on the next $N$ lines, each line contains one number representing the $N$ elements that Gigel needs to sort.

## Output data

The file `order2.out` will contain the elements to be fixed, in order, one per line, so that the sequence ends up sorted in ascending order.

## Constraints

$1 \leq N \leq 2\, 000$

The elements in the array will be distinct numbers, less than or equal to $10\, 000$.

For each test, you score if the number of moves is less than or equal to $2N$ and the sequence of operations correctly sorts the array from the input file. Otherwise, the score for that test will be $0$ points.

You can also fix the fictional elements $0$ and $N+1$.

## Example

`order2.in`
```
4
20
5
50
25
```

`order2.out`
```
3
2
```

