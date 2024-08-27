# Trap

Perry has arrived at Doofenshmirtz's to prevent him from destroying the entire world with his new inator. However, once he enters through the door he has a surprise: instead of the usual large room, he finds himself in a hallway with the floor covered with $N$ tiles lined up, numbered from $1$ to $N$, with him standing at the entrance, right behind tile $1$. Doofenshmirtz's assistant robot, Norm, then tells Agent P: "You are in the latest anti-platypus trap. All you need to do to escape is reach the end of the hallway and pass tile $N$. However, there are bombs under $K$ of the tiles. We would have put one under every tile, but the budget did not allow it, so if you step on a tile that has a bomb under it, you will die instantly. Good luck escaping this time!" As always, Perry is prepared. He has a device where he can enter, several times, a triplet $(c, a, b)$, and the device will return $1$ if in the sequences of tiles of length $c$ that start at $a$ and $b$ respectively, there is an equal number of dangerous tiles (with bombs underneath), or $0$ otherwise. Obviously, Perry needs to find out the positions of the dangerous tiles. You must help him by using his device, trying to enter as few triplets as possible (we cannot waste too much time, otherwise we won't stop Doofenshmirtz before realizing his evil plans).

## Interaction

Initially, the numbers $N$ and $K$ are read from standard input. Your program is allowed to make queries by writing to standard output: "? $c$ $a$ $b$" representing entering a triplet of numbers into the device. After each such query, the interactor will respond in standard input as follows:

- "0": if in the sequences of length $c$ that start at $a$ and $b$ there is not the same number of dangerous tiles.
- "1": if in the sequences of length $c$ that start at $a$ and $b$ there is the same number of dangerous tiles.
- "-1": if the query is invalid, you must close the program after receiving this verdict.

A query is considered valid if the intervals $(a, a + c - 1)$ and $(b, b + c - 1)$ are disjoint, if $1 \leq c \leq N$ and if $1 \leq a, b, a + c - 1, b + c - 1 \leq N$.

After finding the positions of the tiles that have bombs under them, print "! $p_1$ $p_2 \dots p_K$", where $p_i$ = the position of the dangerous tile number $i$, and then terminate the program. After each query, including the final one, you must print '\n' and flush the standard output.

To flush output, you can use the following table:

| Language | C/C++ | Pascal | Python | Java | Rust |
| -------- | ----- | ------ | ------ | ---- | ---- |
| Required header | import sys | use std::io::{self, Write}; |
| Function | fflush(stdout) or cout.flush() | flush(output) | sys.stdout.flush() | System.out.flush() | io::stdout().flush().unwrap(); |

## Constraints and clarifications

- $1 \leq N \leq 10^9$
- $1 \leq K \leq 250$
- $K \cdot 2 + 1 \leq N$

For 20% of the tests:

- $1 \leq N \leq 2000$

For another 20% of the tests:

- $K = 1$

The trap tiles are fixed beforehand. (The grader is not adaptive)

## Scoring

- If the set of positions of the dangerous tiles you found is different from the correct one, the score obtained on that test will be $0$ points.
- Otherwise, your score will be decided based on $Q$, the number of queries made:
    - 50% of the test score for $Q \leq 2 \cdot (K + 1) \cdot ( \log_2 N + 4 )$
    - 100% of the test score for $Q \leq (K + 1) \cdot ( \log_2 N + 4 )$

Additionally, for $1 \leq N \leq 2000$, the test score will be awarded in full if the answer is correct, as long as $Q \leq 10^4$.

## Example

Input | Output
--- | ---
`3 1` | `N and K are read`
`? 1 1 3` | `Query compares tile 1 and tile 3`
`1` | `Responds that the tiles are the same`
 | `! 2`
 | `Tile 2 is the only one that is dangerous`

## Explanation

Out of the $3$ tiles, only one is dangerous. When we find out that tile $1$ and tile $3$ are identical, it becomes clear that neither of the two can have a bomb under them, since $K = 1$. Therefore, we can conclude that tile $2$ is the dangerous one.