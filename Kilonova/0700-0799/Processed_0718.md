Consider strings formed from two types of brackets: round brackets and square brackets. The brackets are encoded as follows: open round bracket with $0$, closed round bracket with $1$, open square bracket with $2$, closed square bracket with $3$. Unlike the usual convention in mathematics, here we can have round brackets included in square brackets and square brackets included in round brackets. We cannot associate an open round bracket with a closed square bracket or vice versa.

# Task

Determine if such a string is correctly constructed in the sense that we can correctly associate pairs of brackets of each type.

# Input data

The input file `paranteze.in` contains on the first line the number $n$ (the number of test strings).

Then on each of the lines $2, 3, \ldots, n+1$ contain the numbers $L\ c_1\ c_2\ \ldots\ c_L$, the natural number $L$ represents the length of a string of brackets encoded as per the statement.

The values $c_1, c_2, \ldots, c_L$ represent the respective codes. All numbers are separated by a single space.

# Output data

The output file `paranteze.out` will contain $n$ lines. On each line, a message will be written. Each line will contain one of the messages `Yes`, respectively `No`, representing the results of the verification of the correctness of the strings. Their order corresponds to the order of the strings from the input file.

# Constraints and clarifications

* $1 \leq n \leq 10$;
* Each value $L$ satisfies the condition: $1 \leq L \leq 500$.

# Example

`paranteze.in`
```
8
6 0 2 3 1 0 1
6 2 0 1 0 1 3
4 0 2 1 3
6 2 0 0 3 1 1
6 2 2 0 1 1 3
6 2 0 0 1 3 0
10 2 2 0 1 0 1 3 3 0 1
10 0 0 0 1 1 1 0 2 3 1
```

`paranteze.out`
```
Yes
Yes
No
No
No
No
Yes
Yes
```

## Explanation

The first string in the test corresponds to the bracket string `([])()