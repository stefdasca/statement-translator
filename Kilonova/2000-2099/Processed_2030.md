**~[img1.jpg|align=right]**

Maxi opened a second-hand furniture store and has many orders for cupboards which he transports with an old car (it’s a second-hand car). The car is specially designed to transport heavy cupboards. The trailer of the car is divided into two parts as shown in the adjacent figure. The car is so old that if one side of the car (left or right) is continuously used for $k$ consecutive days, the axle on that side will break. Hence, we say that the resistance of the car is $k$. The car can transport $0$, $1$, or $2$ cupboards per day, and the transports will be planned in such a way that the car does not break.

In Maxi's city, a week has $n$ days, and the transport orders repeat identically every week. For example: the resistance of the car is $k=3$, a week has $n=8$ days, and the weekly order distributed over days is: $1, 2, 1, 0, 1, 1, 2, 1$.

The 8-day plan below is correct because no part of the car will transport cupboards for $3$ consecutive days:
**~[img2.jpg|align=center]**

The following plan is incorrect because in the first three days the car will transport cupboards on the right side:
**~[img3.jpg|align=center]**

# Task
Find in how many ways modulo $40 \ 099$ the transports can be planned over $z$ given days, if the car's resistance $k$, the number $n$ of days in a week, and the weekly order string are known.

# Input data
The file `marfa.in` contains on the first line two natural numbers $z$ and $k$ as described above. The second line contains the number $n$ of days in a week. The third line contains $n$ natural numbers with values $0$, $1$, or $2$ separated by space, representing the weekly furniture order.

# Output data
The file `marfa.out` will contain a single natural number, the number of correct distinct plans modulo $40 \ 099$.

# Constraints and clarifications
* $3 \leq k \leq 4$
* $5 \leq n \leq 19$
* $1 \leq z \leq 2 \ 000 \ 000 \ 000$

# Example

`marfa.in`
```
6 3
5
1 0 2 2 0
```

`marfa.out`
```
4
```

## Explanation

You are asked for the number of plans over $6$ days, with the car’s resistance being $k=3$ days. The week has $5$ days.
For the order $1 \ 0 \ 2 \ 2 \ 0$ we have $4$ possible plans (the order on the $6^{th}$ day is $1$, the same as the first day, as the week restarts):
**~[img4.jpg]**