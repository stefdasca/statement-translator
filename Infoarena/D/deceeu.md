Why Me?

PCP just received from the secret services a string of $N$ lowercase English alphabet characters. He needs to find out how many subsequences of the given string are perfect. A string of characters is called perfect if it can be formed by concatenating two copies of the same string. For example, "mama" ("ma" + "ma") or "abcabc" ("abc" + "abc") are perfect strings, while "pap" or "abcd" are not. A string $X$ is considered a subsequence of string $Y$ if $X$ can be formed by deleting zero or more characters from $Y$. When PCP read the problem, he felt very discouraged, wondering "Why did I get this task?". You need to show him that there is still hope and help him solve it!

## Input Data

The input file `deceeu.in` contains on the first line $T$, the number of tests. 
There follow $T$ lines, each line describing a test and being formed of a string of characters of size $N$.

## Output Data

The output file `deceeu.out` must contain $T$ lines. The $i$-th line represents the answer for the $i$-th test from the input file. Since the answer can be very large, print it modulo $1.000.000.007$.

## Constraints

$1 \leq N \leq 200$

$1 \leq T \leq 20$

## Example

`deceeu.in`
```
5
abc
abca
effeef
bbbb
aabbbaaabababbabbaab
```

`deceeu.out`
```
0
1
10
7
25545
```

## Explanation

The subsequences are described by the positions in the original string that form them.

For test 3, the 10 subsequences are:

$\{1, 4\}$, $\{1, 5\}$, $\{4, 5\}$, $\{1, 2, 4, 6\}$, $\{1, 2, 5, 6\}$, $\{1, 3, 4, 6\}$, $\{1, 3, 5, 6\}$, $\{2, 3\}$, $\{2, 6\}$, $\{3, 6\}$.

For test 4, the 7 subsequences are:

$\{1, 2\}$, $\{1, 3\}$, $\{1, 4\}$, $\{2, 3\}$, $\{2, 4\}$, $\{3, 4\}$, $\{1, 2, 3, 4\}$.