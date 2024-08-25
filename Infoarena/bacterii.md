# Bacteria

Recently, researchers at the CDC institute have begun to study the multiplication process of Streptococcus paracetivorus bacteria in detail. They observed an anomaly: from $N$ initial bacteria, after one step of multiplication, they become $N * (N - 3) + N + 2$ bacteria. To prevent a rapid increase in this type of bacteria, researchers need to know how many bacteria will exist after $K$ multiplication steps, modulo $M$, where $M$ is a prime number.

## Task

You are given $T$, the number of tests, and for each test, 3 natural numbers $N$, $K$, and $M$. Determine how many bacteria will exist after $K$ multiplication steps knowing that initially there were $N$ bacteria. For each test, the required result will be displayed modulo $M$.

## Input data

The input file `bacterii.in` contains on the first line the number of tests, $T$. On the following $T$ lines, for each test, there are 3 natural numbers $N$, $K$, and $M$, having the meaning given in the statement.

## Output data

The output file `bacterii.out` will contain $T$ lines, and each line $i$ will contain a single natural number, representing the desired result for test $i$.

## Constraints and clarifications

$1 \leq T \leq 1\\ 000$

$1 \leq N \leq 10^9$

$1 \leq K \leq 10^{18}$

$3 \leq M \leq 10^9$

$M$ is a prime number!

## Example

`bacterii.in`
```
1
3
3
97
```

`bacterii.out`
```
63
```

## Explanation

After the first step, the number of bacteria becomes $3 * 0 + 3 + 2$, which is $5$. After the second step, the number of bacteria becomes $5 * 2 + 5 + 2$, which is $17$. After the third step, the number of bacteria becomes $17 * 14 + 17 + 2$, which is $257$. $257 \% 97 = 63$.