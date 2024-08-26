# Infestation

Lora's villa is invaded by rats. Fortunately, we can describe the rooms in Lora's villa as a tree rooted at node $1$, which has $N$ nodes. Initially, no node is infested. Several events occur consecutively, each of them being one of the following $4$ types:
- "1 X" - Node $X$ becomes infested.
- "2 X" - Lora wants to eliminate the rats from the nodes on the path from node $1$ to node $X$ (inclusive) using ultrasound simultaneously on all of them. If the ultrasound is used on an infested node, the rats scatter, and each of its direct neighbors, where the ultrasound is not used at the current moment, becomes infested. The nodes where the ultrasound is used stop being infested. After the rats have moved, the ultrasound stops, meaning the liberated nodes can become infested again in the future.
- "3 X" - Lora hires professionals to free node $X$ and its children. Consequently, $X$ and all its direct successors are no longer infested.
- "4 X" - Lora wants to know the total number of infested nodes in the subtree of node $X$. The subtree of node $X$ is defined as the set of nodes that contain $X$, as well as all its direct or indirect successors (see the example for more information).

## Input data

The input file infestation.in will contain on the first line the natural number $N$ - the number of nodes in the tree. The second line contains $N-1$ numbers, the $i$-th being $p_{i+1}$ - the parent of node $i+1$. The third line contains the number of events $Q$. The next $Q$ lines contain two integers each, representing an event in one of the previously mentioned formats.

## Output data

The output file infestation.out will contain for each event of type $4$ a single number on a line - the number of infested nodes in the subtree.

## Constraints

$$1 \leq N, Q \leq 3 \* 10^5$$ 

### Subtasks

* Subtask Points

$1 \leq 2 \* 10^3$

  * Event types 1, 2, 3, 4
    
$8 \leq 3 \* 10^5$

  * Event types 1, 4
    
$10 \leq 3 \* 10^5$

  * Event types 1, 2, 3, 4

  * The tree is randomly generated*
     
$9 \leq 3 \* 10^5$

  * Event types 1, 3, 4
    
$23 \leq 3 \* 10^5$

  * Event types 1, 2, 3, 4

  * Each node has at most $4$ children

$17 \leq 10^5$

  * Event types 1, 2, 3, 4
    
$26 \leq 3 \* 10^5$

  * Event types 1, 2, 3, 4

* To generate a random tree for each node $i$, its parent (i.e., $p_i$) is generated as a random integer in the interval $[1, i - 1]$. 

## Example

infestation.in
```
5
1 1 3 3
8
1 3
2 5
4 1
1 1
2 1
4 3
3 1
4 3
```

infestation.out
```
1
2
1
```

## Explanations

The events have the following effects:
- "1 3" - Node $3$ becomes infested.
- "2 5" - Lora uses ultrasound on the nodes on the path from $1$ to $5$. These are nodes $1$, $3$, and $5$. Node $3$ is infested and its only neighbor without ultrasound is node $4$. Therefore, node $3$ is no longer infested and node $4$ becomes infested.
- "4 1" - The subtree of node $1$ consists of all the nodes in the tree. The only infested node is node $4$.
- "1 1" - Node $1$ becomes infested.
- "2 1" - Lora uses ultrasound on node $1$. Nodes $2$ and $3$ become infested, while node $1$ is no longer infested.
- "4 3" - The subtree of node $3$ consists of nodes $3$, $4$, and $5$. Among them, nodes $3$ and $4$ are infested.
- "3 1" - Node $1$ and its direct successors, namely nodes $1$, $2$, and $3$, are no longer infested.
- "4 3" - Among nodes $3$, $4$, and $5$, only node $4$ is infested.