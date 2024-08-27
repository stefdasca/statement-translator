## Task

In another episode where Rick and Morty go to save Atlantis, the Citadel is, once again, in danger due to a lost Portal Gun. The Morty Resistance, having obtained this weapon, plans a revolution by creating a system of portals, in the form of a hidden tree, between $n$ main locations (numbered from $1$ to $n$). Knowing that the size of the Citadel is overstressed, the Rick Militia can forcibly change the portal network to manage it. Thus, they can input the coordinates of two key locations $(a,b)$ into a Portal Gun, determining one of two possibilities: the gun returns $(0,0)$ indicating that a portal already exists between $a$ and $b$ or returns a pair $(x,y)$ indicating that a new portal will open between $a$ and $b$, while the portal between $x$ and $y$ will close to prevent the appearance of a cycle, maintaining the tree shape of the network. Help the Rick Militia find the portal system to prevent unnecessary harm to the Mortys.

Interaction

Initially, read from stdin the number $T$ representing the number of tests. For each test, read then $N$ the number of nodes of the tree. Your program is allowed to issue queries by writing to standard output:
"? $a$ $b$" representing inputting a pair into the Portal Gun. After each such query, the interactor will respond on stdin as follows:
"$0$ $0$": if the edge $(a,b)$ already exists in the tree.
"$x$ $y$": if the edge $(a,b)$ does not exist, the pair $(x,y)$ represents the edge that will be removed from the graph with the addition of the edge $(a,b)$ to maintain the tree shape.
After finding out the edges of the tree, print "!" on a single line followed by $n-1$ lines with "$a$ $b$" indicating there is an edge between $a$ and $b$. After each query and after you print the result of a test, you need to print '\n' and flush the standard output. For flushing, you can use the following table:

Language
C/C++
Required header
#include <stdio.h> // flush(stdout); 

Pascal
Function
flush(output);

Python
flush(output)
sys.stdout.flush()

Java
System.out.flush()

Rust
use std::io::{self,Write}; 
io::stdout().flush().unwrap(); 

## Constraints and clarifications

After calling the query, a cycle is first formed, then the edge to be deleted is chosen by excluding the most recently added one.
$T = 30$
$3 \leq N \leq 100$

Scoring

Within a test:

Let $Q$ = number of queries made;

Let Opt = optimal number of queries;

Then the score on that test will be:

if $Q \leq Opt + 5$: 100 points

if $Q \leq Opt + 10$: $100 - (Q - Opt - 5) \times 5$ points

otherwise: 0 points

Within a subtask, the score will be equal to the minimum score among its tests:

Subtask 1: the interactor is random - 30 points

Subtask 2: the interactor is adaptive - 70 points

## Example

```
Stdin

2
3
```

```
Stdout

? 1 3
0 0
? 2 3
0 0
! 1 3
2 3
```

## Explanation

$2$
$3$
We find the number of tests and the number of nodes in the first tree 
```
? 1 3
```
Edge $1$ $3$ is added 
```
0 0
```
The operation returns that edge $1$ $3$ already exists in the tree 
```
? 2 3
```
```
0 0
```
The gun returns that edge $2$ $3$ already exists in the tree 
```
! 1 3
2 3
```
We then display the edges of the first tree 
```
3
```
The second tree is given 
```
? 1 2
```
We call the function for edge $1$ $2$
```
1 3
```
We find that edge $1$ $3$ was deleted to introduce edge $1$ $2$ 
```
! 1 2
2 3
```
By elimination, we know that edge $2$ $3$ is in the tree