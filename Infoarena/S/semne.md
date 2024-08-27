# Signs

Iggel is a troubled alien teenager. He got into trouble at school again and now he must be punished. As a consequence, his parents decided to make him solve the following problem: Given $N$ natural numbers and a number $S$, each number must be either added or subtracted exactly once so that the sum $S$ is obtained.

## Task

Help Iggel by writing $N$ signs of '+' and '-' in a cornfield depending on the operations that need to be performed with the numbers $a_i$ to obtain the sum $S$.

## Input data

The first line of the file `semne.in` contains two integers $N$ and $S$ as described above. The next line contains $N$ numbers $a_i$ in ascending order.

## Output data

The file `semne.out` will contain $N$ characters '+' or '-', representing the sign of each number.

## Constraints and clarifications

$1 \leq N \leq 50\ 000$

$1 \leq a_i \leq 5\ 000\ 000$

For 50% of the tests

$N \leq 500$

$a_i \leq 3\ 000$

## Example

`semne.in`
```
5 3
1 2 3 4 5
```

`semne.out`
```
-+++-
```