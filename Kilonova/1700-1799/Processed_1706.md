On the road leading towards the entrance to the city, there are $n$ vehicles, of which $m$ are small vehicles, which we will refer to as cars, and the rest are large vehicles, which we will call trucks. The city has a bypass road, popularly known as the _beltway_. Trucks must bypass the city by obligatorily taking the beltway. Cars can either continue on the road leading into the city or take the beltway to bypass the city.

On the beltway, trucks travel at a reduced speed, impeding traffic. Therefore, restriction $R$ has been imposed: no columns composed of more than $k$ consecutive trucks will be admitted on the beltway.

# Task

Given $n$, $k$, and the distribution of vehicles on the road, determine two natural numbers $V$ and $T$, where $V$ represents the number of possible traffic routing variants such that restriction $R$ is respected, and $T$ represents the minimum number of cars that need to be diverted to the beltway to comply with the same restriction $R$.

# Input data

The input file `centura.in` contains on the first line three non-zero natural numbers $n$, $m$, and $k$. On the next line, a string of characters consisting only of the characters `A` and `C`. The character `A` represents a car, and the character `C` represents a truck.

# Output data

The output file `centura.out` will contain the non-zero natural numbers $V$ and $T$ separated by a space, with the meanings given in the task.

# Constraints and clarifications

* $1 \leq k < n \leq 100 \ 000$
* $1 < m \leq 30$
* Note, if initially we have a string of the form `CCAAC` and $k = 2$, then there are two distinct solutions for taking the beltway: `CCAC` (the first `A` goes through the city) and again `CCAC` (the second `A` goes through the city).
* It is guaranteed that for all test data, the initial string of vehicles respects restriction $R$.

# Example 1

`centura.in`
```
8 3 2
CCAACACC
```

`centura.out`
```
3 2
```

## Explanation

The following three variants of separating the initial column of vehicles are possible:
1. through the city: $A_1$; on the beltway: $C_1 C_2 A_2 C_3 A_3 C_4 C_5$
2. through the city: $A_2$; on the beltway: $C_1 C_2 A_1 C_3 A_3 C_4 C_5$
3. through the city: none; on the beltway: $C_1 C_2 A_1 A_2 C_3 A_3 C_4 C_5$ (all)

At least two cars need to be diverted to the beltway. Therefore: $V = 3$ and $T = 2$

# Example 2

`centura.in`
```
7 2 2
CCACCAC
```

`centura.out`
```
1 2
```

## Explanation

There is only one variant: all vehicles will be diverted to the beltway: $C_1 C_2 A_1 C_3 C_4 A_2 C_5$ Therefore: $V = 1$ and $T = 2$

