## Rompetrol

The Rompetrol company has $N$ gas stations located along the Soarelui highway. The positions of the gas stations are known and are specified by the distances $d_1$, $d_2$, $\dots$, $d_N$ ($d_i$ represents the distance from the Rompetrol company's headquarters to gas station $i$). The Rompetrol company's headquarters are located at the entrance to the Soarelui highway. Additionally, for each gas station, the amount of fuel $c_i$ required to meet the demands of customers using that gas station is known. In $K$ of these gas stations, the company wants to set up fuel depots, which will supply the respective gas station as well as possibly other neighboring gas stations. Each gas station will be supplied from the nearest depot. For each gas station, the cost $a_i$ to set up a fuel depot within the gas station is known. The transportation cost of fuel from a depot $X$ to a gas station $Y$ is equal to the product of the amount of fuel needed at gas station $Y$ and the distance between $X$ and $Y$. The transportation cost for a given depot placement will be equal to the sum of the transportation costs of all gas stations. The total cost is equal to the sum of the total transportation cost and the setup costs of the depots in $K$ of the gas stations.

## Task

Write a program to determine the minimum total cost.

## Input data

The input file `rompetrol.in` contains in the first line two natural numbers separated by a space $N$ and $K$, representing the number of gas stations and the number of depots that need to be built, respectively. Each line $i$ in the next $N$ lines contains 3 natural numbers, separated by a space: $d_i$, $c_i$, and $a_i$, representing the distance from gas station $i$ to the Rompetrol company's headquarters, the amount of fuel needed at gas station $i$, and the cost of setting up a depot in gas station $i$.

## Output data

The output file `rompetrol.out` will contain in the first line the minimum possible total cost.

## Constraints

$1 \leq N \leq 100\ 000$  
$1 \leq K \leq N$  
$1 \leq N \cdot K \leq 5\ 000\ 000$  
$1 \leq d_1 < d_2 < \dots < d_N \leq 10\ 000\ 000$  
$1 \leq c_i \leq 1000$  
$0 \leq a_i \leq 1\ 000\ 000\ 000$  
At least 40% of the tests will have $N \leq 500$ and $K \leq 300$

## Example

`rompetrol.in`  
`6 3`  
`5 1 0`  
`6 1 0`  
`12 1 0`  
`19 1 0`  
`20 1 0`  
`27 1 0`  

`rompetrol.out`  
`8`

## Explanation

Depot 1 will be built in gas station 2 and supplies gas stations 1, 2, 3. (Cost: $1 \cdot 1 + 0 \cdot 1 + 6 \cdot 1 = 7$)  
Depot 2 will be built in gas station 4 and supplies gas stations 4, 5. (Cost: $0 \cdot 1 + 1 \cdot 1 = 1$)  
Depot 3 will be built in gas station 6 and supplies gas station 6. (Cost: $0 \cdot 1$).  
The total transportation cost is $7 + 1 + 0$.  
The setup cost of the 3 gas stations is $0 + 0 + 0 = 0$.  
The total cost is $8 + 0 = 8$.