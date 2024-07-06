Gigel is a big fan of the music from the 70s. He has an impressive collection of magnetic tapes with songs composed during that period. The technique used in that period might seem rudimentary nowadays, but Gigel wants to recreate as much of the era's atmosphere as possible. 
Each song is recorded on a magnetic tape; the tapes are numbered from $1$ to $N$. Each tape is wound on a plastic reel, and Gigel also has an empty reel. The reels are numbered from $0$ to $N$, each tape having its place on the reel with the same number, and reel $0$ being the empty reel. 
When Gigel listens to a song, the tape recorder unwinds the tape from its reel and winds it onto the empty reel; in the end, the tape is found on the reel that was initially empty, wound in reverse so that the start of the tape is in the center of the reel, and the reel on which the tape was initially becomes empty. Gigel always ensures that, after listening to a song, he rewinds the tape back onto its reel. Gigel's younger brother is more disorganized and often leaves the tape on the reel it reaches after listening to it. He then uses the freshly freed reel as an empty reel to listen to the next song. Thus, after a while, many tapes are found on a different reel than their own, and some tapes are wound in reverse, meaning the start of the song is inside the winding (needing to be rewound before it can be listened to). 
Gigel now wants to restore order, bringing each tape to its reel and wound with the start on the outside. For this purpose, he can perform a sequence of operations. In one operation, he can only take a reel and unwind the tape from it onto the single reel that is empty at that moment, the tape reversing its winding direction in the process.

# Task

Determine a minimal sequence of operations after which each tape reaches the reel whose number matches the tape number and wound with the start on the outside.

# Input data

The input file `role.in` will contain on the first line a natural number $N$ representing the number of tapes. On the next $N$ lines there are two natural numbers separated by a space, $R$ and $I$. The k-th pair describes the position of the tape with number $k$: $R$ represents the number of the reel on which tape $k$ is found, and $I$ has the value $0$ if the tape is wound normally (with the start on the outside) and $1$ if it is wound in reverse.

# Output data

The output file `role.out` will contain a sequence of natural numbers, one number per line. The number on line $i$ represents the number of the reel from which the tape is moved to the empty reel at the $i$-th operation performed.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* There can be at most one tape on a reel at any moment.
* For all test data, there will exist a solution requiring at least one operation.
* **Score**. For the optimal solution, $100\%$ of the score is awarded.
* If the solution is not optimal but correct, partial scores will be awarded as follows:
    * if the difference between the number of operations performed by the contestant and the optimal number of operations is less than or equal to $10\%$ of the optimal number (whole part), $60\%$ of the score is awarded;
    * if the difference between the number of operations performed by the contestant and the optimal number of operations is greater than $10\%$ of the optimal number (whole part), $20\%$ of the score is awarded.

# Example 1

`role.in`
```
2
1 0
0 1
```

`role.out`
```
0
```

# Example 2

`role.in`
```
3
2 0
0 1
3 1
```

`role.out`
```
3
2
1
3
2
0
```