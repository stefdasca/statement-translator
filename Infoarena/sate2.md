## Task

A feudal kingdom is known to be organized into $N$ hamlets. In each hamlet, there are inhabitants such that the total number of inhabitants in the feudal kingdom is $M$. After the invasion of a neighboring migratory people, it is desired to reorganize the $N$ hamlets into $K$ villages as follows:
a) each village should contain the quotient of $M$ divided by $K$ inhabitants
b) each hamlet should be included in one single village. A hamlet is included in a village if all the inhabitants of that hamlet belong to the village. Once a hamlet belongs to a village, it cannot belong to another village. Decide whether it is possible to reorganize the feudal kingdom.

## Input data

The input data is read from the file `sate2.in`. The first line contains the number of tests $T$. Each test contains on the first line 3 natural numbers: $N$ - the number of hamlets, $M$ – the total number of inhabitants in the feudal kingdom, $K$ – the number of villages desired to be formed. The next line contains $N$ natural numbers representing the number of inhabitants in each hamlet.

## Output data

The output file `sate2.out` includes, for each test, a single line containing the answer "DA" or "NU" (without quotes), indicating whether it is possible to reorganize the feudal kingdom or not.

## Constraints

$1 \leq T \leq 11$

$1 \leq N \leq 3000$

$1 \leq M \leq 90000$

$ K = 3$ or $4$

The values for the number of inhabitants in each hamlet are natural numbers in the interval $[1, 10\ 000]$.

There may be multiple hamlets with the same number of inhabitants.

## Example

`sate2.in`

```
2
9 60 3
2 2 10 6 1 10 14 11 4
9 60 4
2 2 10 6 1 10 14 11 4
```

`sate2.out`

```
DA
NU
```