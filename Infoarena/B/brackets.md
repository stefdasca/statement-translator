## Task

You were in your room, minding your own business, working on the persistent Trie documentation for the ACM Finals. Suddenly, someone knocks on the door. Your neighbor next door asks to borrow two correct bracket sequences because he has some friends visiting and wants to play a game. Since he doesn't think very highly of you, he offers you a recursive definition of the correctness of a bracket sequence, hoping you can follow it:
- The empty sequence is correct.
- If the sequence $A$ is correct, then the sequence $(A)$ is also correct.
- If the sequences $A$ and $B$ are correct, then the sequence $A$ concatenated with $B$ is correct.

You look around the room and see a treap broken in half under the table, an FFT with a constant of a million etched on the mirror, and finally, a bracket sequence left in a pizza box. You decide to partition your bracket sequence (which is not necessarily correct) into exactly two subsequences of approximately equal length (apparently important for the neighbor's dubious game) so that both are correct bracket sequences. You want to get rid of these brackets entirely, so you won't leave any in the pizza box.

## Input data

The input file `brackets.in` will contain on its first line $T$, the number of tests. The structure of a test is as follows: the first line contains a number $N$, representing the number of brackets in the sequence. The next line contains a bracket sequence of length $N$.

## Output data

The output file `brackets.out` will contain multiple lines, representing the answers to the corresponding tests. If it is not possible to partition the input sequence into two correct bracket subsequences, you will print "-1". Otherwise, you will print the number of brackets in the first subsequence, followed by the indices of this subsequence. Then, you will print the number of brackets in the second subsequence, followed by the indices of this subsequence. Indices are numbered from $1$ to $N$. The intersection of the two sets of indices must be empty, and the union of the two sets must be equal to $\{1, 2, \dots, N\}$. Both sets of indices must be printed in ascending order.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq N \leq 10\ 000$

If there are multiple solutions, you will happily accept any of them.

## Example

`brackets.in`

```
2
8
((())())
6
()()))
```

`brackets.out`

```
4 1 3 5 8 4 2 4 6 7
-1
```

~[name.png]
