# Lottery

Having run out of means to finance his career as a professional FIFA player, RMN chose to play the Prize Lottery. He will participate in $q$ draws. For each draw, he will be given an interval of the form $[a,b]$ from which RMN has to choose 2 distinct natural numbers. If the 2 chosen numbers are coprime, he wins the draw and a considerable sum. Our hero believes that randomly choosing the 2 numbers is not profitable enough, so he asks you to calculate the number of winning pairs for each draw.

## Input data

The input file `loterie.in` will contain on the first line a natural number $q$, the number of draws. On the next $q$ lines, there will be 2 natural numbers $a$ and $b$ representing the endpoints of the interval of the respective draw.

## Output data

The output file `loterie.out` will contain $q$ numbers, the number on the $i$-th line representing the number of winning choices for draw $i$.

## Constraints and clarifications

$q \leq 100000$  
$a \leq 100$, for any draw  
$b \leq 50000$, for any draw  

The pair $(a,b)$ is not different from the pair $(b,a)$

For 20% of the tests  
$q \leq 1000$  
$a \leq b \leq 100$

## Example

`loterie.in`  
```
2  
2 5  
1 1  
```

`loterie.out`  
```
5  
0  
```

## Explanation

In the first case, the winning pairs are $(2,3), (2,5), (3,4), (3,5), (4,5)$  
In the second case, there is no winning pair.