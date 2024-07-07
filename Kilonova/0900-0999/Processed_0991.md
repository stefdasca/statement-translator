
Once FlaviuS realized that drawing the "intersection of meteors" is a futile task, he discovered that a much more complicated and important occupation is exactly the opposite! He has an attack plan: he knows where to put the pen on the paper, and exactly what the sequence of directions he will follow is (*North*, *East*, *South*, and *West*). His goal is to create a broken line that does not pass through the same point twice, except the final point, which he wants to be exactly the same as the initial one. Additionally, $2$ consecutive moves have different axial orientations (after a vertical one follows a horizontal one and vice versa).

# Task

Given $T$ drawings represented by $N$ and the sequence of $N$ directions, FlaviuS asks you (he doesn't know the solution) to tell him if he can achieve his artistic dream, and if so, how long each segment he draws should be.

# Input data

The first line contains the number $T$ of drawings that FlaviuS wants to successfully complete. Each of the $T$ tests is described by $2$ lines, the first containing the natural number $N$, and the second, a sequence of $N$ characters from the set $\{\texttt{N}, \texttt{E}, \texttt{S}, \texttt{W}\}$.

# Output data

For each test, the first line will display `YES` if the drawing can be accomplished, otherwise `NO`. If it can be accomplished, the second line will contain $N$ non-zero natural numbers which represent the length of the line in each direction.

# Constraints and clarifications

* $1 \leq T \leq 2\ 000\ 000$.
* $1 \leq N \leq 200\ 000$.
* The sum of the values of $N$ in a file will not exceed $2\ 000\ 000$.
* Each value of $N$ is even, and the first character is `E` or `W`.
* Any correct solution in which the lengths are at most $10^9$ is accepted.
* Any solution that does not display, for affirmative responses, $N$ positive numbers less than or equal to $10^9$ will receive $0\%$ of the score for the test.
* **If the existence of a correct solution is determined, but the values in the array do not create a drawing to FlaviuS's liking, $20\%$ of the score for the test will be awarded.**

|# | Score | Constraints|
| - | - | ------------|
|1|15|$1 \leq N \leq 10$ and $1 \leq T \leq 15$.|
|2|35|$1 \leq N \leq 2\ 000$ and the sum of the values of $N$ in a file will not exceed $20\ 000$.|
|3|10|There is at most one value `N` in each sequence.|
|4|40|No additional constraints.|

# Example

`stdin`
```
3
6
ENWNWS
6
ENWNEN
20
ENESENWNENWNWSWSWSES
```

`stdout`
```
YES
4 1 3 3 1 4
NO
YES
2 3 2 3 2 6 3 2 3 1 1 1 4 1 1 2 2 3 2 4
```

## Explanation

**For the first example**, the drawing is depicted in the image below. The blue dot indicates where the masterpiece begins and ends.

~[desen1.png|align=center|width=30%]

**For the second example**, there is no correct solution.

**For the third example**, the following path is not suspicious at all.

~[desen2.png|align=center|width=40%]
