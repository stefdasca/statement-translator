
$N$ bamboo rods are given with lengths $L_1$, $L_2$, $\dots$, $L_N$. According to an ancient tradition, two rods are in harmony if they have the same length. Since the $N$ lengths can differ, it is not obvious how to make pairs of harmonious rods. Thus, two rods can be chosen and if one is longer, it will be cut to match the length of the other, to harmonize with its pair. The surplus is added to the group of existing rods, and the pair is left aside to harmonize for a long time to bring luck and prosperity. The above procedure is repeated successively until either all rods are exhausted or only one rod remains.

# Task

Given $Q$ sets of rods, determine for each set, what is the smallest possible length of the final non-harmonious rod.

# Input data

The input file `bete.in` contains on the first line the number $Q$, representing the number of sets of rods. Then there are $Q$ lines, containing space-separated numbers, each line representing a set of rods. Thus, the first number in a line will represent the number $N$ of rods within the set, followed by their lengths $L_1$, $L_2$, $\dots$, $L_N$.

# Output data

The output file `bete.out` will contain $Q$ numbers, each on a separate line, representing the answer associated with each dataset.

# Constraints and clarifications

* $1 \leq Q, N \leq 10^{4}$
* $1 \leq L_k \leq 100$
* The total number of rods within the $Q$ sets will not exceed $10^{4}$.
* If all rods are exhausted, the output file will contain the value $0$.

# Example

`bete.in`
```
2
3 2 3 5
5 2 3 3 3 10
```

`bete.out`
```
0
1
```

## Explanation

Set 1: $L = \{2, 3, 5 \}$

- harmonize $3$ with $5 \rightarrow L = \{2, 2 \}$
- harmonize $2$ with $2 \rightarrow L = \{\}$
- length of the final rod: $0$

Set 2: $L = \{2, 3, 3, 3, 10 \}$

- harmonize $2$ with $10 \rightarrow L = \{3, 3, 3, 8 \}$
- harmonize $3$ with $8 \rightarrow L = \{3, 3, 5 \}$
- harmonize $3$ with $5 \rightarrow L = \{2, 3 \}$
- harmonize $2$ with $3 \rightarrow L = \{1 \}$
- length of the final rod: $1$
