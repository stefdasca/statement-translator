```markdown
A sequence of `N` natural numbers is considered. Some positions of the sequence are uninfected, and this is marked by the fact that the value at those positions is $0$. The rest of the positions are infected, and the non-zero value at an infected position represents the cost at which it can be disinfected. We disinfect some positions and want to eventually have exactly $K$ uninfected positions, and the total cost of disinfection should be minimal. A position can be disinfected at a given moment if and only if it has at least one uninfected neighboring position. After disinfecting a position, its associated cost is added to the total cost, the position becomes uninfected, and any other neighboring infected position can afterward be disinfected.

# Task
Knowing `N, K` and the sequence of natural numbers, determine the minimum cost with which exactly `K` uninfected positions can be obtained in the end (including the initially uninfected positions).

# Input data
The input file `antivirus.in` will contain on the first line the natural number `T` – the number of tests. Each test is described on two lines. The first line contains two natural numbers `N` and `K` with the significance mentioned in the statement, and the second line contains `N` natural numbers representing the elements of the sequence.

# Output data
The output file `antivirus.out` must contain `T` lines. Each line will display the response for a test - a natural number representing the minimum cost of a disinfection such that in the end the sequence contains exactly `K` uninfected positions – including those that were initially uninfected.

# Constraints and clarifications
* `1 \leq T \leq 4`
* `1 \leq K \leq N \leq 2000`
* The numbers in the array are less than or equal to $1\ 000\ 000$.
* For tests worth `10` points, it is guaranteed that `N \leq 80`
* For other tests worth `20` points, it is guaranteed that `N \leq 200`
* For other tests worth `10` points, in the initial sequence, there is exactly one uninfected position
* For other tests worth `10` points, in the initial sequence, there are exactly `2` uninfected positions

# Example

`antivirus.in`
```
2
8 5
9 1 4 4 0 1 3 9
6 4
1 0 2 0 1 1
```

`antivirus.out`
```
10
2
```

Explanations
---

There are `T = 2` tests.
For the first test, the elements at indices `2, 3, 4, 6` are disinfected.
For the second test, the elements at indices `5` and `6` are disinfected. Another valid solution would be indices `1` and `5`.
```