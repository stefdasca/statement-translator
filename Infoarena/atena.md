# Athena

In ancient Greece, the street network of any city consisted of intersections connected by bidirectional roads, constructed such that from any intersection one could reach any other intersection, directly or indirectly, by passing through other intersections. Moreover, between any two intersections in a city, there was at most one direct road, and there were no roads from an intersection to itself. It is known that in those times, the street network of the city of Athens had $N_1$ intersections, connected by $M_1$ bidirectional roads, while the street network of the city of Sparta had $N_2$ intersections, connected by $M_2$ bidirectional roads. The intersections in Athens are considered numbered from $1$ to $N_1$, while the intersections in Sparta are considered numbered from $N_1+1$ to $N_1+N_2$. Pericles, the king of Athens, decided to find out to what extent the street network of Sparta resembles the street network of Athens. To this end, he asked one of the Athenian mathematicians, Parmenides, to find out if the street network of Sparta is included in the street network of Athens. Pericles considers the street network of Sparta to be included in the street network of Athens if and only if there exist disjoint non-empty subsets $A_1, A_2, \dots, A_{N_2}$ of the set $\{1, 2, \dots, N_1\}$ such that for any road between two intersections $N_1+a$ and $N_1+b$ in Sparta, there is a road between an intersection $c$ and an intersection $d$ in Athens, with $c$ in $A_a$, $d$ in $A_b$ and $1 \leq a, b \leq N_2$, $1 \leq c, d \leq N_1$. Unfortunately, Parmenides died while he was on his way to the Applied Mathematics Congress in Syracuse, so the task now falls to you. However, Parmenides mentioned in passing before he left that the solution to the problem essentially relies on the following two properties of the street network in Athens: $N_1 \geq 2*M_2$; No matter which intersection $a$ you choose in Athens and any other 3 distinct intersections $b$, $c$, and $d$ connected by direct roads to $a$, there is a direct road between $b$ and $c`$ or between $c$ and $d` or between $b$ and $d` (there can also be two of these direct roads or even all three together). Write a program that determines if the street network of Sparta is included in the street network of Athens, as defined by Pericles. If the answer is affirmative, then the program must also determine the sets $A_1, A_2, \dots, A_{N_2}$.

## Input data

The input file `atena.in` has the following structure: the first line contains two natural numbers $N_1$ and $M_1$, representing the number of intersections in Athens, and the number of bidirectional roads between them, respectively; on each of the next $M_1$ lines are written two natural numbers separated by a space $x$ $y$ $(1 \leq x, y \leq N_1)$ with the significance that there is a road between intersections $x$ and $y$ in Athens; the next line contains two natural numbers $N_2$ and $M_2$, representing the number of intersections in Sparta, and the number of bidirectional roads between them, respectively; on each of the next $M_2$ lines are written two natural numbers separated by a space $x$ $y$ $(N_1+1 \leq x, y \leq N_1+N_2)$ with the significance that there is a road between intersections $x$ and $y$ in Sparta.

## Output data

The output file `atena.out` shall contain on the first line the word `DA` if the street network of Sparta is included in the street network of Athens or `NU` if it is not included. Only in the case when the first line contains `DA`, $N_2$ lines will follow with the following structure: on line $i+1$ $(1 \leq i \leq N_2)$ there will be an integer $p_i$ representing the number of elements in the set $A_i$, followed by a space, and then by $p_i$ integers separated by spaces, representing the elements in set $A_i$ in any order. Each element in set $A_i$ must be a natural number between $1$ and $N_1$. If there are multiple solutions, then any of them is considered correct.

## Constraints and clarifications

$1 \leq N_1, N_2 \leq 100,000$  
$1 \leq M_1, M_2 \leq 200,000$  
$N_1 - 1 \leq M_1$  
$N_2 - 1 \leq M_2$  
For all tests used for grading, the street network of Athens satisfies the two properties stated by Parmenides.

## Example

`atena.in`  
```
6 6
1 2
2 3
3 4
4 5
5 6
1 6
3 3
7 8
8 9
9 7
```

`atena.out`  
```
DA
2 1 4
1 2
1 3
```

## Explanation

In the example above, the street network of Athens consists of 6 intersections connected by 6 roads, while the street network of Sparta consists of 3 intersections connected by 3 roads. The first property stated by Parmenides is verified because $6 \geq 2 * 3$. Since Athens does not contain intersections incident to at least 3 roads, the second stated property is also verified. We can choose disjoint and non-empty sets. For the road between $7$ and $8$, there is a road between $1$ and $2$, for the road between $8$ and $9$, there is a road between $2$ and $3$, and for the road between $9$ and $7$, there is a road between $4$ and $3$. Therefore, according to the definition given by Pericles, the street network of Sparta is included in the street network of Athens.