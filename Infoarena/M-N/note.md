## Task

A musical score is written for $V$ voices, each voice having $N$ notes. We say that a solfeggio overlays this score if the solfeggio also has a length of $N$ notes and each note of the solfeggio matches the note at the corresponding position of the score, in at least one of the voices. For example, the solfeggio mi re la do si fa sol la overlays the score with 2 voices and 8 notes mi re do do si fa fa si sol si la do sol mi sol la, because the notes 1, 2, 5, and 6 of the solfeggio are sung according to the first voice, while the notes 3, 7, and 8 are sung according to the second voice. It is noted that the fourth note (do) is sung according to both voices. We say that a solfeggio of an arbitrary length mismatches in $K$ places if exactly $K$ modifications are needed to make it overlay the score. A modification can be:
1) Deleting a note from the solfeggio
2) Adding a note to the solfeggio
3) Replacing a note in the solfeggio

For example, the solfeggio mi re sol do si fa si mismatches in two places, because we need to replace the note sol with la and insert another fa between si and fa to bring it to the form: mi re la do si fa fa si which overlays the score.

## Task

Determine if a given solfeggio overlays a given score, or, otherwise, what is the minimum number of places it mismatches. The notes will be represented by numbers from 1 to 100.

## Input data

The input file `note.in` will have the following structure:
- The first line will contain $V$ and $N$, separated by exactly one space, the number of voices and the number of notes.
- The next $V$ lines contain $N$ numbers each, symbolizing the score with $V$ voices and $N$ notes on each voice. The numbers will be natural and between 1 and 100.
- The line $V+2$ will contain the number $M$ of notes in the solfeggio.
- The line $V+3$ will contain $M$ natural numbers within the interval $[1, 100]$, representing the notes of the solfeggio.

## Output data

The output file `note.out` will contain the minimum number of places where the solfeggio mismatches, depending on the given score. If the solfeggio overlays the score, the number displayed will be 0.

## Constraints

$1 \leq V \leq 512$

$1 \leq M$, $N \leq 1024$

## Example

`note.in`
```
2 8
3 2 1 1 7 4 4 7
5 7 6 1 5 3 5 6
7
3 2 5 1 7 4 7
```

`note.out`
```
2
```

## Explanation

The 3rd note of the solfeggio will be replaced with 1 or 6, and between the last two notes, one of the notes 4 or 5 will be added.