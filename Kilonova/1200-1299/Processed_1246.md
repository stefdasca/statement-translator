Mihăiță and Andrei meet on the basketball court to settle an old dispute. They take turns shooting the ball into the basket. Each contestant shoots until they miss, then it's the other's turn, and so on. They keep track of the shots in the following way:
- If Mihăiță scores, they write the digit $1$ on the score sheet.
- If Andrei scores, they write the digit $2$ on the score sheet.
- Each miss is marked with the digit $0$.

The two play until one of them gets tired and quits, even if one of them cheats and shoots when it's not his turn. By checking the score sheet, it must be determined if any of them cheated, in which case the message **error** is displayed and the program execution stops. If the game was played correctly, the scores of the two are calculated based on the following rules:
- If one of them scores, he gets $10$ points and the other loses two points.
- If one of them misses, he loses three points.
- Whoever quits the game loses $10$ points.

The two contestants play $n$ games, each game is tracked on a score sheet.

# Task

For each of the $n$ score sheets, check if any of them cheated by shooting when it was not their turn. In this case, the message **error** will be displayed, otherwise, the score achieved by the two contestants will be displayed.

# Input data

From the file `baschet.in`, the following are read: the first line contains the natural number $n$, and the following $n$ lines contain a score sheet where the digits are written one after the other, without separator spaces.

# Output data

In the file `baschet.out`, for each score sheet, a line is recorded with the content: **error**, if one of the contestants cheated, or the corresponding score (two integers separated by a space, the first being the score achieved by Mihăiță).

# Constraints and clarifications

* $0 < n \leq 10$
* Each score sheet contains at most $255$ digits.
* The game is started by Mihăiță.
* Every time a player cheats, he will not miss, regardless of whether it is Mihăiță or Andrei.
* Partial scores are not awarded.

# Example

`baschet.in`
```
2
11020022102 
102201022201102
```

`baschet.out`
```
error
19 36
```

## Explanation

Two games were contested.
In the first game, Mihăiță cheated: $1 \ 1 \ 0 \ 2 \ 0 \ 0 \ 2 \ 2 \ 1 \ 0 \ 2 \ \textcolor{red}{1} \ 0 \ 2$ 
The second game was played correctly; Andrei quit and the score is as shown.