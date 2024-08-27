## Task

The rabbit Mivas is on a special mission. Lunch break is approaching, and Mivas needs a little help from you. The rabbit is traveling in a helicopter above the $OX$ axis, between the numbers $1$ and $N$. He knows that at each integer coordinate ($1$, $2$, $\dots$, $N$) there is a carrot, with known nutritional value. The helicopter will drop Mivas above an arbitrary position, and the rabbit will eat exactly $2$ carrots as follows: first the one at the landing position, and then the next one to the right (towards $N$) with a nutritional value smaller than the first one. If there is no such carrot, Mivas will remain half hungry. We define the nutritional value of a meal as the sum of the nutritional values of the carrots eaten. Because Mivas does not know exactly where he will be dropped by the helicopter, he asks you to calculate for each position the nutritional value of a meal starting from that position.

## Input data

The input file `xspe.in` will contain the natural number $N$ on the first line, and on the second line the $N$ natural numbers, representing the nutritional values of the carrots.

## Output data

The output file `xspe.out` will contain $N$ numbers, the $i$-th representing the value of a meal starting at position $i$.

## Constraints and clarifications

$2 \leq N \leq 1\,000\,000$

The nutritional value of a carrot is positive, less than $10^8$.

For tests worth 20 points,

$2 \leq N \leq 1\,000$

It is recommended to avoid reading with streams.

## Example

`xspe.in`
```
5 
4 2 20 1 13 
```

`xspe.out`
```
6 3 21 1 13 
```