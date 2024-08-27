## Task

The city of $Salaj$ is very small $(VERY VERY VERY SMALL)$. The city has $N$ blocks $(in theory has 2,3 blocks but we will fictively assume that $N \leq 50$)$ and currently $0$ paths built between blocks $(in the end there will be $M$ such paths)$. A Salajen component is a component of blocks where from any block you can reach any other block $(in graph theory terms, it is also called a strongly connected component)$. Bored because he has nothing to do in his city $(because it is too small)$, $Razvan$ decided to play a game. Each time a new path is constructed, $Razvan$ writes down on a sheet of paper how many Salajen components exist in the city. In the end, after all $M$ paths have been built, $Razvan$ obtains a sequence of length $M$. After so much work, our character decides to go to the club but quickly realizes he is in $Salaj$ and doesn't have one. Upset, he wonders how many distinct sequences he can obtain based on how the $M$ paths are built. Note: there are multiple ways to obtain the same sequence but $Razvan$ is only interested in the number of distinct sequences. As a result, a sequence will be counted only once.

## Input data

The input file `salaj.in` will contain on the first line a natural number $T$, representing the number of tests. On the following $T$ lines there will be 3 natural numbers each: $N$, $M$ and $MOD$.

## Output data

The output file `salaj.out` will contain $T$ lines, with the $i$th line containing the answer for the $i$th test. A line will contain $M$ values. The $i$th value represents the number of sequences $Razvan$ can obtain modulo $MOD$ if he has $N$ blocks and $i$ edges $(where $N$, $M$, and $MOD$ are the respective test's values).

## Constraints and clarifications

$1 \leq N \leq 50$  
$1 \leq T \leq 10$  
$1 \leq M \leq N \times (N - 1)$  
A path is a directed edge  
$1 \leq MOD \leq 1\,000\,000\,000$  

Legend says that $Salaj$ is actually a county but nobody knows where it is.

## Example

`salaj.in`  
```
2  
5 10 666013  
6 9  
10 1  
2 4  
9 21  
50 110  
209 351  
546  
1  
2  
4  
9  
1  
1  
6  
0  
7  
```
`salaj.out`  
```
10 1  
2  
4  
9  
21  
50  
110  
209  
351  
546  
```