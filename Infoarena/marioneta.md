## Task 

Papusa, Communism, Control After a harsh summer of picking pickled cucumbers, the harvests at Bastion need to be redistributed. There are an infinite number of pickled cucumber farms, but only $N$ of them had non-zero harvests this year. These are conveniently placed in a line, so that the farm with number $i$ is placed $i$ agricultural units to the right of Bastion. The $i$-th farm can redistribute its harvest in the following way: if it has exactly $i$ pickled cucumbers, they will be equally divided among all the farms between Bastion and farm $i-1$ (i.e. each receives one pickled cucumber, while farm $i$ loses them all). The goal of the National Consolidation Program for Redistributing Agricultural Exploits is to bring all the pickled cucumbers from the province to Bastion for a further redistribution. The program fails if a number of pickled cucumbers remain in the province without being redistributed in the agreed manner. Determine if the Ghoberman government's program will fail or succeed. 

## Input data 

The input file `marioneta.in` contains, for the first test, a number, $T$, indicating that there will be $T$ different scenarios to solve. Each scenario will have the following format: the first line contains $N$, representing the number of farms with non-zero harvests. The next $N$ lines each contain two numbers $P_i$ and $C_i$, indicating that farm number $P_i$ gathered a harvest of $C_i$ pickled cucumbers. 

## Output data 

In the output file `marioneta.out`, print for each scenario, $1$ if the government's program will succeed, $0$ if it will not. 

## Constraints 

$1 \leq T \leq 20$ 

$0 \leq C_i \leq 10^9$ 

$1 \leq N$ 

$1 \leq P_i \leq 1\ 000\ 000$ 

Let $S$ = $C_1 + C_2 + \dots$

## Subtasks 

1. $11$ points, $N \leq 400$ and $S \leq 5000$ 
2. $14$ points, $N \leq 1\ 000$ 
3. $21$ points, $N \leq 6\ 000$ and $S \leq 10^7$ 
4. $26$ points, $N \leq 10\ 000$ 
5. $28$ points, $N \leq 50\ 000$ 

## Example 

`marioneta.in`:
```
3 
1 
2 
2 
2 
3 
2 
4 
4 
1 
3 
3 
1 
1 
0 
```

`marioneta.out`:
```
1 
0 
