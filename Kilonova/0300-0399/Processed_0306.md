On a table, there are chocolate bars. Each chocolate bar consists of at least `2` and at most `16` tablets.

Two girls – `A` and `B`, play a game in which each alternatively makes a move, with `A` making the first move. The girl whose turn it is must choose one of the remaining bars on the table and use one of the following options:
a. If the bar has two tablets, she breaks it into two tablets and eats them.
b. If the bar has at least three tablets, she breaks off one tablet from an end, eats it, and leaves the remaining bar on the table.
c. If the bar has at least four tablets, she breaks it into two bars of at least two tablets each and leaves the two bars on the table without eating anything.

The table below explains the moves that can be applied to bars of `2, 3, 4`, and `5` tablets, with the tablets to be eaten in the corresponding move being bolded. 

~[ciocolata.png]

The game ends when there is no more chocolate on the table. The goal of the game is for each girl to eat as little chocolate as possible (the girls do not want to gain weight). It is known that the two contestants are extremely intelligent, so each plays optimally.

# Task
For `t` game configurations where the numbers of bars of each type are known, determine the number of tablets eaten by each girl at the end of the game.

# Input data
The input file `ciocolata.in` contains on the first line a natural number `t` – representing the number of game configurations for which the response must be found. The next `t` lines describe one configuration of a game. Each of these lines contains `15` natural numbers - separated by a space - $c_2, c_3, c_4, \ldots, c_{16}$ representing the number of bars of `2, 3, 4, ..., 16` tablets on the table at the beginning of the game.

# Output data
The output file `ciocolata.out` will contain `t` lines describing the result of the `t` configurations from the input file. On each of these lines, `two` natural numbers `x` and `y` will be written separated by space, `x` - representing the number of tablets eaten by `A` and `y` - the number of tablets eaten by `B` in the corresponding game from the input file.

# Constraints
* `1 \leq t \leq 30 002`
* For `30%` of the tests, for each of the `t` configurations, there will be only bars of size `2, 3, 4`, or `5`.
* For each of the `t` configurations, the number of bars of each type is a natural number and does not exceed `30 002`.

# Example
`ciocolata.in`
```
1
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0	
```

`ciocolata.out`
```
3 2
```

Explanation
---

On the table, we have a bar of `2` and one of `3`.
`A` breaks the bar of `3` and eats `1`.
`B` breaks one of the remaining bars of `2` and eats `2`.
`A` breaks the remaining bar of `2`, eats `2`, and the game ends.

Another possibility would have been:
`A` breaks the bar of `2` and eats `2`.
`B` breaks the remaining bar of `3` and eats `1`.
`A` breaks the remaining bar of `2`, eats `2`, and the game ends.
This variant is incorrect because `A` did not play optimally.