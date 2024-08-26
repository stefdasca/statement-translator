## Alibaba

Ali Baba caught the 40 thieves rummaging through his treasures. They were many, and he was alone, so he tried to negotiate with them. Among the treasures, there was a special chest with the number of diamonds written on it. Ali Baba proposed to the leader of the thieves to cut $K$ digits from the representation of the number, and he would give the thieves as many diamonds as the number remaining after the cut.

## Task

Help the leader of the thieves determine the number that remains after the cut, so that it is as large as possible.

## Input data

The first line of the input file `alibaba.in` contains two natural numbers (separated by a space) $N$ and $K$, representing the number of digits in the number written on the chest, and the number of digits to be cut, respectively. The second line contains the string of digits written on the chest. There are no spaces between the digits.

## Output data

The first line of the output file `alibaba.out` will contain the number of diamonds the thief will be able to take.

## Constraints and clarifications

$1 \leq N \leq 10\, 000$

$0 \leq K \leq N-1$

Denoting by $c_1, c_2, \dots, c_N$ the sequence of digits of the number written on the chest, 

$0 \leq c_i \leq 9$,

$i = 1, 2, \dots, N$.

## Example

`alibaba.in`
```
5 3
12312
```

`alibaba.out`
```
32
```