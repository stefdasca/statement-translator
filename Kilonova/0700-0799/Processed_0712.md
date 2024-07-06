Gigel is a great enthusiast of numbers. He spends all his free time playing with numbers. While doing so, one day he wrote on paper $10$ distinct two-digit numbers and noticed that among them there are two disjoint subsets with an equal sum. Of course, Gigel thought it was a coincidence and wrote another $10$ distinct two-digit numbers and to his surprise, after some time he again found two disjoint subsets with an equal sum.

# Task
Given $10$ distinct two-digit numbers, determine the number of pairs of **disjoint** subsets with an equal sum that can be formed from the given numbers, as well as one of these pairs for which the sum of the numbers in each of the two subsets is the maximum.

# Input data
The input file `numere.in` contains on the first line $10$ distinct natural numbers separated by a space $x_1$, $x_2$, $\\dots$, $x_{10}$.

# Output data
The output file `numere.out` contains three lines. The first line contains the number of pairs of subsets with an equal sum and the maximum sum obtained, separated by a space. The second line contains the elements of the first subset separated by a space, and the third line contains the elements of the second subset separated by a space.

# Constraints and clarifications
- $10 \\leq x_i, y_i \\leq 99$, for $1 \\leq i \\leq 10$
- $1 \\leq k, p \\leq 9$
- The order of subsets in pairs does not matter.
- The determined pair of subsets is not necessarily unique.

# Example
`numere.in`
```
60 49 86 78 23 97 69 71 32 10
```
`numere.out`
```
65 276
78 97 69 32
60 49 86 71 10
```

## Explanation

There are $65$ solutions.
The maximum sum is $276$.
$9$ out of the $10$ numbers are used.
The first subset has $4$ elements, the second subset has $5$ elements.