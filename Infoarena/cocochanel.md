Coco Chanel

In Coco Chanel's garden, there are $N$ roosters and $M$ hens. A rooster can befriend a hen if the arrogance of the rooster is less than or equal to the arrogance of the hen. After a rooster has befriended a hen, the arrogance of the rooster doubles. Determine for each rooster the maximum number of hens it can befriend.

## Task

## Input data

The input file `cocochanel.in` will contain on the first line $N$ and $M$. The next line will contain $N$ numbers: the $i$-th number represents the arrogance of the $i$-th rooster. The third line will contain $M$ numbers: the $i$-th number represents the arrogance of the $i$-th hen.

## Output data

The output file `cocochanel.out` will contain $N$ lines: the $i$-th line contains the maximum number of hens that the $i$-th rooster can befriend.

## Constraints and clarifications

$1 \leq N$
$M \leq 100\ 000$ 
the arrogances are natural numbers in the interval $[1,\ 1\ 000\ 000\ 000]$

## Example

cocochanel.in 
```
4 5
7 10 1 4
100 10 20 70 36
```
cocochanel.out 
```
4
4
5
5
```