A gas station has an underground tank that can store at most $L$ liters of gas, but there is the possibility of storing additional gas in a rented tank with unlimited capacity for which a fee of $C$ dollars is paid for each liter of gas stored from one day to the next. To serve its customers, the station supplies gas at most once a day, in the morning. The price of a liter of gas is $D$ dollars. For each supply, an additional fee of $P$ dollars is paid in addition to the cost of the ordered gas. Under these conditions, ordering a large amount of gas can increase the storage cost.

The gas station closes after $N$ days. It delivers to its customers $G_i$ liters of gas, from its stock, at the end of each day $i$, where $i=1,2, \ldots , N$. The problem is to choose the quantities of gas to be ordered daily so that at the end of the $N$-th day the entire stock is consumed and the total cost is minimal. It is assumed that the tank is initially empty.

# Task

Write a program that determines the minimum total cost for the station to serve its customers in the $N$ days and consume the entire quantity of gas at the end of the $N$-th day.

# Input data

The first line of the input file `gaz.in` contains four natural numbers separated by a space, $L, P, D, C$, with the meaning given above.

The second line contains the natural numbers $N, G_1, G_2, \ldots G_N$, separated by a space, where $N$ represents the number of days after which the station will be closed and $G_i$ the quantity of gas needed for the day $i$, $i=1,2, \ldots, N$.

# Output data

The output file `gaz.out` will contain on the first line the minimum total cost required.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* $1 \leq L, G_i \leq 1\ 000, i = \{ 1, 2, \ldots, N \}$
* $1 \leq P, D, C \leq 5\ 000$
* For $80\%$ of tests we will have $N \leq 100$

# Example

`gaz.in`
```
5 3 1 1
5 3 2 4 5 1
```

`gaz.out`
```
22
```

# Explanation

An optimal planning is described below.

On the morning of the first day, order $5$ liters of gas and store it in the own tank. At the end of the day, deliver $3$ liters. The cost of the first day is $5+3=8$. During the night, $2$ liters will remain in the own tank, without additional costs.

On the second day, the station does not supply but delivers $2$ liters of gas. The cost of this day is $0$.

On the morning of the third day, order $10$ liters of gas, storing $5$ liters in each of the two tanks. In the evening, deliver $4$ liters from the rented tank. During the night, $5$ liters of gas remain in the own tank, and one more liter in the rented tank for which one dollar will be paid. Thus, the total cost adds up to $10+3+1=14$ dollars.

On the morning of the fourth day, the station does not supply, but in the evening delivers $5$ liters of gas, one from the rented tank and $4$ from the own tank. During the night, there will be no additional storage costs.

On the last day, deliver the last liter of gas from the own tank.

The total cost is: $8+14=22$.