# Trompeta

Victor, the farmer, bored of listening to so much rock music, has found a new passion: jazz. Thus, he got a haircut, dyed his hair black, and then got himself a trumpet. To demonstrate his musical skills, he decided to hold a live concert. Unfortunately, other activities consumed part of his practice time, and now he is no longer capable of performing the entire concert. More precisely, out of the initial $N$ notes, he can only play $M$, as he tires and starts making mistakes afterward. Each note is represented by a value in the range $[0 \dots 9]$ which indicates the pleasure it produces to the audience when played. The total pleasure of a concert is equal to concatenating the played notes viewed as a number in base $10$. Victor thought it would be best to select the notes in such a way that the concert is as pleasing as possible for the audience, to appear more skilled than he actually is.

## Task

Given the $N$ initial notes, find the dream concert for the farmer.

## Input data

The file `trompeta.in` contains the numbers $N$ and $M$ on the first line. The next line contains the values corresponding to the $N$ notes.

## Output data

The file `trompeta.out` contains $M$ digits on the first line, representing the concert that will be played.

## Constraints and clarifications

$1 \leq N \leq 1000000$

$1 \leq M \leq N$

The notes in the chosen concert must be in the initial order to maintain the harmony of the concert.

## Example

`trompeta.in`

```
5 4
19990
```

`trompeta.out`

```
9990
```