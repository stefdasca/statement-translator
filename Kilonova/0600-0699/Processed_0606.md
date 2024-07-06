In a storage facility of the state mint, $n$ bags of coins arrive. The warehouse manager knows the number of coins in each bag and would like to balance the contents of the bags by moving coins from one bag to another, so that each bag ends up with the same number of coins. Help the warehouse manager achieve an equal number of coins in each bag by performing a minimum number of moves.

# Input data
The input file `monezi.in` contains on the first line an integer $n$, representing the number of bags. Each of the following $n$ lines contains an integer, representing the number of coins in each bag.

# Output data
The results will be written in the output file `monezi.out` in the following format:
- The first line contains an integer $m$, representing the minimum number of moves required.
- The following $m$ lines will each contain 3 integers $a$, $b$, $c$, separated by a space, where:
  - $a$ represents the index of the bag from which coins are moved;
  - $b$ represents the index of the bag to which coins are moved;
  - $c$ represents the number of coins moved from bag $a$ to bag $b$.

# Constraints and clarifications
- $2 \leq n \leq 2\ 000$
- The total number of coins in all bags is $ \leq 1\ 000\ 000\ 000$.
- In case the problem has no solution, the word `NU` will be written in the file, and if the problem has multiple solutions, any of them may be displayed.

# Example
`monezi.in`
```
3
35
48
37
```
`monezi.out`
```
2
2 1 5
2 3 3
```
