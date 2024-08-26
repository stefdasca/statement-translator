## Task

A kind of "after work comes reward," the Commission has promised to offer the participants of this contest free food and drink. After several discussions, it was decided that offering pizza to the contestants, as originally planned, would be immoral (it is the fasting period, isn't it?!). So it was decided that the best course of action is to offer only the pizza crusts (the commission's favorite part of the pizza). Two members of the commission, we won't name names, culinary masters, offered to prepare the crusts themselves (for a fee, of course) on the night before the contest. With only one oven available, they can only prepare one crust at a time. The two want to be paid according to the total time spent preparing the crusts (the price per minute for each of them is known). Moreover, if one has to prepare several crusts in a row, each will ask for an additional cost for each "extra" crust: For example, if the first member prepares 3 crusts one after another, he will ask for the additional cost twice (plus the standard cost for each crust). It was concluded that $N$ crusts are needed for the contest day. The preparation time for each is known. The two decided that the first will start preparing the crusts in the order $1, 2, \dots, N$ while the second in the order $N, N-1, \dots, 1$.

## Input data

The input file `blaturi.in` will contain on the first line the natural number $N$, representing the number of crusts that need to be prepared. The second line will contain $N$ non-zero natural numbers representing the preparation times of the $N$ crusts. The third line will contain two natural numbers $P1$ and $S1$ representing the price per minute and the additional cost requested by the first colleague. The last line will contain two natural numbers $P2$ and $S2$ representing the price per minute and the additional cost requested by the second colleague.

## Output data

The output file `blaturi.out` will contain, on the first line, the minimum cost to prepare the $N$ crusts.

## Constraints and clarifications

$1 \leq N \leq 100\; 000$   
$1 \leq P1, P2 \leq 100$   
$1 \leq S1, S2 \leq 10\; 000$   
$1 \leq preparation\ time\ of\ a\ crust \leq 100$   
For 20% of the tests, $1 \leq N \leq 10$ is guaranteed.   
The additional cost is the same regardless of the preparation time of the crust.   
It is possible for one colleague to prepare all the crusts alone.

## Example

`blaturi.in`
```
4  
1 2 3 4   
2 1   
3 3  
```

`blaturi.out`
```
23    
```

## Explanation

Only colleague 1 prepares the 4 crusts.    
Cost: $(2*1) + (2*2 + 1) + (2*3 + 1) + (2*4 + 1)$