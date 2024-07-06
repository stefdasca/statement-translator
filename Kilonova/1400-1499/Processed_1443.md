~[s1.jpg|align=right|width=20em] Spy 008 wants to find a secret location in the jungle, with a tracking device. Initially, the spy is at the entrance of the jungle on level $1$, and with each step, he advances from level $i$ to level $i+1$, reaching the secret location located on the last level, at position $u$ from the left edge of the current level. To reach the secret location, he can move one position to the Southeast (coded with the character `E`) or to the Southwest (coded with the character `V`), moving from level $i$ to level $i+1$ at a constant speed. The number of positions on a level increases by $1$ compared to the previous level, as shown in the attached image. We call a route a sequence formed by the characters `E` or `V`, corresponding to the spy's movement from level $1$ to the secret location. For the example in the attached image, the character sequence `VEEVE` represents a route corresponding to the secret location at position $4$ at level $6$.

# Task

Knowing the sequence of characters corresponding to a route, determine:
1) the position of the secret location on the last level;
2) the number of distinct routes that the spy can follow starting from the initial position to reach the secret location corresponding to the given route. Two routes are considered distinct if they differ by at least one position.

# Input data

The input file `spion.in` contains on the first line a natural number $p \in \{1,2\}$, and on the second line a sequence of characters corresponding to a route.

# Output data

If the value of $p$ is $1$, then only point 1 of the task will be solved. In this case, the output file `spion.out` will contain on the first line a natural number representing the position on the final level of the secret location. If the value of $p$ is $2$, then only point 2 of the task will be solved. In this case, the output file `spion.out` will contain on the first line a natural number representing the number of distinct routes modulo $100\ 003$.

# Constraints and clarifications

* $2 \leq$ the length of the step string $<=> 100\ 000$;
* for $20\%$ of the tests, $p=1$;
* for another $10\%$ of the tests, $p=2$ and the length of the character sequence $\leq 255$;
* for another $10\%$ of the tests, $p=2$ and $300 \leq$ the length of the character sequence $\leq 1\ 900$;
* for another $10\%$ of the tests, $p=2$ and $3\ 000 \leq$ the length of the character sequence $\leq 5\ 000$.

# Example 1

`spion.in`
```
1
VEEVE
```

`spion.out`
```
4
```

## Explanation

The secret location is at position $4$ on level $6$.

# Example 2

`spion.in`
```
2
VEV
```

`spion.out`
```
3
```

## Explanation

There are three routes: `VVE`, `VEV`, `EVV`.

# Example 3

`spion.in`
```
2
EVEVVEVEEE
```

`spion.out`
```
210
```