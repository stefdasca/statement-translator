Ionel and Gigel have decided to reminisce about their childhood game called "Maroco". They have $n$ sticks, numbered from $1$ to $n$. Each stick has a certain score, and the scores are distinct. Initially, the sticks are arranged in a pile where they are stacked on top of each other.

The rules of the game are:
- At any moment, only one "free" stick can be extracted, meaning no other stick is on top of it;
- The children do not think many moves ahead but choose the best move at that step, meaning they select the "free" stick with the highest score.

Ionel starts the game.

# Task

Given the number of sticks $n$, the score of each stick $p_1, p_2, \dots, p_n$ and the arrangement of the sticks in the pile, determine which child is the winner and their accumulated score.

# Input data

The input file `maroco.in` contains the number of sticks $n$ on the first line. The next $n$ lines contain information about the $n$ sticks. Specifically, the $i+1$ line contains: $p_i\ nr_i\ b_{i_1}\ b_{i_2}\ \dots\ b_{nr_i}$, where $p_i$ is the score of stick $i$, $nr_i$ is the number of sticks above stick $i$, and $b_{i_1}\ b_{i_2}\ \dots\ b_{nr_i}$ is the list of the $nr_i$ sticks initially above stick $i$.

Numbers on the same line are separated by spaces.

# Output data

The output file `maroco.out` should contain on the first line two natural numbers separated by a space $w$ and $t$, where $w$ represents the winner of the game ($1$ if Ionel is the winner, $2$ if Gigel is the winner, or $0$ in case of a tie), and $t$ represents the total score accumulated by the winner.

# Constraints and clarifications

* $2 \leq n \leq 100$ and $n$ is even.
* $1 \leq p_i \leq 1\ 000$
* All numbers involved in the problem are natural numbers.
* For test data, there is always a solution.

# Example

`maroco.in`
```
10
70 0
100 3 1 9 10 
40 2 2 4
80 2 1 6
90 2 2 7
40 0
60 2 6 9
20 1 10
10 1 8
50 0
```

`maroco.out`
```
1 320
```

## Explanation

The sticks chosen by each child are:
* Ionel: $1$ ($70$p), $6$ ($40$p), $8$ ($20$p), $2$ ($100$p), $5$ ($90$p) $ \rightarrow 320$p;
* Gigel: $10$ ($50$p), $4$, ($80$p), $9$ ($10$p), $7$ ($60$p), $3$ ($40$p) $ \rightarrow 240$p.