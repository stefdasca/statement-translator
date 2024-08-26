# Distances

A good friend of Zaharel, Bronzarel is in the hospital suffering from typhoid. Being good friends, Zaharel goes to visit him. The last time he visited, Bronzarel had drawn several connected undirected graphs with weights on the hospital walls (yes, Bronzarel is also passionate about computer science!) and moreover, had calculated for each of these the minimum distances from a chosen source node to all the others. Zaharel, curious as always, decided to see if Bronzarel was delirious or not and wrote down on a piece of paper what he had written on the walls. When he got home, he decided to see for which graphs the minimum distances calculated by Bronzarel were correct.

## Task

Write a program that helps Zaharel determine for each graph if the minimum distances were calculated correctly.

## Input data

The input file `distante.in` will contain on the first line a number $T$, representing how many graphs are on the paper. The following lines will describe successively each graph. The first line of a graph description will contain the numbers $N$, $M$, and $S$ representing the number of nodes, the number of edges, and respectively, the source node from which the minimum distances are calculated. The second line of the description contains $N$ elements $D_1$ $D_2$ $\dots$ $D_N$ representing the minimum distances calculated by Bronzarel. The following $M$ lines will contain three natural numbers $a$ $b$ $c$ representing that there is an edge with weight $c$ from $a$ to $b$. 

## Output data

The output file `distante.out` will contain $T$ lines, each with either the word `DA` if the minimum distances were calculated correctly for the respective graph, or `NU` otherwise.

## Constraints and clarifications

$0 \leq T \leq 10$ 

$1 \leq a, b, S \leq N \leq 50000$ 

$0 \leq M \leq 100000$ 

$0 \leq c \leq 1000$ 

## Example

`distante.in` 
```
2 
5 6 1 
0 1 7 3 6 
1 2 1 
1 3 7 
1 4 3 
3 4 4 
2 5 5 
4 5 6 
4 4 2 
1 0 2 3 
1 2 1 
2 3 1 
2 4 1 
3 4 1 
```

`distante.out` 
```
DA 
NU 
```