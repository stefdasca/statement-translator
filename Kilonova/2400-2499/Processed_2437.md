Here is the translated statement:

---

You and your desk mate took a break at Vila Elena, where you bought two bags of chips. At the end of the break, there are $A$ chips left in your bag, and $B$ chips left in your mate's bag.

You challenge your mate to a game: as long as no bag is empty, you and your desk mate take turns to take chips from the fuller bag (if both bags have the same number of chips left, you can choose which bag to take from). The rule is that the number of chips taken must be a non-zero multiple of the number of chips remaining in the other bag.

For example, if it is your turn and the two bags have $3$ and $11$ chips left respectively, you can take $3$, $6$, or $9$ chips from the bag with $11$ chips.

Whoever empties a bag first can eat what remains in the other one, thus winning the game.

# Task

If you go first and your mate plays optimally, will you win the game? You have $3$ game situations to determine if you win or not.

# Input data

The first three lines of the input file `chipsuri.in` each contain two natural numbers $A$ and $B$, representing the number of chips in your bag and your desk mate's bag, respectively, for the current situation.

# Output data

The output file `chipsuri.out` will contain 3 messages representing the answer to the 3 situations, each on a new line: `YES`, if you win the game situation, or `NO`, if you may lose it.

# Constraints and clarifications

* $1 \leq A, B \leq 1\ 000\ 000\ 000\ 000\ 000\ 000$.

# Example

`chipsuri.in`
```
9 3
4 3
11 2
```

`chipsuri.out`
```
YES
NO
YES
```

## Explanation

Situation $1$: You can empty the first bag directly.  
Situation $2$: You have only one possibility: take $3$ chips from the larger bag. This leaves one bag with $3$ chips and one bag with $1$ chip. Your mate can then empty the first bag.  
Situation $3$: You can take $8$ chips from the bag. Your mate will have a bag with $2$ chips and one with $3$, from which they will be forced to take $2$ chips. On your turn, you will have a bag with $2$ chips and one with $1$, thus you will obviously win the game.  

---

I have double-checked the statement for any grammar and/or syntax errors and made sure to follow the specified instructions accurately.