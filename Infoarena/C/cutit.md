# Cut It

I've spoiled your appetite for pizza with this problem. Probably the sharpest problem in the entire contest (hopefully not the corniest joke). Your little sister, Taurina, has her birthday coming up. Taurina is somewhat interested in computer science (of course, not as much as you, but you hope that one day she will follow in your footsteps), which is why you thought of a very special gift for a special girl: an undirected graph! Taurina loves cutting things, especially undirected graphs. You remember from your algorithms and data structures classes that a cut in a graph is a partition of the set of nodes into two non-empty subsets. You realize that as soon as you give it to her, Taurina will start cutting the graph in all possible ways and marveling at what she obtains. Since you are a good brother and Taurina is an obedient little sister, you agree that she will not make too much mess. Thus, Taurina will only make those cuts in which both subsets are connected (in other words, if we were to look at the graph formed by each of the two complementary subsets of nodes and the edges connecting them, it remains connected). Thus, there will be only two resulting pieces, and the mess will be minimized. You thought a lot about this gift and decided to give Taurina a graph that has exactly $K$ "beautiful" cuts. Moreover, for financial reasons, you cannot afford a graph with more than $80$ nodes, so the budget must be chosen carefully. You look at the calendar. Her birthday is today. Hurry up, you don't want to give her sparkling water, like in previous years!

## Input data

The input file `cutit.in` will contain a single natural number, $K$.

## Output data

The output file `cutit.out` will contain:
- the first line will contain two natural numbers $N$, $M$, representing the number of nodes and the number of edges of the gift-graph, respectively.
- the following $M$ lines, each containing a distinct edge of the graph, given by a pair $(u, v)$ with the meaning "there is an undirected edge between nodes $u$ and $v$"

## Constraints and clarifications

$1 \leq K \leq 10^4$
The displayed graph must have at least 1 node
The displayed graph must be connected
The displayed graph must have at most 80 nodes

## Example

`cutit.in`
$4$

`cutit.out`
$4$ $4$
$1$ $2$
$2$ $3$
$3$ $1$
$3$ $4$

## Explanation

There are exactly $4$ cuts that meet the condition in the statement:
- $\{ 1 \}$, $\{ 2, 3, 4 \}$
- $\{ 2 \}$, $\{ 1, 3, 4 \}$
- $\{ 4 \}$, $\{ 1, 2, 3 \}$
- $\{ 1, 2 \}$, $\{ 3, 4 \}$