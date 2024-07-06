Before long, in Bukovina, there were only $N$ cities connected by $N-1$ bidirectional roads. However, it was possible to travel from any city to any other city by traveling on one or more roads.

When Ștefan had to make an important announcement, he would send the message to each of his $M$ messengers. Each messenger, after receiving the message from Ștefan, would leave to transmit the received message along a fixed route. Specifically, messenger $i\\ (1 \\leq i \\leq M)$ will transmit the message to all the cities situated on the route starting from city $a_i$ and ending in city $b_i$. To transmit the message to all the cities on their route, messenger $i\\ (1 \\leq i \\leq M)$ will receive $X_i$ gold coins.

# Task

What is the minimum number of gold coins Ștefan had to pay for his message to reach all the $N$ cities in Bukovina?

# Input data

The input file `mesaj.in` contains on the first line the natural number $N$, representing the number of cities in Bukovina. The next $N-1$ lines each contain two distinct natural numbers separated by a space $a \\ b$ with the meaning "there is a road that connects directly the cities $a$ and $b$". On line $N+1$ there is a natural number $M$ representing the number of messengers. On the following $M$ lines there is information about the $M$ messengers. On the $i$-th line among the $M (1 \\leq i \\leq M)$ there are written three natural numbers separated by a space $a_i \\ b_i \\ X_i$, meaning "messenger $i$ traverses the route from city $a_i$ to city $b_i$, being paid $X_i$ gold coins".

# Output data

The output file `mesaj.out` will contain a single line which will contain the minimum number of gold coins Ștefan must pay for the message to be transmitted to all the $N$ cities.

# Constraints and clarifications

* $2 < N < 11\ 011$
* $2 < M < 110\ 011$ 
* $0 < X_i < 1\ 111$, for any $1 \\leq i \\leq M$ 
* $1 \\leq a_i, b_i \\leq N$, for any $1 \\leq i \\leq M$ 
* There will not be more than $9$ messengers passing through the same city.

# Example

`mesaj.in`
```
10
1 2
1 3
3 4
3 5
5 6
5 7
5 8
2 9
2 10
9
8 6 10
10 9 10
1 4 30
4 1 10
7 8 50
1 7 10
6 1 10
10 1 10
9 1 10
```

`mesaj.out`
```
40
```

## Explanation

The minimum required sum is $40$ gold coins. Four messengers are required, with the routes:
* $8 \\ 6$
* $1 \\ 7$
* $4 \\ 1$
* $10 \\ 9$
There are other solutions, but for these, the required sum is higher.