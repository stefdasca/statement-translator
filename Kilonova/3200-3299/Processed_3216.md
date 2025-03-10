Our group, "The Cracg Mafia," consists of $N$ members who are very loyal to each other. Thus, every time someone from the group provides a service to another person, both individuals remember this so that they can later reciprocate. However, some members sometimes find themselves unable to repay their debts, which is why they have chosen to ask for your help. You know that there are $M$ "debt" relationships between two people. These relationships can be reduced in the following way:

* If $a$ owes $b$ and $b$ owes $a$, then we say they are even, and both debts disappear.
* If $a$ owes $b$ and $b$ owes $c$ ($c \ne a$), then both debts disappear and are replaced by a debt of $a$ to $c$ (we eliminate the "middle-man").

# Task

The mafia now wants to know if, by applying the above operations, it is possible for there to finally be no debts between members. They ask you to find out this information for them.

# Input data

The first line contains two natural numbers, $N$ and $M$. Each of the following $M$ lines contains two distinct natural numbers $a$ and $b$, indicating a debt relationship between $a$ and $b$ ($a$ owes $b$).

# Output data

If it is possible for there to finally be no outstanding debts, print the message `Even`. Otherwise, if such a situation is not achievable, print the message `Debts`.

# Constraints and clarifications

* $3 \le N \le 100 \ 000$;
* $2 \le M \le 100 \ 000$;
* $1 \leq a, b \leq N$;
* A member of the mafia provided you with important information: irrespective of the order of reductions, the answer will always be the same;
* It is possible for there to be multiple debt relationships between two people $a$ and $b$. In this situation, the pair $(a, b)$ will appear multiple times in the input data;
* For tests worth $19$ points, $N \le 10$, $M \le 15$;
* For other tests worth $31$ points, $N \le 5$;
* For other tests worth $18$ points, $M \le 5$;
* For other tests worth $32$ points, there are no additional restrictions.

# Example 1

`stdin`
```
5 5
1 2
2 3
3 1
4 5
5 4
```

`stdout`
```
Even
```

## Explanation

We have two cycles of debts, among members $1$, $2$, and $3$, and among members $4$ and $5$. Both can be reduced so that the members remain even.

# Example 2

`stdin`
```
4 3
1 2
2 3
3 4
```

`stdout`
```
Debts
```

## Explanation

No matter how hard we try, in the end, member $1$ will owe member $4$, so we cannot eliminate all the debts.