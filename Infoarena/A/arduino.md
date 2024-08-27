## Task

Niramax is decorating the Christmas tree this year together with his colleagues. The team has already adorned the tree with ornaments while listening to "Decorate the Tree Map," a famous song. The only thing left to do is to put up the lights. The chosen lights are given by an array with $N$ elements, each element representing a light bulb. Each light bulb can have $M$ colors. The question that concerns the team is how to choose the colors of the bulbs. A loud colleague, being the most vocal, imposes the following scheme: "Don't be silly! Beauty is given by the number of different colors in the installation. We can impose restrictions on the number of distinct colors. To distribute the colors nicely, I'll give you $R$ restrictions in the form: - $NR$ $K$ $i_1$ $i_2$ $\dots$ $i_K$ : We take the values from the array at positions $i_1$ $i_2$ $\dots$ $i_K$. These values must contain exactly $NR$ distinct numbers after removing duplicates." As soon as the loud colleague finished listing the restrictions while everyone looked at him in amazement, his number one enemy at work says that it's hard to find a solution. The loud colleague responds, "No, you're dumb, haha! I'll find them all. I'll code it right now." Niramax tells the loud colleague, "You don't need to do that," but it was too late. The loud colleague was already lost in his world. Your job is to calculate the number found by the loud colleague.

## Input data

The input file `arduino.in` will contain on the first line the numbers $N$ $M$ and on the second line the number of restrictions $R$. The next $R$ lines contain the descriptions of the restrictions $NR$ $K$ $i_1$ $i_2$ $\dots$ $i_K$, one per line.

## Output data

The output file `arduino.out` will print the answer on a single line.

## Constraints

$2 \leq N \leq 10$   
$1 \leq M \leq 1000$   
$1 \leq$ sum of $K$ $\leq 100$

WEEEEE! ATTENTION!!! The answer must be printed MODULO $10^9 +7$ 

## Example

`arduino.in`   
```
10 1000  
2  
1 2 2 4  
2 3 2 3 7  
```

`arduino.out`    
```
146853000  
```

## Explanation

It's like counting our age until we get the answer manually...