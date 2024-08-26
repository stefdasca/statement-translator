Weeee

Little $B$ is about to say his first word. His mother keeps repeating "Come on, $B$, I know your first word will be mommy". His father believes that his first word will be "Daddy". When $B$ finally speaks, he just says: $WEEEEEEEEEEE$. Both parents are disappointed with him, so they decide to stop talking to him. Upset, $B$ goes to his play area. He has blocks with a letter written on each. Upset, he throws away all the blocks which have letters other than $W$ and $E$. He then arranges the blocks in a line. The goal of his game is to form the longest possible word from the remaining blocks (the ones that contain the letters $W$ or $E$). Unfortunately, he knows only one word: a word that starts with the letter $W$ and is then formed only from $E$s. He wants to form the word with the maximum possible length. Thus, his goal is to form a subarray of blocks that starts with $W$ and then contains all the $E$s from the blocks. The only operation allowed in his game is to swap 2 adjacent blocks. Find the minimum number of swaps such that there exists a subarray of blocks which starts with $W$ and then contains all the $E$s, or little $B$ will start crying :(

## Input data

The input file `weeee.in` will contain on the first line the number $N$, representing the length of the block array. The second line of the file contains the array of blocks, viewed from left to right. Each of the $N$ blocks will have the letter $W$ or $E$, corresponding to the letter written on that block.

## Output data

The output file `weeee.out` will contain a single number, representing the minimum number of swaps such that there exists a subarray which starts with $W$ and contains all the $E$s of the initial array. For the subarray to be a valid word, it must contain one $W$ and at least one $E$. If no such subarray can be formed, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$

Read carefully what is written in "## Output data", to avoid an $\#MLC$ later!

The problem name contains exactly $4$ characters "e". Meanwhile, little $B$ has grown up, but he still likes the word $WEEEEEE$

## Example

`weeee.in`
```
7
WEEEEWE
```
`weeee.out`
```
1
```

## Explanation

We will swap the penultimate and the last block. Now, the subarray which starts from position $1$ and has length $6$ will start with the letter $W$ and will contain all the $E$s of the initial array. This will bring happiness to little $B$.