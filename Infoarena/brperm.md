## Task

Note: In the statement, $b_1 \dots b_K$ represents an integer written in binary notation, where $b_1$ is the most significant bit and $b_K$ is the least significant bit. The witch Roxana, while flying on her broomstick through the galaxy, discovered a new planet (the BR-PERM planet) where all the inhabitants were involved in a strange dance. In this dance, participants stand in a line and then reorder themselves. In a dance with $2^K$ participants, the person in position $b_1 \dots b_K$ will move to position $b_K \dots b_1$ (indexed from 0). Roxana realized that every person on BR-PERM wears clothing of one of 26 colors. These colors will be represented by letters of the Latin alphabet. BR-PERM inhabitants consider the sequences of dancers where the color sequence that the inhabitants wear before and after the dance is the same to be special. They call such sequences "cute." For example, when $K=2$, we have a sequence of 4 dancers 0, 1, 2, 3, which after the dance will be ordered as follows: 0, 2, 1, 3. Thus, the color sequence $abba$ is cute, but $abca$ is not. BR-PERM inhabitants ask Roxana to help them with this problem (it seems that witches always help people solve their problems). They show her a sequence of $n$ dancers and ask her to answer several questions: "Is the sequence of length $2^K$ starting at dancer $P$ cute?"

## Input data

The input file "brperm.in" contains, on the first line, the number $N$. The next line contains a string of characters (lowercase letters of the Latin alphabet) of length $N$. The following line contains the number of questions $Q$, and on the next $Q$ lines are two numbers each $P, K$.

## Output data

The output file "brperm.out" contains the answers to the $Q$ questions (1 if the given sequence is cute, 0 if it is not), in order, each on a new line.

## Constraints and clarifications

$1 \leq N \leq 500000$

$1 \leq Q \leq 500000$

For 20 points, $1 \leq N \leq 1000$ and $1 \leq Q \leq 1000$

For another 30 points, $1 \leq N \leq 100000$ and $1 \leq Q \leq 100000$

For another 20 points, $s$ contains only the characters 'a' and 'b', and the colors are chosen randomly independent with a certain fixed probability for each test.

## Example

brperm.in

`8`

`axxyxxyb`

`4`

`0 3`

`1 1`

`1 2`

`3 2`

brperm.out

`1`

`1`

`0`

`1`