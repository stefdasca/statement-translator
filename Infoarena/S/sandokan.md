## Task

Sandokan has chosen a natural number $K$ and found a sequence with $N$ distinct natural numbers on the couch. He plays with this sequence of numbers and successively applies the following operation: selects $K$ distinct elements from the sequence and removes all but the one with the maximum value (among those chosen). If at some point the sequence has strictly fewer elements than $K$, he stops and writes this sequence on a magic piece of paper; otherwise, he continues applying operations on the resulting sequence. It is hard for us to determine what sequence Sandokan wrote, so we only want to find out the total number of distinct possibilities of writing a sequence on the magic piece of paper. Since there may be quite a few possibilities, we want to know only the remainder when this number is divided by $2\,000\,003$.

## Input data

The input file `sandokan.in` contains on the first line the numbers $N$ and $K$, as described in the statement. The next line contains the $N$ distinct natural numbers.

## Output data

The first line of the output file `sandokan.out` contains the total number of distinct possibilities of writing a sequence on the magic piece of paper modulo $2\,000\,003$.

## Constraints and clarifications

$2 \leq K \leq N \leq 5\,000$

The $N$ initial numbers are natural and do not exceed $2$ billion

Two possibilities of writing a sequence are distinct if there is at least one number that appears in one sequence and does not appear in the other

## Example

`sandokan.in`

```
3 3
1 2 3
```

`sandokan.out`

```
1
```