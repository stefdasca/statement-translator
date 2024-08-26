# Carrots

Farmer Ion has a garden consisting of $N$ square zones with a side length of $1$ meter, arranged one after another in a line. In each such zone grows a magic carrot. For each carrot, its energy value is known. Rila the Rabbit, a mischievous rabbit, has invaded the farmer's garden and started eating the carrots. The rabbit follows a certain path and eats the entire carrots in the zones it passes through. After a carrot is eaten, another grows in its place with the same energy value (don't forget that the carrots are magical and the garden is imaginary). Rila's satisfaction degree is given by the sum of the energy values of the carrots he eats. Because the rabbit is a clever animal, its path has certain characteristics. Rila starts in a random zone and performs $P$ rabbit jumps, such that with his jumps he never leaves the garden. The farmer, after studying the rabbit's behavior for a long period, now knows the lengths of those $P$ rabbit jumps and knows that he performs all these jumps in any order. Determine the maximum satisfaction degree that the rabbit can obtain.

## Input data

The input file `morcovi.in` contains on the first line $N$, the number of garden zones. The second line of the file contains $N$ natural numbers, the $i$-th number on this line indicating the energy value of the carrots growing in the $i$-th zone. The third line of the file contains the number $P$, the number of jumps that the rabbit makes. The last line contains $P$ natural numbers, in any order, indicating the lengths of the rabbit's jumps.

## Output data

The output file `morcovi.out` contains a single natural number on the first line, representing the maximum satisfaction degree that Rila can obtain on his path through the farmer's garden.

## Constraints and clarifications

$2 \leq N \leq 1\ 000$

$1 \leq P \leq 12$

The energy value of a carrot is a natural number in the interval $[1, 100\ 000\ 000]$

Each length of the $P$ jumps is less than $N$

A jump from zone $x$ to zone $y$ has the length $|x-y|$

## Example

`morcovi.in`:

```
7 
1 20 3 1 1 40 10 
3 
1 2 4
```

`morcovi.out`:

```
71 
```

## Explanation

The rabbit starts in zone $4$. From there, it performs a jump of length $2$ to the left, reaching the zone with the carrot of value $20$. Then, it performs the jumps of length $4$ and $1$ to the right in sequence, eating the carrots with values $40$ and $10$ as well. The satisfaction degree is $1 + 20 + 40 + 10 = 71$.