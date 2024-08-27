## Task

The tests for this problem are not well constructed enough to accurately differentiate inefficient or incorrect solutions. Enter here if you want to help us improve the quality of the tests for this problem! On the planet $Srevni$, there are $N$ cities connected by one-way streets. The cities are identified by numbers between $1$ and $N$. In each of these cities, a very nutritious food is produced. The selling price of the food can be different from city to city. To reduce costs, food transportation is done as follows: a supply truck that needs to supply city $i$ leaves from city $i$ to the city from where it needs to bring the food. When it arrives at the destination, it is loaded and then teleported back to city $i$. One day, $Regnos$, the ruler of the planet, out of boredom, thought it would be useful to know the lowest purchase price of the food for each city on the planet.

## Input data

The input file `srevni.in` will contain on the first line two integers $N$ and $M$. The next line will contain $N$ natural numbers separated by spaces, representing the food prices in each of the $N$ cities. Each of the next $M$ lines will contain two integers, separated by a space, $X$ and $Y$, indicating that there is a road from city $X$ to city $Y$.

## Output data

The output file `srevni.out` will contain on the first line $N$ numbers separated by spaces, which represent the lowest purchase prices of the food for each of the $N$ cities.

## Constraints and clarifications

$1 \leq N \leq 100\,000$  
$1 \leq M \leq 100\,000$  
Prices are natural numbers between $1$ and $1\,000\,000$

## Example

`srevni.in`

```
4 4 
1 2 4 3 
1 3 
2 4 
3 2 
3 4
```

`srevni.out`

```
1 2 2 3
```