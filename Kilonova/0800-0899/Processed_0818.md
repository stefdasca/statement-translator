One of the attractions of the famous Prater amusement park in Vienna is the Vienna Giant Ferris Wheel. From it, the view of the entire Vienna can be admired.

The wheel has $n$ cabins, numbered from $1$ to $n$ clockwise and symmetrically arranged on the circumference of the wheel. Customers are boarded in the cabin where the wheel is tangent to the ground, and the rotation starts with cabin $1$ in the boarding position and rotates counterclockwise. A customer pays $1$ EUR for a rotation and can buy any number of rotations.

The $p$ customers who want to use the wheel must follow this procedure: the customer with the order number $i$ buys a ticket on which their order number and the number of rotations $c_i$ are written, then they get in line. When a cabin is free in the boarding position or a cabin is vacated, the wheel stops and the next customer boards. A customer disembarks after completing the number of rotations written on their ticket.

# Task

Write a program that, knowing the number $n$ of cabins of the wheel, the number $p$ of customers, and the number of rotations bought by each customer, $c_i$, calculates:

* the total amount collected by the wheel administrator from the customers;
* the order in which the customers disembark from the wheel;
* the number of the cabin from which the last customer disembarks.

# Input data

The input file `roata.in` contains the first line, the natural number $n$, the second line the natural number $p$, and the third line the natural numbers $c_i$, separated by a space, with the meanings given above.

# Output data

The output file `roata.out` will contain the first line the total amount collected, the second line the order numbers of the customers, in the order of disembarkation, separated by a space, and the third line the number of the cabin from which the last customer will disembark.

# Constraints and clarifications

* $2 \leq n \leq 360$;
* $1 \leq p \leq 100\ 000$;
* $1 \leq c_i \leq 100\ 000$;
* solving the first task is worth $20\%$ of the score, while each of the other two tasks is worth $40\%$ of the score.

# Example

`roata.in`
```
4
7
6 4 1 5 2 8 3
```

`roata.out`
```
29
3 5 2 4 1 7 6
3
```

## Explanation

The wheel has $n = 4$ cabins and the number of customers is $p = 7$. The first customer buys $6$ rotations, the second $4$ rotations, $\dots$, and the seventh customer buys $3$ rotations. The total amount collected is $29$ EUR. After the first $4$ customers board the wheel and a complete rotation is made, the first to disembark is the third customer and the fifth customer immediately boards. After another $2$ rotations, the fifth customer disembarks and the sixth customer boards. After another rotation, the second customer disembarks and the seventh customer boards. The last $4$ customers disembark in the order $4, 1, 7, 6$. The cabin from which the last customer disembarks is cabin number $3$.