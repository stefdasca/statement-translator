## Task

Mihai has a string of length $N$ consisting of uppercase and lowercase English letters and digits. He defines a substring (i.e., characters found at consecutive positions) as duplicated if the substring appears at least twice at different positions in the initial string. Moreover, Mihai defines the value of a string as follows: The probability that a randomly chosen non-empty substring is duplicated. Find the value of a given string. The result should be displayed as an irreducible fraction. Note: When Mihai randomly chooses a non-empty substring, he proceeds as follows: he randomly selects 2 positions (start, end) from the set, and the chosen substring is the one between the start and end positions (considering indexing from $1$ to $N$).

## Input data

The input file `strdup.in` contains on the first line the number of tests $T$. The next $T$ lines contain each a string consisting of uppercase and lowercase letters + digits.

## Output data

The output file `strdup.out` will contain $T$ fractions on separate lines, in the form `<numerator>/<denominator>` (without any additional spaces), representing the probability that a randomly chosen non-empty substring is duplicated.

## Constraints and clarifications

$1 \leq T \leq 5$

$2 \leq N \leq 1000$

It is guaranteed that at least one substring is duplicated;

Beware of the memory limit!

## Example

`strdup.in`

```
2
00
aaab
```

`strdup.out`

```
2/3
1/2
```

## Explanation

For the first test, Mihai can choose $3$ non-empty substrings identified by the positions: $(1, 1)$ - "0", $(1, 2)$ - "00" and $(2, 2)$ - "0". Among these, $2$ are duplicated - both "0". Therefore, the result is $2/3$.

For the second test, Mihai can choose $10$ different substrings. Among these, the duplicated ones are:
* $(1, 1)$ - "a"
* $(1, 2)$ - "aa" because it also appears at $(2, 3)$;
* $(2, 2)$ - "a"
* $(2, 3)$ - "aa"
* $(3, 3)$ - "a"

The probability that the substring is duplicated is $5/10 = 1/2$ (the fraction must be displayed in irreducible form!).