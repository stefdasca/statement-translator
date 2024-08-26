## Task

I believe everyone has played Rayman and knows the protagonist. New levels have appeared in the famous game and you have the duty to tell Rayman where to go. A level consists of several mountains of different heights, each with an obstacle of a certain risk level at the top. More precisely, the level looks like a matrix with $N$ rows and $M$ columns, and each cell in the matrix represents a mountain with an obstacle. Because Mister Dark, Admiral Razorbeard, Andre, and The Magician have joined forces and invented a potion that robs Rayman of his flying ability, he can only jump from one mountain to another with a height less than or equal to the current one. We all know that Rayman loves adventure, so he wants to go through as many obstacles as possible, but we also know that Rayman is superstitious, so he does not want to turn back (he believes that Mister Unlucky will come upon him and kill him). More precisely, if at some moment he is on a mountain at row $x$ and column $y$, in the future, he can only reach a mountain at row $x$ and column $y1$ if $y < y1$ (in other words, the sequence of moves cannot be reversed). However, we also know that as fearless as Rayman is, he does not want to take many risks, so you need to choose a path for him that goes through as many obstacles as possible but with the minimum total risk (in case of a tie by length). Because he does not like to waste time choosing from multiple routes and wants to leave as soon as possible, he guarantees that there is only one set of obstacles with the maximum cardinality that can be traversed under the above conditions, with the minimum total risk (the actual path is not necessarily unique). But because the game has evolved significantly since its first appearance in 1995, and because we are in the year 2015, and because we managed to get through the year 2013 just fine, there is an energy coefficient, namely: let $E$ be an $N$×$N$ square matrix with the meaning $E[i][j]$ is the energy consumed to jump from a mountain at row $i$ to a mountain at row $j$. But everyone knows that Rayman can jump very far and the energy consumption for a jump does not depend on the length of the jump but rather depends on the jump itself, so he consumes more energy if he jumps through an intermediate stone. In other words, it is guaranteed that $E[i][j] \leq E[i][k] + E[k][j]$, for any $k$. Of course, Rayman wants to have as much energy as possible for obstacles, so you also need to choose a path that consumes as little energy as possible if there are multiple paths with the same cardinality and total risk. Rayman can start from anywhere. Rayman will reward you with 100 points if you help him get through all the levels.

## Input data

The first line of the file `rayman.in` contains two natural numbers $N$ and $M$ with the above meanings. The next $N$ lines contain $M$ numbers each, representing the heights of the mountains. The input file also contains another $N$ lines with $M$ numbers each, representing the risk levels of the obstacles. The following $N$ lines contain $N$ numbers each, representing the matrix $E$.

## Output data

The file `rayman.out` must contain 3 numbers $Nrmax$, $Riscmin$, and $Energmin$ separated by a space. $Nrmax$ represents the maximum number of obstacles, $Riscmin$ represents the minimum risk assumed to pass $Nrmax$ obstacles, and $Energmin$ is the minimum energy consumed to pass $Nrmax$ obstacles with the risk level $Riscmin$.

## Constraints

$1 \leq N \leq 15$  
$1 \leq M \leq 10$  
$5$  
$1 \leq$ height of a mountain $\leq 10$  
$6$  
$0 \leq$ risk level of an obstacle $\leq 10$  
$9$  
$0 \leq$ energy consumed for a jump $\leq 1000$  
$E[i][i] = 0$, for $1 \leq i \leq N$  
Attention! Large volume of input data, we recommend optimizing the reading using this code.  
Full feedback!  

Subtask 1 (15 points):  
• $1 \leq M \leq 1000$  
• the heights of the mountains are all distinct

Subtask 2 (20 points):  
• $1 \leq N \leq 8$  
• $1 \leq M \leq 1000$  

Subtask 3 (25 points):  
• $E[i][j] = 0$, $1 \leq i \leq N$, $1 \leq j \leq N$  

Subtask 4 (40 points):  
• Initial constraints

## Example

`rayman.in`

```
3
8 3 2 4 6 2 1 4 2 5 8 7 6 11 4 9 10 1 1 14 12 5 8 10 20 1 1 5 4 1 1 4 6 5 1 2 1 6 1 8 10 3 3 1 1 1 2 3 2 0 1 2 3 0 2 2 1 0 11 12 7
```

`rayman.out`

```
10 6 14
```

## Explanation

The path Rayman follows is: $(3, 3) \rightarrow (3, 4) \rightarrow (2, 2) \rightarrow (2, 3) \rightarrow (2, 4) \rightarrow (3, 5) \rightarrow (2, 6) \rightarrow (1, 1) \rightarrow (1, 2) \rightarrow (1, 5) \rightarrow (1, 6)$