Costel discovered his father's briefcase with a combination lock in a storage room. The lock is composed of $4$ metal discs inscribed with the digits from $0$ to $9$. Each disc can be moved individually, from top to bottom or from bottom to top, forming combinations of digits. Often, for convenience, the combination that opens the briefcase is made up only of identical digits: $0000, 1111$, etc.

Costel imagines a lock composed of $N$ metal discs, each inscribed with the digits from $0$ to $9$, each can be moved in the two specified directions. By move, Costel means shifting a disc up or down by one position, meaning shifting the disc to the previous digit or the next digit from the current one.

# Task

Create a program that, knowing the initial position of each of the $N$ discs of the lock, determines and displays:

1. the largest digit that appears on the lock's discs in the initial state;
2. the minimum number of moves necessary for the number obtained on the lock to consist only of identical digits, a number necessary to open the briefcase;
3. the smallest digit that can be obtained as a result of performing the minimum number of determined moves;
4. the number of combinations made up of identical digits that can be obtained as a result of performing the minimum number of determined moves.

# Input data

The file `cifru.in` contains:

* The first line contains the natural number $N$ representing the number of discs;
* The next $N$ lines each contain a digit, representing the current digit on each disc of the lock.

# Output data

The output file `cifru.out` will contain, on separate lines, the $4$ requested values.

# Constraints and clarifications

* $1 < N \leq 100\ 000$;
* A disc can remain unmoved.
* Correctly solving task $1$ earns $20\%$ of the points for each test
* Correctly solving task $2$ earns $40\%$ of the points for each test
* Correctly solving task $3$ earns $20\%$ of the points for each test
* Correctly solving task $4$ earns $20\%$ of the points for each test

# Example

`cifru.in`
```
4
7
3
9
0
```

`cifru.out`
```
9
7
0
2
```

## Explanation

We have a lock with $4$ discs. Initially, the lock is in state $7390$ (the first disc is positioned on digit $7$, the second on digit $3$, etc.). The largest digit on the lock is $9$. 
The minimum number of moves is $7$ and can be achieved in two ways: 

1. Move the first disc up by $2$ positions, the second disc down by $4$ positions, the third remains unmoved, and the last disc moves down by one position. The combination obtained is $9999$.
2. Move the first disc up by $3$ positions, the second disc down by $3$ positions, the third up by one position, and the last remains unmoved. The combination obtained is $0000$. Thus, the smallest digit that forms the combination with the minimum number of moves is $0$. We have $2$ combinations that can be obtained in the determined minimum number of moves: $0000$ and $9999$.