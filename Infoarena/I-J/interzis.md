Forbidden

Count how many sequences of $N$ characters, containing only the characters 'a' and 'b', exist, with the condition that these sequences do not contain as a subsequence a fixed sequence of length $L$.

## Input data

The input file `interzis.in` contains on the first line the numbers $N$ and $L$ as described in the problem statement. The next line contains the sequence of length $L$ composed of the characters 'a' and 'b'.

## Output data

The output file `interzis.out` will contain the required number of sequences, modulo $101267$.

## Constraints

$1 \leq N \leq 15000$

$0 \leq L \leq 1000$

For $80\%$ of the tests $L \leq 50$

## Example

`interzis.in`
```
3 3
aaa
```

`interzis.out`
```
7
```

## Explanation

All valid sequences must not contain the subsequence 'aaa'. Therefore, the $7$ sequences will be:

`aab`
`aba`
`abb`
`baa`
`bab`
`bba`
`bbb`