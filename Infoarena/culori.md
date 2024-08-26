## Colors

Alice and Bob, two renowned mountain climbers who have just finished their exams, decided to spend their vacation in the heart of the mountains. One day, while exploring the nearby forests, they discovered a cave that they presumed once belonged to a colony of monkeys. According to their knowledge in the field, the cave consists of $N$ chambers connected by bidirectional corridors such that there is a single path between any two chambers. Moreover, the walls of each chamber were painted by the monkeys in a color denoted by an integer between 1 and $N$. Our adventurers want to reconstruct the map of the cave. To do this, they proceed as follows: initially, Bob is in chamber $ \#1$ with his left hand touching the wall at every step. Bob notes the color of the chamber he is in, then - without taking his left hand off the wall - enters a new chamber (which may have been visited before). Bob stops when he returns to chamber $ \#1$ and all $N$ chambers have been visited. Alice notices that, unfortunately, based only on the sequence of colors noted by Bob, the cave map cannot always be reconstructed. Therefore, she asks you to find out how many possible maps can be drawn based on the collected data.

## Input data

The first line of the input file contains the integer number $N$. The second line contains the sequence of $2 * N - 1$ colors in the order they were noted by Bob.

## Output data

The first line of the output file will contain the number of possible maps modulo $9901$.

## Constraints and clarifications

$1 \leq N \leq 256$

## Examples

`culori.in`
```
3
3 1 3 1 3
```

`culori.out`
```
2
```

`culori.in`
```
2
2 2 1
```

`culori.out`
```
0
```

## Explanation

In the drawing, we observe the two possible maps for the first example, with Bob's route marked with blue arrows. By traversing either of the two caves according to Bob's algorithm (starting from chamber $ \#1$ marked in red in the drawing), we obtain the color sequence $3 1 3 1 3$.