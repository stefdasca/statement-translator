```markdown
Qwerty plays a lot with random numbers. Recently, he combined his passion for random numbers with his passion for permutations. Qwerty has an array of distinct numbers $V$ and a permutation $P$. He started applying the permutation on the array. He would like to apply the permutation an infinite number of times on the array, but since the world will end in the year $2012$, he thought to ask for help to satisfy his sick curiosity.

# Task

Qwerty asks you to tell him which is the smallest lexicographical array he can obtain by applying the permutation $P$ on the array $V$ any number of times, and in return, he offers you $100$ points and an extra chance for IOI.

# Input data

The input file `randomizare.in` contains:

- The first line contains the natural number $N$ representing the length of the permutation $P$ and the array $V$.
- The second line contains $N$ distinct natural numbers representing the elements of the array $V$.
- The third line contains $N$ distinct natural numbers between $1$ and $N$ representing the elements of the permutation $P$.

# Output data

The output file `randomizare.out` must print $N$ distinct natural numbers representing the smallest lexicographical array that can be obtained.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* The elements of the array $V$ can be stored in $32$-bit signed integer variables.

# Example

`randomizare.in`
```
10
18 5 67 25 4 68 34 65 74 82
4 3 8 7 1 5 2 10 6 9
```

`randomizare.out`
```
4 34 5 18 68 74 25 67 82 65
```

## Explanation

The arrays that Qwerty can obtain are:

1. $(18 \ 5 \ 67 \ 25 \ 4 \ 68 \ 34 \ 65 \ 74 \ 82)$
2. $(25 \ 67 \ 65 \ 34 \ 18 \ 4 \ 5 \ 82 \ 68 \ 74)$
3. $(34 \ 65 \ 82 \ 5 \ 25 \ 18 \ 67 \ 74 \ 4 \ 68)$
4. $(5 \ 82 \ 74 \ 67 \ 34 \ 25 \ 65 \ 68 \ 18 \ 4)$
5. $(67 \ 74 \ 68 \ 65 \ 5 \ 34 \ 82 \ 4 \ 25 \ 18)$
6. $(65 \ 68 \ 4 \ 82 \ 67 \ 5 \ 74 \ 18 \ 34 \ 25)$
7. $(82 \ 4 \ 18 \ 74 \ 65 \ 67 \ 68 \ 25 \ 5 \ 34)$
8. $(74 \ 18 \ 25 \ 68 \ 82 \ 65 \ 4 \ 34 \ 67 \ 5)$
9. $(68 \ 25 \ 34 \ 4 \ 74 \ 82 \ 18 \ 5 \ 65 \ 67)$
10. $(4 \ 34 \ 5 \ 18 \ 68 \ 74 \ 25 \ 67 \ 82 \ 65)$
```