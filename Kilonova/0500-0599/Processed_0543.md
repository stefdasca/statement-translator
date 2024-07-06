History: "*On September 29, 1474, Ștefan cel Mare requested help from Pope Sixtus IV in preparation for the impending war on the horizon.*" As autumn approached and time was running out due to the imminent war, Ștefan decided to personally oversee the grape harvest at the vineyards in Huși, near Vaslui, a vineyard that Ștefan highly valued. The harvested grapes were deposited in piles at the end of each row of vines. For each of the $N$ rows, the amount (in "ocale") harvested from that row is known. Ștefan decided that the transportation of the grapes to the cellar would be done using carts, with one cart being able to transport any amount of grapes. Given the bountiful harvest, transportation would be done in one or more trips. Ștefan, who was carefully supervising the activity, noticed that for each trip, he had **exactly as many** carts as there were piles left to be transported. Ştefan was a fair leader and therefore decided that all the carts available at any given time should transport **the same** amount of grapes.

# Task

1. Determine the longest **sequence** of piles that the $N$ carts can transport **in the first trip**.
2. Determine **a way** to transport all the grapes to the cellar, according to Ștefan's requirements.

# Input data

The input file `struguri.in` contains on the first line two natural numbers $C$ and $N$, separated by a space, representing the task ($1$ or $2$) and the number of piles of grapes that need to be transported. The second line contains $N$ non-zero natural numbers, separated by a space, representing the $N$ quantities of grapes.

# Output data

If the task is $1$, the output file `struguri.out` will contain on the first line three natural numbers, separated by a space, representing the length of the sequence of piles, the index of the first pile in the sequence, and the index of the last pile in the sequence.
If the task is $2$, the output file will contain on the first line the number $T$ of trips; each of the following $T$ lines has the same structure:
* the first three values represent:
    - the number of carts transporting grapes in that trip
    - the amount of grapes each cart transports
    - the number of piles transported; 
* the following values on that line represent **the indices** of the piles transported in that trip; values will be displayed in ascending order and separated by a space.

# Constraints and clarifications

* $1 \\leq N \\leq 20 \\ 000$;
* The quantities are less than $100 \\ 000$;
* For both tasks, any correct solution is accepted;
* For task $1$ $46$ points are awarded, and for task $2$ $54$ points are awarded.

|# | Points | Constraints|
| - | -- | ------------|
| 1 | 12 | $1 \\leq N \\leq 10$, of which 5 points are awarded for task 1 |
| 2 | 30 | $11 \\leq N \\leq 100$, of which 12 points are awarded for task 1 |
| 3 | 14 | $101 \\leq N \\leq 1 \\ 000$, of which 8 points are awarded for task 1 |
| 4 | 27 | $1 \\ 001 \\leq N \\leq 10 \\ 000$, of which 21 points are awarded for task 1 |
| 5 | 17 | $10 \\ 001 \\leq N \\ 20 \\ 000$ |

# Example 1

`struguri.in`
```
1 10
2 1 3 4 5 10 6 8 9 7
```

`struguri.out`
```
5 6 10
```

## Explanation

From the sixth pile to the tenth, there are a total of $40$ ocale; each of the $10$ carts will transport $4$ ocale.

# Example 2

`struguri.in`
```
2 5
7 8 11 2 5
```

`struguri.out`
```
3
5 4 3 1 2 5
2 1 1 4
1 11 1 3
```

## Explanation

A possible solution could be the following:
*Trip 1*: there are $5$ piles, so there are $5$ carts (each cart transports $4$ oca from $3$ piles ($1 \\ 2 \\ 5$))
*Trip 2*: there are $2$ piles left, so there are $2$ carts, each transporting $1$ oca from pile $4$
*Trip 3*: there is one pile left, so there is $1$ cart, which will transport $11$ ocale from pile $3$
Another correct solution could be described in the output file as:
```
2
5 3 2 1 2 
3 6 3 3 4 5 
```
In this situation, there are 2 trips: in the first, each of the $5$ carts transports $3$ ocale from piles $1$ and $2$. In the second trip, $3$ carts will be used, each transporting $6$ ocale from piles $3$, $4$, and $5$.