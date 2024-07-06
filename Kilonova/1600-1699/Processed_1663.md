```markdown
Manole is extremely sick. Because of this, he went to the family doctor who advised him to follow a treatment with $N$ pills, from which he has to take a half every day. He bought from the pharmacy a box containing exactly $N$ pills, each one having a stripe on the surface that marks its half.
Manole starts his treatment and finds out that he can only proceed as follows:
* He takes a whole pill from the box and uses only half of it on that day, putting the remaining half back in the box;
* He takes a half pill from the box, left from one of the previous days, and uses it on that day.

# Task

Write a program that determines the number of ways he can take all $N$ pills, proceeding according to the method described above.

# Input data

The input file `pastile.in` contains on the first line the natural number $N$.

# Output data

The output file `pastile.out` will contain on the first line the determined number.

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$

# Example

`pastile.in`
```
3
```

`pastile.out`
```
5
```

## Explanation

If we denote by `P` a whole pill and by `J` a half pill then Manole had $5$ possibilities:
1. `P J P J P J`
2. `P P J J P J`
3. `P J P P J J`
4. `P P P J J J`
5. `P P J P J J`
```