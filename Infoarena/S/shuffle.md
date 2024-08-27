# Shuffle

## Task

After exhausting all financial resources from her country, Victoria is thinking about tricking the card shuffling machines in Las Vegas. On the Green Table in the casino, there are $N$ cards placed in a line, numbered from left to right (the first card has the value $1$, $\dots$, the last card has the value $N$). The shuffling machine is placed in front of the table and performs $K$ shuffles. A shuffle is performed as follows: in the first step, the machine takes the first half of the row of cards, and the second half is moved to the beginning (the first half remains in a special reserved area of the machine); in the second step, the machine takes the second half of the cards it has in the reserved area and places them at the end of the row of cards. It repeats the second step until no cards remain in the reserved area. Victoria wonders what the row of cards looks like after $K$ such shuffles, so you are required to give her the answer! To avoid very large output files, the row obtained after $K$ shuffles will be encoded using the following algorithm:
```cpp
int encode(int N, int S[]) { 
    // N = number of cards in the row 
    // S[i] = the card that is in position i, (1 <= i <= N) 
    int ret = 0; 
    for(int i=1; i<=N; i++) { 
        ret = (ret * 13 + S[i]) % 1299827; 
    } 
    return ret; 
    // the variable ret will need to be printed in the output file 
} 
```

## Input data

The input file `shuffle.in` contains on the first line, separated by a space, two natural numbers $N$ and $K$, representing the number of cards on the table, respectively the number of shuffles performed.

## Output data

The output file `shuffle.out` will contain on the first line a single natural number representing the row of cards on the table after $K$ shuffles, encoded according to the algorithm presented in the statement.

## Constraints and clarifications

$
2 \leq N \leq 2\,000\,000 \\
0 \leq K \leq 10^{18} \\
$

Shuffle number $i$ is performed on the row of cards obtained after the first $i-1$ shuffles, for any non-zero $i$.

If a row of elements has length $P$, then the first half of the row is represented by the first $\left[\frac{P}{2}\right]$ elements of the row (possibly $0$), the remaining elements constituting the second half (i.e., the next $P - \left[\frac{P}{2}\right]$ elements).

$[x]$, where $x$ is a real number, denotes the integer part of the number $x$. The encoding algorithm of the row does not present any peculiarities that could influence the solving of the problem.

## Example

shuffle.in
```
7 2
```

shuffle.out
```
823554
```

## Explanation

Initially, the row of cards on the table is $1\, 2\, 3\, 4\, 5\, 6\, 7$. The first shuffle is performed:
- the second half of the row is moved to the beginning, and the first half is saved in the reserved area. On the table, we will have: $4\, 5\, 6\, 7$, and in the reserved area: $1\, 2\, 3$.
The second half of the reserved area is moved to the end of the row, so on the table, we will have: $4\, 5\, 6\, 7\, 2\, 3$, and in the reserved area: $1$.
The second half of the reserved area is moved to the end of the row, so on the table, we will have: $4\, 5\, 6\, 7\, 2\, 3\, 1$, and no more cards will be in the reserved area, so the first shuffle is finished. On the table, there is the row $4\, 5\, 6\, 7\, 2\, 3\, 1$, and the second shuffle begins:
- the second half of the row is moved to the beginning, and the first half is saved in the reserved area. On the table, we will have: $7\, 2\, 3\, 1$, and in the reserved area: $4\, 5\, 6$.
The second half of the reserved area is moved to the end of the row, so on the table, we will have: $7\, 2\, 3\, 1\, 5\, 6$, and in the reserved area: $4$. 
The second half of the reserved area is moved to the end of the row, so on the table, we will have: $7\, 2\, 3\, 1\, 5\, 6\, 4$, and no more cards will be in the reserved area, so the second shuffle is finished. On the table, finally, there is the row $7\, 2\, 3\, 1\, 5\, 6\, 4$, which when encoded becomes: `823554`.