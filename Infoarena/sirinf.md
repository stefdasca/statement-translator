## Task

Note: During the contest, the tests were weak. Now the tests have been updated. Cristinel found a string $S$ of length $N$. Alexei is envious because he also wants a string. Therefore, they decided that whoever solves this problem will get the string. We define the infinite string $T$ as an infinite concatenation of $S$. In other words, $T = S + S + \dots$ an infinite number of times. Both Alexei and Cristinel observed that the string $T$ has at most $N$ distinct suffixes. The $N+1$-th suffix will be the same as the first suffix. The $N+2$-th suffix will be the same as the second suffix. And so on. We take these $N$ suffixes, sort them lexicographically (in case of ties, by the index of the suffix). To get the string, Alexei and Cristinel need to answer the question: What is the position of the string $S$ in the sorted list of the $N$ suffixes? For more details, refer to the example explanation.

## Input data

The input file `sirinf.in` contains $T$, the number of tests in the first line. Then, on the next lines, there appears one string formatted from the English alphabet for each test.

## Output data

The output file `sirinf.out` contains $T$ lines, with the $i$-th line containing the position of the string $S$ in the sorted list of the $N$ suffixes of the string $T$.

## Constraints

$
1 \leq N \leq 10^6
$

$
1 \leq T \leq 10
$

## Example

`sirinf.in` 

```
5
cabcab
mama
alexei
cristinel
dusmaniitraiescprintrenoi
```

`sirinf.out` 

```
5
3
1
1
4
```

## Explanation

$S = cabcab$, $T$i represents the $i$-th suffix of the string $T$

The suffixes in sorted order: 

1) $T2 = abcabcabca\dots$ 
2) $T5 = abcabcabca\dots$ 
3) $T3 = bcabcabcab\dots$ 
4) $T6 = bcabcabcab\dots$ 
5) $T1 = cabcabcabc\dots$ 
6) $T4 = cabcabcabc\dots$ 

We observe that the initial string is at position $5$.