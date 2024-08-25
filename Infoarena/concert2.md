# Concert2

Michael is a big fan of Parazitii, so he is participating in a contest where he has to compose the beat of a song for the band's new album. Contestants have to choose from a list of notes, whose frequencies are known, and the winner receives two free tickets to the band's next concert. Since many can compose beats, to differentiate between novices and the experienced ones, the composed beat must have the following properties:
- The notes must be chosen in the order they appear on the list
- Any two consecutive chosen notes must be distinct
- The beat must not contain a subsequence of $K_1 + 1$ notes whose frequencies are increasing
- The beat must not contain a subsequence of $K_2 + 1$ notes whose frequencies are decreasing

The winner of the contest is the one with the longest beat.

## Task

Given $N$, $K_1$, and $K_2$, help Michael win two tickets to the concert for him and his best friend.

## Input data

The input file `concert2.in` contains on the first line the values $N$, $K_1$, and $K_2$. The second line contains $N$ natural numbers indicating the frequencies of the notes.

## Output data

The output file `concert2.out` will contain a single natural number representing the maximum length of the beat.

## Constraints and clarifications

$1 \leq N \leq 2500$

$1 \leq K_1 \leq 300$

$1 \leq K_2 \leq 300$

$1 \leq$ frequencies of the notes $< 2^{31}$

## Example

`concert2.in`

```
8 2 3
1 3 2 1 6 8 9 7 6
```

`concert2.out`

```
7
```

## Explanation

The notes with frequencies $1 3 2 1 9 7$ can be chosen