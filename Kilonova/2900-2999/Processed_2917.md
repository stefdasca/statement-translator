Below is the translated competitive programming problem statement in English, with the specified instructions and format preserved:

---

Consider an alphabet $A$ consisting of the letters `X`, `Y`, and `Z`. Ric has started to learn word counting techniques. Now, he wants to count the words formed using the letters of the alphabet $A$ of length $N$, such that no two adjacent positions have the same letters.

# Task

Given $N$, determine:
1. The largest word of length $N$ in alphabetical order from the alphabet $A$, such that no two adjacent positions have the same letters.
2. The number of words formed using the letters of the alphabet $A$ of length $N$, such that no two adjacent positions have the same letters.

# Input data

The first line of the input file `cuvinte.in` contains $C$, the number corresponding to the task to be solved ($1$ or $2$). The second line will contain $N$.

# Output data

The first line of the output file `cuvinte.out` will contain the answer to the task corresponding to the input file.

# Constraints and clarifications

* $1 \leq N \leq \ 30 \ 000$;
* Two letters are adjacent in a word if they are on consecutive positions;
* Correctly solving task $1$ will award $20$ points.
* Correctly solving task $2$ will award $80$ points.

# Example 1

`cuvinte.in`
```
1
3
```

`cuvinte.out`
```
ZYZ
```

## Explanation

The largest word in alphabetical order with letters from the alphabet $A$ is `ZYZ`, which satisfies the restriction from task $C = 1$!

# Example 2

`cuvinte.in`
```
2
2
```

`cuvinte.out`
```
6
```

## Explanation

The words that can be formed with $N = 2$, respecting the restriction from task $C = 2$ are `XY`, `XZ`, `YX`, `YZ`, `ZX`, `ZY`.

---

Please review for potential errors and ensure the translated text correctly follows given instructions.