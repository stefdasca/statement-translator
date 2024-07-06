Gigel discovers that he is a big football fan and a true supporter of the Juventus Torino team. He watched a match between Juventus Torino and AC Milan and wrote down on a sheet the $N$ goals in the order they were scored. For each goal scored by Juventus, he wrote down the digit $1$, and for each goal scored by Milan, he wrote down the digit $2$.

**The score of the match**, at any given moment, is expressed by two numbers: the first representing the total number of goals scored up to that point by the first team, Juventus Torino, and the second representing the total number of goals scored up to that point by the second team, AC Milan.

**The score is tied** if the two numbers are equal, and a team **leads** the opposing team if the number of goals scored by it is strictly greater than those scored by the opposing team.

**The final score** is the one obtained at the end of the game.

We say that **strong comeback** is a situation where a team, *which is behind*, scores enough goals *to take the lead*, without the opposing team scoring any goals during this time.

# Task

1. Determine the final score.
2. Determine the number of tied scores recorded throughout the game, starting with the initial score. The initial score, $0 - 0$, is considered tied.
3. Determine the number of goals corresponding to the greatest comeback in the game (the maximum number of consecutive goals scored by a team during a comeback).

# Input data

The input file `microbist.in` contains on the first line two natural numbers $C$ and $N$ separated by a space. $C$ represents the task to be solved, and $N$ is the number of goals scored. The next line contains, separated by a space, $N$ values representing the goals scored, as described above.

# Output data

The first line of the output file `microbist.out` will contain:

* for $C = 1$, two natural numbers separated by a space, representing, in this order, the number of goals scored by Juventus Torino and the number of goals scored by AC Milan;
* for $C = 2$, the required number of tied scores;
* for $C = 3$, the required maximum number of goals.

# Constraints and clarifications

* $1 \le C \le 3$
* $1 \le N \le 100\ 000$
* It is guaranteed that for all test data corresponding to task $3$, there is at least one strong comeback

|# | Score | Constraints|
| - | - | ------------|
|1|21|$C = 1$|
|2|24|$C = 2$|
|3|55|$C = 3$|

# Example 1

`microbist.in`
```
1 5
1 2 1 2 2
```

`microbist.out`
```
2 3
```

## Explanation

Solving task $C = 1$, and $N = 5$ goals were scored. The final score is $2 - 3$.

# Example 2

`microbist.in`
```
2 5
1 1 2 2 2
```

`microbist.out`
```
2
```

## Explanation

Solving task $C = 2$, and $N = 5$ goals were scored. The scores recorded during the game were, in this order: $0 - 0, 1 - 0, 2 - 0, 2 - 1, 2 - 2, 2 - 3$.

Of these, two were tied: $0 - 0$ and $2 - 2$.

# Example 3

`microbist.in`
```
3 6
1 1 2 2 2 2
```

`microbist.out`
```
3
```

## Explanation

Solving task $C = 3$, and $N = 6$ goals were scored. The greatest comeback occurred when AC Milan was behind $2 - 0$ and then scored three consecutive goals, taking the lead at that moment, making the score $2 - 3$.

# Example 4

`microbist.in`
```
3 11
1 2 2 2 1 1 1 1 2 1 1
```

`microbist.out`
```
3
```

## Explanation

Solving task $C = 3$, and $N = 11$ goals were scored. The greatest comeback was when Juventus was behind $1 - 3$ and then made a strong comeback by scoring three consecutive goals and taking the lead with $4 - 3$.