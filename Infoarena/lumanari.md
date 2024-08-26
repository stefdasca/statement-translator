# Candles

Miss P. really likes romantic dinners. She considers a dinner to be more romantic if more candles are lit at the table where she sits. The owner of her favorite restaurant knows that P. will visit in the coming evenings. We will number these evenings starting from $1$. To impress her, he wants to light exactly $i$ candles each evening $i$. At the end of the evening, the candles will be extinguished. Also, he knows that if a candle is lit in one evening, its height will decrease by $1$. He has $M$ candles of different heights available, which will be used only at Miss P.'s table. The owner wants to know the maximum number of evenings $N$ in which he can impress Miss P.

## Input data

The input file `lumanari.in` will contain on the first line the number $M$ as described in the statement. On the second line of the input file, there will be $M$ natural numbers representing the heights of the $M$ candles.

## Output data

In the output file `lumanari.out`, it will contain the maximum value of $N$.

## Constraints and clarifications

$1 \leq M \leq 200\ 000$

The heights of the candles will be natural numbers less than $10^9$

If a candle reaches a height of $0$, it can no longer be used.

## Example

`lumanari.in`
`
6
1 3 4 5 6 1
`

`lumanari.out`
`
5
`

## Explanation

The candles will be used in the following manner over the $5$ days:

Day $0$: $1\  3\  4\  5\  6\  1$

Day $1$: $0\  3\  4\  5\  6\  1$

Day $2$: $0\  2\  3\  5\  6\  1$

Day $3$: $0\  2\  2\  4\  5\  1$

Day $4$: $0\  1\  1\  3\  4\  1$

Day $5$: $0\  0\  0\  2\  3\  0$