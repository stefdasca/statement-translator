After qualifying for the European Football Championship in France and considering `N` players from which he must call up some for the national team, the Romanian coach resorted to some unconventional methods. He went to the renowned witches in Craiova to help him find the winning formula for the opening match against France. The witches, after prolonged chants, concluded that the squad must have an exact value of `X` and the arrogance coefficient as small as possible. **The value of a squad** of players is defined as the sum of the values of the players in the squad. **The arrogance coefficient** of a squad of players is defined as the difference between the maximum value of a player in the squad and the minimum value of a player in the squad. It is also known that the value of the squad cannot exceed a known value `Vmax`. A **squad of players** is defined as a non-empty subset of players chosen from the `N`. Note that a squad can also consist of a single player.

# Task
Given the number `N` of players, the number `Vmax` as defined above, and the value of each player. The Romanian coach found the winning formula and is curious if you can too. Since he does not fully trust the witches, he asks you to find, for each value `X` in the range `[1,Vmax]`, the minimum possible arrogance coefficient for which there is at least one squad among the `N` players with the exact value `X`. If no squad can be obtained with the exact value `X`, the answer is considered `-1`.

# Input data
The input file `euro.in` contains the first line `T`, representing the number of tests. Next, there will follow `T` tests, each having the following structure: the first line of a test contains `N` and `Vmax`, representing the total number of players and the maximum value that a squad can have, respectively. The second line of the test contains `N` natural numbers separated by a space. The `i`-th number on this line represents the value of the `i`-th player.

# Output data
The output file `euro.out` will contain `T` lines, one for each test in the input file. A line corresponding to a test contains `Vmax` numbers (the `Vmax` of the current test), where the `i`-th number represents the minimum possible arrogance coefficient for a subset of players with an exact value of `i`. If there is no subset of players with the exact value, print `-1`.

# Constraints and clarifications
* `1 \leq T \leq 2`
* `1 \leq N \leq 4000`
* `1 \leq Vmax \leq 8000`
* `1 \leq valoare[i] \leq Vmax`
* For `20%` of the tests `N \leq 20`
* For `40%` of the tests `N \leq 100` and `Vmax \leq 100`
* For `50%` of the tests `N \leq 300` and `Vmax \leq 300`

# Example

`euro.in`
```
2
4 7
5 2 3 4
5 15
1 8 2 3 6
```

`euro.out`
```
-1 0 0 0 0 2 1
0 0 0 2 1 0 5 0 3 5 4 5 6 2 7
```

Explanation
---

For the first test:
* A squad with the value `1` cannot be found, so the answer for `1` is `-1`.
* Squads with values `2, 3, 4, 5` can be obtained from a single player.
* The squad with value `6` can be obtained from players with values `2` and `4`.
* For the value `7`, there are two possible squads formed from players with the values `5 2` respectively `3 4`. The latter squad has a lower arrogance coefficient (i.e. `max(3,4)-min(3,4)=1`).