## Task

Nagomi is tasked with eliminating all the other cafes on her very first day at Ton Tokoton. Since the other cafes want to join forces, they organize a secret meeting. At least, that's what they think. In reality, Nagomi has the map of the rooms where each member of the other cafes will sleep. This map is represented as a connected acyclic graph. Nagomi, who has reached an agreement with the hotel owner, discovers that the beds are equipped with poisoned needles that can prick the person sleeping on them without waking them up. She acquires a special device with the following ability: for 2 rooms $a$ and $b$, it activates the needles in the rooms on the chain between $a$ and $b$. The pricking process, carried out simultaneously in all rooms, lasts one second. Nagomi sets up some activations, which will be executed in the given order, possibly with dislike towards certain other maids. Another known fact: members of a cafe are so connected that pricking one affects all of them. Each cafe has its tolerance, which is the maximum number of pricks the entire clan can endure without being destroyed. Now, Nagomi wonders: for each clan, at what moment in time is it destroyed? Mr. Bland, proud of having used up another marker supply, patiently awaits a rigorous answer.

## Input data

The first line of the input file sever.in contains the numbers $N$ and $M$, representing the number of rooms and the number of clans, respectively. The rooms are numbered from $1$ to $N$. The next $N-1$ lines contain two numbers each, $x$ and $y$, indicating that there is a connection between room $x$ and room $y$. The next line contains $N$ values, the $i$-th representing the clan of the woman in room $i$. The next line contains $M$ values, the $i$-th representing the tolerance of clan $i$. The next line contains $Q$, the number of activations of the device. The next $Q$ lines contain two numbers $x$ and $y$, meaning the device has been activated between rooms $x$ and $y$.

## Output data

The output file sever.out will contain, on a single line, separated by a space, $M$ values, the $i$-th representing the moment in time when clan $i$ is destroyed. If a clan survives the attack, $-1$ will be printed.

## Constraints

$1 \leq N, Q \leq 200 000$  
$1 \leq M \leq N$  
Tolerances are non-negative integers that fit in the data type $int$  
The problem's test cases are grouped as follows:

### Constraints

$1 \ \leq \ N, \ Q \ \leq \ 5\ 000$  
$2 \ \leq \ 1 \ \leq M \ \leq 100$  
$3 \ \leq \ N, \ Q \ \leq 100\ 000$  
$4 \ \leq \ 30$  

The original constraints

The problem statement is a satire and should be treated as such.

## Example

`sever.in`  
`10 5`  
`1 6`  
`1 2`  
`3 4`  
`8 9`  
`2 3`  
`1 10`  
`6 7`  
`7 8`  
`4 5`  
`3 3 3 1 1`  
`2 2 2 4 5`  
`2 4 6 0 3 5`  
`3 5`  
`1 3`  
`1 9`  
`3 4`  
`2 7`  
`4 5`  
`5 3`  

`sever.out`  
`-1`

## Explanation