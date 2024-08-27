## Task

Astro and Buru are out of ideas. They need to quickly find problems for the final round of the preONI competition. Since they have no idea, they decide to buy a magic lamp. However, after buying it, they realize that the lamp is actually an ordinary lamp, not a magical one. Frustrated, the two start playing the following game: Buru writes a word consisting of lowercase English letters on a piece of paper. Astro also writes another word. The two will alternately write words on the paper, and the word written at each step starting from the $3^{rd}$ will be the concatenation of the previous two words. At some point, Buru stops after $N$ words have been written on the paper and asks Astro: "What were the two starting words?" Since they have written so many words, they forgot the initial words. Given $N$ and the $N^{th}$ word on the paper, determine the two initial words. If there are multiple possible solutions, display the one in which the first word is lexicographically minimal. If there is no solution, display the number $0$.

## Input data

The input file `lampa.in` contains on the first line the numbers $N$ and $M$, where $N$ is the ordinal number of the given word and $M$ is its length. The second line will contain $M$ characters representing the $N^{th}$ word on the paper.

## Output data

The output file `lampa.out` will contain on the first line the first word on the paper (the one written by Buru). The second line will contain the second word on the paper (the one written by Astro). If there is no solution, the output file will contain only one line with the number $0$.

## Constraints and clarifications

During the correction, $10$ tests will be used. They will have the following values for $N$ and $M$:
$T1$ \
$T2$ \
$T3$ \
$T4$ \
$T5$ \
$T6$ \
$T7$ \
$T8$ \
$T9$ \
$T10$ \
$8$ $523$ \
$8$ $4200$ \
$10$ $5001$ \
$9$ $8910$ \
$7$ $46189$ \
$6$ $88600$ \
$25$ $346468$ \
$14$ $590005$ \
$15$ $1010860$ \
$17$ $3027197$ 

The two initial words must have non-zero length.

## Example

`lampa.in`
```
5 22
astroburuburuastroburu
```

`lampa.out`
```
astro
buru
```

## Explanation

The words written on the paper are: `astro`, `buru`, `astroburu`, `buruastroburu`, `astroburuburuastroburu`.