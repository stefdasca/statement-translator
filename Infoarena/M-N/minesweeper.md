# Minesweeper

One day, the great computer scientist Gigel is visited by his 2-year-old cousin. Not knowing how to entertain him, Gigel decides to let his cousin play minesweeper. The game consists of a $N$ x $M$ grid that is initially empty. On the first press, a square becomes a flag, on the second it turns into a question mark, and on the third press, it returns to its initial form. Gigel knows that his cousin will stop when the whole grid is filled with question marks (as he finds such a grid boring). However, since the cousin is so young, he doesn't realize he can press each square up to two times. Instead, he presses a random square every second. The great computer scientist is too busy with his own difficult problems, so he asks you to tell him approximately how long it will take for his cousin to get bored (i.e., obtain the entire grid with question marks).

## Task

Determine the average time it will take to transform the entire grid into one with question marks by pressing randomly.

## Input data

The input file `minesweeper.in` will contain 2 numbers $N,M$ with the significance described above.

## Output data

The output file `minesweeper.out` will contain a single real number with 6 decimal places representing the average number of presses needed for all squares to turn into question marks.

## Constraints and clarifications

$$1 \leq N \times M \leq 22$$

Although the original game has a different purpose, his younger cousin cannot solve it, so Gigel tricks him into thinking this is how you play minesweeper.

The answer is considered correct if the absolute difference between your result and the correct result is at most a thousandth of the correct result. In other words, if your result is $x$ and the correct result is $y$, then if $|x - y| \leq y / 1000$, the result is considered correct.

`minesweeper.in`:

```
1 3
```

`minesweeper.out`:

```
28.928571
```