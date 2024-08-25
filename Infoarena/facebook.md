Facebook

On the right side of Facebook, you see $K$ friend suggestions. For each suggestion, the number of mutual friends is known. Gigel wants to have $K$ people with the same number of mutual friends in the suggestions. He can reject a Facebook suggestion, in which case another person takes that place. Knowing in advance the order of the $N > K$ suggestions that Facebook has prepared, find the minimum number of operations needed to fulfill Gigel's wish. If there is no solution, return $-1$.

## Input data

The input file `facebook.in` will contain the numbers $N$ and $K$ on the first line. The second line will contain $N$ numbers, representing the number of mutual friends Gigel has with each of the friends suggested by Facebook, in the order of their appearance in the suggestion list.

## Output data

The output file `facebook.out` will contain on the first line the minimum number of operations, if there is a solution. Otherwise, it will contain $-1$.

## Constraints and clarifications

$1 \leq K \leq N \leq 2^{17}$

Gigel is very popular, so the number of mutual friends he has with the suggestions given by Facebook is within the range $[0, 2^{30}]$.

## Example

`facebook.in`
```
6 3
1 2 3 1 1 2
```

`facebook.out`
```
2
```

## Explanation

Gigel rejects the second suggestion, and the list of $K$ suggestions becomes: $1\ 3\ 1$. Gigel rejects the second suggestion again, and the new suggestions are: $1\ 1\ 1$.