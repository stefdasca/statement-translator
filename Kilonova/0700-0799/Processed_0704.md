```markdown
# Task

Gigel's younger brother received a set of colored blocks from Santa Claus. Gigel had just finished fifth grade and no longer played with such toys, but when nobody was watching, he seemed to join the little one in the game, especially when he arranged the $n$ blocks one after another, and all kinds of requirements that his computer science teacher might come up with crossed his mind:

1. to see how many colors are there in total;
2. which color is used for the most blocks;
3. the positions from which a block should be removed from the sequence so that a sequence of blocks of the same color as long as possible is formed from the remaining blocks.

# Input data

Input will be read from the file `cuburi.in`: 
First line contains $n$, the number of blocks, and then, on the next line, a sequence of $n$ color numbers, separated by spaces. The colors are numbered starting from $1$. Each task must output a separate answer on a new line.

# Output data

The file `cuburi.out` will contain one line for the answer/answers to each task.

# Constraints and clarifications

* $N$ is a natural number less than $200\ 000$, and the colors are at most $10$ in number, numbered from $1$ to $10$.
* For tests worth $40$ points, $N \leq 100$;
* For tests worth another $40$ points, $N \leq 2\ 000$;
* If there are multiple solutions for tasks $2$, $3$ all should be specified in ascending order.
* Tests and constraints have been modified.

# Example

`cuburi.in`
```
15
5 2 5 2 2 3 3 2 3 5 3 3 3 2 2
```

`cuburi.out`
```
3
2 3
10
```
```