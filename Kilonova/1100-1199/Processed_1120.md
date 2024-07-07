Georgel is writing an algorithm that contains assignment, alternative, selection, repetitive, and compound structures. After writing the algorithm, he wants to test it for all possible cases. To do this, he needs to know the minimum number of test cases necessary.

To describe the structures, the following keywords are used:
- for assignment
    - `ATRIB`
- for alternative
    - `DACA`
    - `ATUNCI`
    - `ALTFEL` (where `ALTFEL` may be omitted)
- for selection
    - `ALEGE`
    - `CAZ`
    - `CAZ_IMPLICIT` (where `CAZ_IMPLICIT` may be omitted)
- for repetitive
    - `CAT_TIMP`
    - `REPETA`
    - `PANA_CAND`
    - `PENTRU`
- for compound
    - `INCEPUT`
    - `SFARSIT`

There is no distinction between uppercase and lowercase letters. An algorithm starts with the keyword `INCEPUT`, ends with `SFARSIT`, and does not contain empty structures. Moreover, a compound structure starts with the keyword `INCEPUT` and ends with `SFARSIT`.

# Task

Calculate the minimum number of test cases necessary to verify the algorithm.

# Input data

From the text file `algor.in`, the algorithm is read which contains one keyword per line. There are no empty lines. The algorithm respects the principles of structured programming and is written correctly.

# Output data

In the file `algor.out`, the first line will contain the minimum number of test cases necessary to verify the algorithm. The verification is based on the "white-box" principle, meaning that the tests are composed in such a way that it is possible to execute the algorithm on all possible branches. For example, in the case of a repetitive structure `CAT_TIMP` containing a single `ATRIB` in its body, one test targets an execution without entering the structure's body, another for passing through it at least once. Similarly, the `PENTRU` structure is treated.

# Constraints and clarifications

* After the keywords `ATUNCI`, `ALTFEL`, `CAZ`, `CAZ_IMPLICIT`, `CAT_TIMP`, `REPETA`, `PENTRU` there must necessarily be an assignment, alternative, decision, repetitive or compound structure.
* The algorithm has at most $127$ instructions.

# Example 1

`algor.in`
```
INCEPUT
ATRIB
DACA
ATUNCI
ATRIB
SFARSIT
```

`algor.out`
```
2
```

# Example 2

`algor.in`
```
INCEPUT 
ATRIB
REPETA
INCEPUT
ATRIB
ATRIB
SFARSIT
SFARSIT
```

`algor.out`
```
1
```

## Explanation

`REPETA` executes at least once.

# Example 3

`algor.in`
```
INCEPUT 
ATRIB 
ALEGE 
CAZ
ATRIB
CAZ
INCEPUT
ATRIB
ATRIB
SFARSIT
SFARSIT
```

`algor.out`
```
3
```

## Explanation

- Execute `ATRIB` from the first `CAZ`
- Execute `ATRIB` from the second `CAZ`
- Neither the first nor the second `CAZ` is executed

# Example 4

`algor.in`
```
INCEPUT
ATRIB 
ALEGE 
CAZ
ATRIB
CAZ
ATRIB
CAZ_IMPLICIT
ATRIB
SFARSIT
```

`algor.out`
```
3
```

## Explanation

- Execute `ATRIB` from the first `CAZ`
- Execute `ATRIB` from the second `CAZ`
- Execute `ATRIB` from `CAZ_IMPLICIT`

# Example 5

`algor.in`
```
INCEPUT 
ATRIB 
DACA 
ATUNCI 
ATRIB
ALTFEL
ATRIB
PENTRU
ATRIB
SFARSIT
```

`algor.out`
```
4
```

## Explanation

- Execute `ATUNCI` and `PENTRU`
- Execute `ATUNCI` and do not execute `PENTRU`
- Execute `ALTFEL` and `PENTRU`
- Execute `ALTFEL` and do not execute `PENTRU`

# Example 6

`algor.in`
```
INCEPUT
PENTRU
INCEPUT
ATRIB
DACA
ATUNCI
ATRIB
ALTFEL
INCEPUT
DACA
ATUNCI
ATRIB
DACA
ATUNCI
ATRIB
ALTFEL
ATRIB
SFARSIT
SFARSIT
SFARSIT
```

`algor.out`
```
6
