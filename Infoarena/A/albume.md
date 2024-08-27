# Albums

Tudoraş has a passion for music. He owns $K$ albums from the discography of each of the $C$ bands he listens to. Every day, Tudoraş randomly selects exactly $Q$ albums from his collection to listen to during the day. At the end of the day, Tudoraş analyzes the albums he listened to. Specifically, he counts the number of different bands from which the $Q$ chosen albums come and notes this value. What will be the arithmetic mean of the recorded values, if the process is repeated for an infinite number of days? In other words, what is the expected value of the number of bands listened to in a day?

## Input data

The input file `albume.in` contains on the first line three values separated by space: $C, K, Q$.

## Output data

The output file `albume.out` must contain on the first line a single real value: the arithmetic mean of the values noted by Tudoraş.

## Constraints and clarifications

$1 \leq C, K \leq 1000$

$1 \leq Q \leq \min(1000, C \cdot K)$

For tests worth 10 points, $K = 1$.

For other tests worth 10 points, $Q = C \cdot K$.

For other tests worth 20 points, $C \cdot K \leq 10$.

Every day, all albums have an equal probability of being selected.

The result is considered correct if it has an absolute error of at most $10^{-6}$.

## Example

`albume.in`

```
2 2 2
```

`albume.out`

```
1.666666667
```

```
232 654 27
```

`albume.out`

```
25.542102567
```

## Explanation

In the first example, there are two bands, each with two albums. We number the albums as follows: $a_1 = 1$ (the first album of the first band), $a_2 = 1$ (the second album of the first band), $a_3 = 2$ (the first album of the second band), $a_4 = 2$ (the second album of the second band). By randomly selecting two albums, the following configurations can occur:

| Chosen albums | Bands |
|---------------|-------|
| $a_1, a_2$    | $1$   |
| $a_1, a_3$    | $1, 2$ |
| $a_1, a_4$    | $1, 2$ |
| $a_2, a_1$    | $1$   |
| $a_2, a_3$    | $1, 2$ |
| $a_2, a_4$    | $1, 2$ |
| $a_3, a_1$    | $2, 1$ |
| $a_3, a_2$    | $2, 1$ |
| $a_3, a_4$    | $2$   |
| $a_4, a_1$    | $2, 1$ |
| $a_4, a_2$    | $2, 1$ |
| $a_4, a_3$    | $2$   |

The sum of the numbers of bands in each case is equal to $1 + 2 + 2 + 1 + 2 + 2 + 2 + 2 + 1 + 2 + 2 + 1 = 20$. The 12 cases have an equal probability of occurring.

The result is $20 / 12 = 1.\overline{6}$.