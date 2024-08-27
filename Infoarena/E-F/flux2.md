## Task

Recently, the mayor of Infoarena hired someone to take care of the city's water transport network. It can be represented by $N$ reservoirs and $M$ pipes connecting each 2 distinct reservoirs. Among these $N$ reservoirs, two are more special, $S$ and $D$. The main reservoir (from which water enters the transport network) is the one with index $S$, and through the reservoir with index $D$, water reaches the city. In all other reservoirs, the amount of water that enters is equal to the amount that exits (it wouldn't make sense for more water to exit, and if more entered, the reservoir would explode at some point). Water circulates in the network only through the $M$ pipes, and for each pipe, a price $dis_i$ is known, indicating the maintenance cost the municipality has to pay to transport one unit of water per second through that pipe. Additionally, for each pipe, the maximum amount of water that can pass through it per second is known. The person hired to take care of this network was tasked to send as much water as possible from $S$ to $D$, while also ensuring that the cost per second is minimal (obviously the cost is the same for each second). Since the municipality of Infoarena is busy with many things, they ask you to look at several plans of the employee's (for multiple water transport networks) and to tell for each if it is efficient or not. In return, the municipality of Infoarena guarantees you 100 points for this problem.

## Input data

The input file `flux2.in` will contain on the first line a natural number $T$ representing the number of transport networks (respectively the number of employee's plans). Each transport network is then described as follows: The first line will contain 4 natural numbers $N$, $M$, $S$, and $D$ representing the number of reservoirs, the number of pipes, the reservoir source, and respectively the destination. The next $M$ lines will each contain 5 numbers $x_i$, $y_i$, $dis_i$, $f_i$, and $c_i$ representing a pipe going from $x_i$ to $y_i$ with a maintenance cost $dis_i$ and the maximum amount of water that can pass through it per second being $c_i$. Also, you know that the recent employee of the municipality proposes that $f_i$ units of water per second pass through this pipe.

## Output data

The output file `flux2.out` must contain $T$ lines, each having the answer to the respective transport network. Thus, line $i$ will contain 1 if the plan proposed by the employee is efficient (obtains the lowest possible cost for the maximum amount of water) or 0 otherwise.

## Constraints and clarifications

$1 \leq T \leq 6$

$2 \leq N \leq 1\,000$

$0 \leq M \leq 200\,000$

$1 \leq S, D, x_i, y_i \leq N$  
$S \ne D$

$0 \leq f_i, c_i \leq 1\,000\,000$

$0 \leq dis_i \leq 1\,000$

The plan proposed by the employee is correct (follows the restrictions in the statement, namely, the amount of water entering any reservoir is equal to the amount exiting except for $S$ and $D$)

## Example

`flux2.in`
```
2 
4 5 3 4 
2 1 0 4 4 
2 4 1 4 4 
3 2 0 8 8 
3 4 2 2 2 
1 4 4 4 6 
1 4 1 2 1 
0 1 2 3 0 0 
2 4 2 2 0 4 
1 3 2 6 6 
3 4 0 6 6 
4 1 4 0 3 
1 0 
```
`flux2.out`
```
1 
0 
```