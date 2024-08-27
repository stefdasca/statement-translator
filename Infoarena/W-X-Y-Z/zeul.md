# Por Costel, the God

Por Costel became a powerful Xel'Naga god after combining his essence with the ancient Ouros. Now he watches over mortals, being an omniscient entity and, as fat as he is, omnipresent. People live relatively peaceful lives, doing good deeds for each other. Por Costel can see in the infinite void all pairs of mortals $(x,y)$ with the property that the mortal $x$ has given a corncob to the mortal $y$. Por Costel, being a benevolent god, wants to bring balance to the world by ensuring that each mortal has given corncobs as many times as they have received them. To this end, he can manipulate a mortal to give a corncob to another. However, like any god, Por Costel wants to minimize his interventions in the lives of mortals. Por Costel already knows the optimal solution, being omniscient. Can you find it?

## Input data

The input file `zeul.in` will contain on the first line two natural numbers: the number of mortals $N$ and the number of corncob gifts that have occurred, $M$. On the next $M$ lines, there are two numbers per line, $x$ and $y$, meaning that the mortal $x$ has given a corncob to the mortal $y$. 

## Output data

The output file `zeul.out` will contain on the first line the minimum number $S$ of manipulations Por Costel has done to bring balance to the world. The next $S$ lines each will contain 2 natural numbers each, indicating that Por Costel has influenced the mortal $x$ to give a corncob to the mortal $y$.

## Constraints

$1 \leq N \leq 100\ 000$  
$1 \leq M \leq 300\ 000$  
For 40\% of the tests, $N \leq 10\ 000$  
Por Costel must survive

## Example

`zeul.in`
```
4 4
1 2
1 3
2 4
3 4
```

`zeul.out`
```
2
4 1
4 1
```
