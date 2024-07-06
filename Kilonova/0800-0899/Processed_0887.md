Miruna has discovered a new game. She has uppercase and lowercase English letters and successively builds increasingly longer strings of letters. She defines the CAPS operation for a letter as transforming that letter from uppercase to lowercase or vice versa. For each string $S$, Miruna associates a new string $S_C$, called the CAPS string, which is obtained by applying the CAPS operation to all the letters in string $S$. Miruna has invented another operation for a string of letters $S$, called NEXT, which produces a new string $S_N$ that has the structure $SS_cS_cS$ (it is formed in order from left to right by the letters of $S$, followed twice successively by the letters of string $S_C$, and then again followed by the letters of $S$). For example, for the string $S = $ `Ham`, the corresponding CAPS string $S_C = $ `hAM` and if the NEXT operation is applied to the string $S$, it produces the string $S_N = $ `HamhAMhAMHam`. Initially, Miruna constructs a string $S$ of $K$ letters. Then, she constructs a new string obtained by applying the NEXT operation to the string $S$. Miruna wants to successively obtain increasingly longer strings by applying the NEXT operation to the string constructed in the previous step.

Thus, for $K=3$ and $S = $ `Ham`, Miruna will construct the strings `HamhAMhAMHam`, `HamhAMhAMHamhAMHamHamhAMhAMHamHamhAMHamhAMhAMHam`, and so on. Miruna continues the construction process until she obtains a sufficiently long final string.

# Task

Miruna asks you to answer $Q$ questions such as:
_"If a natural number $N$ is given, what is the letter at position $N$ in the final string and how many times has this letter appeared in the final string from the beginning up to and including position $N$?"_

# Input data

The first line of the `caps.in` file contains two natural numbers separated by a space representing the values $K$ (the length of the initial string) and $Q$ (the number of queries). The next line contains the initial string $S$ of length $K$. On the following $Q$ lines will be one number $N$, representing the requirement of a query.

# Output data

In the `caps.out` file, there will be $Q$ lines, each containing two values separated by a space representing the answer to a query (the letter at position $N$ in the final string and its number of occurrences up to and including position $N$).

# Constraints and clarifications

* $1 < K \leq 100\ 000$
* $1 \leq Q \leq 50\ 000$
* $0 < N \leq 10^{18}$
* For each test, $40\%$ of the score is awarded if all the queried letters in the test are correct, and $60\%$ of the score is awarded if all the numbers of occurrences of the letters up to positions $N$ in the test's queries are correct.
* Miruna guarantees that she has constructed a final string longer than $N$.
* The first position in the string is considered position $1$.

| #  | Points | Constraints           |
| -  | ------ | --------------------- |
| 1  | 15     | $K \leq 250$, $Q \leq 1\ 000$, $N \leq 3\ 000$ |
| 2  | 20     | $N \leq 100\ 000$     |
| 3  | 20     | $K \leq 3\ 000$, $Q \leq 1\ 000$|
| 4  | 35     | No additional constraints. |

# Example

`caps.in`
```
3 1        
Ham
5 
```

`caps.out`
```
A 1
```

## Explanation

At position $5$ there will be the letter `A`, its number of occurrences from position $1$ to position $5$ is $1$.