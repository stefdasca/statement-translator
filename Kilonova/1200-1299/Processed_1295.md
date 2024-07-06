```markdown
Viorel received a strategy game from his parents. The hero of the game has an initial level $n$ and must complete certain missions. The hero $i$ is allowed access to a mission only if his level is at least equal to the minimum level required by it, and after each completed mission, his level increases to a certain value, specific to that mission.  
After completing a mission, Viorel chooses another mission for his hero, under the mentioned conditions.  
Because his parents do not let him play too much, Viorel must choose the $\\underline{\\text{minimum number of missions}}$, and his dream is to reach a $\\underline{\\text{level at least equal to} \\ m}$.

# Task

Determine the level reached by the hero after completing the chosen missions and their number.

# Input data

The input file `joc.in` contains:
* The first line contains three natural numbers: $n$ (the initial level of the hero), $k$ (the number of available missions), and $m$ (the minimum level required to finish the game) separated by a space
* Each of the following $k$ lines corresponds to a mission and contains two positive values, separated by a space, representing the minimum level required to start the mission, and the level acquired by the hero at the completion of the respective mission.

# Output data

The output file `joc.out` contains a single line which will print the hero's level and the minimum number of chosen missions, separated by a space.

# Constraints and clarifications

* $0 \\lt n, m \\leq 2 \\ 000 \\ 000 \\ 000$
* $2 \\lt k \\leq 5 \\ 000$
* It is considered that at least one level is accessible to the hero!

# Example 1

`joc.in`
```
6 10 25
1 3
2 3
1 2
2 6
3 9
2 10
5 8
10 17
15 27
17 24
```

`joc.out`
```
27 3
```

## Explanation

Viorel chooses for his level 6 hero the following missions: $(2, 10), (10, 17)$ and $(15, 27)$, so at the end his hero has level 27, the minimum required to win the game.

# Example 2

`joc.in`
```
3 5 100
1 2
2 9
7 19
29 80
77 190
```

`joc.out`
```
19 2
```

## Explanation

Viorel chooses for his hero 2 missions and reaches level 19. The chosen missions are: $(2, 9)$ and $(7, 19)$.

# Example 3

`joc.in`
```
5 4 20
1 3
9 20
2 10
19 44
```

`joc.out`
```
20 2
```

## Explanation

Viorel chooses for his hero 2 missions and reaches level 20. The chosen missions are: $(2, 10)$ and $(9, 20)$.
```

I have translated the document accordingly and ensured correct grammar and syntax in English.