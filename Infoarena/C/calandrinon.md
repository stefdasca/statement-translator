# Calandrinon

## Task

The problem states that we have a string of length $N$ consisting only of lowercase English letters. The white bird asks you to remove some of these characters so that the resulting string after all removals has the following properties simultaneously:
- It contains only distinct elements.
- It is the longest possible.
- It is lexicographically minimal compared to any other string that would meet the first two conditions after a possible series of removals.

For example, if you have the string $alblb$, a possible series of removals would be selecting the first $l$ and the first $b$ so that the resulting string in the end is $alb$. This string meets the first two properties but not the third one because there is another series of removals that results in a lexicographically smaller string, namely the string $abl$ by removing the first $l$ and the second $b$. The latter is also the accepted solution by the white bird for the given example string.

## Input data

The input file `calandrinon.in` will contain on the first line a single value, $N$, representing the number of characters in the string. The second line of the file will contain $N$ characters representing the initial string.

## Output data

On the first and only line of the output file `calandrinon.out`, the characters of the resulting string after the removals will be printed.

## Constraints

$1 \leq N \leq 10^6$

We say that a string of characters $a_1 ,a_2 \dots a_M$ is lexicographically smaller than a string $b_1 , b_2 \dots b_M$ if there exists a position $1 \leq i \leq M$ such that $a_1 = b_1$, $a_2 = b_2 \dots a_{i-1} = b_{i-1}$ and $a_i < b_i$.

For $25\%$ of the tests, the string will contain only the characters $(a, b, c, d, e, f, g)$.

## Example

`calandrinon.in` 
```
29
vinefarasochemiiauzibatengeam
```

`calandrinon.out` 
```
vefarsochiuzbtngm
```