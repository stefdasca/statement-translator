After the brilliant victory at Austerlitz against the Russo-Austrian coalition, Emperor Napoleon Bonaparte wants to reward $N$ generals who distinguished themselves in battle. For this, he has a sum of franc value $S$. At the festivities dedicated to the victory, the $N$ generals will be lined up in decreasing order of their merits on the battlefield, and the Emperor will call them for awarding the reward in this order.

Bonaparte wants to distribute the entire sum such that the most meritorious general receives the largest sum, and any other general receives an amount at most equal to the general who was rewarded before them. Additionally, the general with the smallest reward must not receive less than $F$ francs.

# Task

Determine the number of distinct ways of awarding the rewards by Emperor Napoleon.

# Input data

The input file `rec.in` contains three natural numbers $S$, $N$, and $F$, separated by a single space, as specified in the statement.

# Output data

The output file `rec.out` will contain a single natural number, representing the number of distinct reward distributions.

# Constraints and clarifications

* $2 \leq F \leq S \leq 400$
* $1 \leq N \leq 50$
* For $20\%$ of tests $S \leq 80$
* For $80\%$ of tests $S \leq 150$

# Example

`rec.in`
```
9 3 2
```

`rec.out`
```
3
```

## Explanation

The sums can be awarded in the following ways:

```
5 2 2
4 3 2
3 3 3
```

The smallest sum paid to a general is $2$.