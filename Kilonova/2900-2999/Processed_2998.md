# Task

Lensu is at the other end of the world but wants to reach the Euro 2024 final in Germany. He has $N$ cities along the way and initially starts in city $1$, with the goal of reaching city $N$, specifically the stadium in Berlin. He has $z$ days to reach there to avoid missing the final, and every day he needs to stop in a city to rest. Each city has a cost $v_i$ in lei for lodging, $i \\ (1 \\leq i \\leq N)$, in case Lensu wants to stop at a hotel there. From one day to the next, he can travel a maximum of $k$ cities, meaning if he is in city $x$ on one day, the furthest city he can stay in the next day is city $x+k$.

Every time he stops in a city, Lensu will withdraw **the same** amount of money from the bank to pay for his accommodation, for simplification.

Determine the minimum amount of money he needs to withdraw from the bank each time he stops in a city in order to reach the final on time.

# Input data

The first line of the input file `euro.in` contains the natural numbers $N$, $z$, and $k$.
The next line of the input file `euro.in` contains the $N$ natural numbers $v_i$, separated by a space.

# Output data

The first line of the output file `euro.out` will contain a single natural number, the minimum amount of money Lensu needs to withdraw from the bank each time he stops in a city.

# Constraints and clarifications

* $1 \\leq N \\leq 200 \ 000$;
* $1 \\leq v_i \\leq 1 \ 000 \ 000$;
* $1 \\leq z \\leq N$;
* $1 \\leq k \\leq 200 \ 000$;
* Lensu will necessarily stay in city $1$ and city $N$.
* If Lensu withdraws $x$ money and the lodging costs $y$ money, where $x \\geq y$, then he can stay in the respective city.
* If Lensu withdraws $x$ money and the lodging costs $y$ money, where $x > y$, the remaining money after lodging is not considered.
* If Lensu cannot reach the final, $-1$ will be printed.

|#|Points|Constraints|
|-|-|--------|
|1|40|$1 \\leq v_i \\leq 100$, $1 \\leq N \\leq 1000$, $1 \\leq k \\leq 50$|
|2|30|$1 \\leq k \\leq 50$|
|3|30|Without additional constraints|

# Example 1

`euro.in`
```
10 4 3
1 3 4 2 4 5 3 2 3 1
```

`euro.out`
```
3
```

## Explanation

Lensu stays in 4 different days, in the cities: $1$, $4$, $7$, $10$, the minimum amount of money he needs to withdraw is $3$. ($3 > 1$, $3 > 2$, $3 = 3$, $3 > 1$)
**Note: Lensu could not stay in city $5$ on the second day because $5 - 1 > k$**

# Example 2

`euro.in`
```
15 4 3
1 3 4 3 4 5 3 2 3 1 2 3 4 2 4
```

`euro.out`
```
-1
```

## Explanation

Whatever amount of money Lensu withdraws, he cannot reach the final because he needs to stop too often.

