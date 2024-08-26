## Task

Por Costel found the legendary safe that is said to "hide enough food that a man can feed for a lifetime." He believes it will be enough for breakfast, but first, he has to get past its defensive mechanism which is very similar (curiously) to that of a suitcase. To open the safe, he must enter a code of length $N$ (digits from $0$ from $0$ to $9$). The code is entered through $N$ wheels. Each wheel can be operated up or down (if a wheel indicates the value $X$, it can be operated by a single move to indicate the value $X + 1$ or to indicate the value $X - 1$). The legend says that the safe was crafted by ancient pigs. Therefore, there are $M$ distinct codes that can open the safe. Moreover, the safe has deteriorated over time, and now each of the $N$ wheels has a "margin of error" given by a number $E_i$. What this means is that a code will open the safe if there is a code among the $M$ for which: $|C_{i,j} - P_{k,j}| \leq E_j$ for any $i$ from $1$ to $T$ where:

* $C_{i,j}$ means the $j$-th digit of the code $i$
* $P_{k,j}$ means the $j$-th digit of the code $k$

Since the system was designed by some pigs, it was expected not to be of very high quality. There are so many combinations that open the safe, so many that we ask you to calculate their number modulo $10^9 + 7$. Por Costel is already licking his lips in anticipation!

## Input data

The input file `cifrul.in` will contain on the first line $T$, the number of tests; the following lines will describe the test cases as follows:
- the first line will contain $N$, $M$, $K$, $C$, $E$
- the next $M$ lines contain $N$ numbers separated by spaces (representing the codes of the $M$ ancient pigs). The $k$-th of these lines describes the $k$-th code

## Output data

The output file `cifrul.out` will contain $T$ lines, each containing the required number for that particular test.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 50$

$1 \leq M \leq 50$

$1 \leq K \leq 10^9$

$0 \leq C \leq 9$

$0 \leq E \leq 9$

## Example

`cifrul.in`
```
2
1 2 10000 3 1
6
3
1 100 5 1 6 30 12
1331
```

`cifrul.out`
```
10000
1331
```