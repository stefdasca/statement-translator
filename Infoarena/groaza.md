## Task

To avoid fainting keep repeating: it's only a movie, it's only a movie "The Last House on the Left (1972)" tagline The last time Marcel watched a horror movie, he remembered the time when he was scared (as a cute and innocent little kid) of Grigorian tunnels. Now that he has grown up (attended a university, touched a probability course, etc.), he decided to tackle this issue from a new perspective. $\dots$ It's just a programming problem. It's just a programming problem. You are given two numbers $N$ and $M$. Construct an undirected connected graph with $N$ nodes and $M$ distinct edges with endpoints in different nodes, such that the following algorithm has an expected number of steps as large as possible (not necessarily the maximum possible, see the Scoring section):

You start at node 1

As long as you haven't reached node $N$

From the edges incident to the current node, randomly choose one (all edges have the same probability of being chosen) and move to the node indicated by it.

## Input data

The input file `groaza.in` contains on the first line the numbers $N$ and $M$.

## Output data

The output file `groaza.out` contains $M$ lines, each containing two numbers separated by a space, representing the endpoints of one of the edges.

## Constraints

$2 \leq N \leq 50$   
$N - 1 \leq M$   
$M \leq \frac{N * (N - 1)}{2}$   

Scoring Each of the 5 evaluation tests will be scored independently (the tests are not grouped). Thus, out of the 20 possible points per test, a portion will be awarded based on the case:

If the displayed graph does not contain exactly $M$ edges,  
or the edges are not distinct,  
or one has endpoints in the same node,  
or the graph is not connected:  
0 points are awarded  

Otherwise, the expected number of executions of instruction 3 in the pseudocode, $E$, will be calculated and compared with $X$, the same value but obtained for the graph found by $\dots$ the committee; points are awarded.

Very important is that the score obtained is preliminary! At the end of the contest, the committee reserves the right (actually, they already have it) to run any submitted source locally and replace number $X$ (defined above) with number $E$ (obtained by this source), in case $E > X$. Then all sources for this problem are re-evaluated.

Remember that only the last submission counts in the ranking. The first implication: Scores can drop, meaning the feedback received during the contest may not match the final ranking. (Theoretically, they can also increase if some non-deterministic solutions find a more advantageous graph on reevaluation.) The second implication: A very suitable graph for the task may be rewarded not only with the maximum score on the test but also by increasing the score difference from other competitors (alongside the committee's tacit acknowledgment of being intellectually surpassed by the ingenuity of the competitor).

Important note: Regarding non-deterministic sources. Both the initial $X$ number and the final $X$ number will be obtained by running sources that display the same graph at each run, meaning they are deterministic regarding the result. Also, these sources do not run in a time exceeding the problem's time limit.

Firstly, this means that there will always be a deterministic solution to get the maximum score. Secondly, non-deterministic sources will not be considered for this race to the best obtained graph. Also, be aware that source reevaluation can happen multiple times before the results for this problem are displayed, so non-deterministic sources might not be as lucky as they wish.

Some values for $N$ and $M$ in tests are known:

test \#1 \#2 \#3 \#4 \#5  
$N$ $50$ $10$ $23$ $? ?$  
$M$ $49$ $40$ $? 52 ?$  

## Example

`groaza.in 4 3` 

`groaza.out 1 2 2 3 3 4` 

## Explanation

For the displayed graph, the example from the Tunnel of Horror problem teaches us that $E$ would be equal to $9$. Whether we believe those who worked on that example or not, we do not know the value of $X$, nor what the maximum possible for $N = 4$ and $M = 3$ is.