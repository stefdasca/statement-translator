Here's the translated competitive programming problem statement in English:

On an island, there are $N$ cannibals. For each cannibal $i$, 4 determining factors are known: $X[i]$ - the cannibal's speed, $Y[i]$ - the cannibal's endurance, $Z[i]$ - the cannibal's strength, and $T[i]$ - the cannibal's value.

It is known that a cannibal $i$ can eat a cannibal $j$ if and only if:

* $X[i] \geq X[j]$ and $Y[i] \geq Y[j]$ and $Z[i] \geq Z[j]$ and $T[i] \geq T[j]$.

The truth is that hunger is great and with nothing to eat, the cannibals begin to eat each other. Considering their religion, a cannibal cannot eat more than two other cannibals. Knowing all this, you must determine the minimum number of cannibals who can remain alive after the Great Feast.

# Input data

The input file `canibali.in` contains on the first line a natural number $N$, representing the number of cannibals. The next $N$ lines contain 4 numbers separated by spaces: $X[i], Y[i], Z[i]$, and $T[i]$, representing the speed, endurance, strength, and value of the $N$ cannibals.

# Output data

The output file `canibali.out` must contain a single number, representing the minimum number of cannibals who can remain alive.

# Constraints and clarifications

* $3 \leq N \leq 2\ 048$
* $0 \leq X[i], Y[i], Z[i], T[i] \leq 2^{17}$
* For ethical and philosophical reasons, a cannibal cannot eat themselves.

# Example 1

`canibali.in`
```
3
1 2 3 4
2 1 3 4
1 2 4 3
```

`canibali.out`
```
3
```

## Explanation

None of the 3 cannibals can eat any of the other 2, so all 3 remain alive.

# Example 2

`canibali.in`
```
3
1 2 3 4
1 2 3 4
1 2 3 4
```

`canibali.out`
```
1
```

## Explanation

Each of the 3 cannibals can eat any of the other 2, so one correct solution that gives the correct answer is: Cannibal 2 eats Cannibal 3, and Cannibal 1 eats Cannibal 2. Another correct solution is: Cannibal 1 eats Cannibal 2 and Cannibal 3.

# Example 3

`canibali.in`
```
4
1 2 3 4
1 2 3 4
1 2 3 4
2 3 4 5
```

`canibali.out`
```
1
```

## Explanation

One correct solution is: Cannibal 2 eats Cannibal 3, Cannibal 1 eats Cannibal 2, and Cannibal 4 eats Cannibal 1. An incorrect solution is: Cannibal 4 eats Cannibal 1 and Cannibal 2, leaving 2 cannibals alive.