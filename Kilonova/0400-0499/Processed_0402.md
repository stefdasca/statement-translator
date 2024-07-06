After discovering pirate Spânu's hiding place, the sailors on the ship "Speranța" decided to offer the villagers a part of his treasure. Since the treasure consisted of an unlimited number of gold coins, called "galbeni," the only problem for the sailors was the rule by which to distribute the coins.

After long discussions, they proceeded as follows: they asked the villagers to line up in order and come, one by one, to collect their due gold coins. The first villager was asked to choose the number of coins, provided that this number had exactly $K$ digits. The second villager would receive a number of gold coins calculated as follows: the number of gold coins of the first villager is multiplied by all its non-zero digits, the result is multiplied by $8$ and then divided by $9$ keeping only the last $K$ digits of the quotient. If the resulting number has fewer than $K$ digits, the digit $9$ is added to the end until $K$ digits are completed.

To determine how many coins the third villager will receive, the same rule applies, starting from the number of coins of the second villager. The rule continues to apply to each villager, starting from the number of coins received by the villager who stood in line immediately in front of them.

# Task

Knowing the number of gold coins chosen by the first villager, determine the number of gold coins the $N$-th villager will receive.

# Input data
The input file `galbeni.in` contains on the first line the $3$ non-zero natural numbers $S$, $K$, $N$ separated by a space, where $S$ represents the number of gold coins chosen by the first villager, $K$ is the number of digits of the number $S$, and $N$ represents the order number of the villager for which you are required to determine the number of coins received.

# Output data
The output file `galbeni.out` will contain on its only line a natural number representing the determined result.

# Constraints and clarifications
* $2 \leq N \leq 1 \ 000 \ 000 \ 000$;
* $1 \leq K \leq 3$;
* It is guaranteed that $S$ has exactly $K$ digits.

# Example 1

`galbeni.in`
```
51 2 3
```

`galbeni.out`
```
77
```

## Explanation

The first villager took $51$ gold coins. The second villager will receive $26$ coins ($51$ is multiplied by its non-zero digits $51 * 5 * 1 = 255$, $255$ is multiplied by $8$ resulting in $2040$. The quotient of $2040$ divided by $9$ is $226$, the last two digits being $26$).

The third villager will receive $77$ coins ($26$ is multiplied by its non-zero digits $26 * 2 * 6 = 312$, $312$ is multiplied by $8$ resulting in $2496$. The quotient of $2469$ divided by $9$ is $277$, the last two digits being $77$).

# Example 2

`galbeni.in`
```
10 2 3
```

`galbeni.out`
```
96
```

## Explanation

The first villager receives $10$ gold coins. To calculate how many coins the second villager receives, we proceed as follows: multiply $10$ by its non-zero digits: $10 * 1 = 10$, then by $8$, $10 * 8 = 80$. The quotient of $80$ divided by $9$ is $8$. This number having fewer than $K=2$ digits, the digit $9$ is added to its end resulting in $89$.

For the third villager, starting from $89$ ($89 * 8 * 9 = 6408$, $6408 * 8 = 51264$, the quotient of $51264$ divided by $9$ is $5696$, the last two digits are $96$).

