~[flareon.png|align=right|width=32.5%]

The city of Alexandria has been overrun by groups of durants, ant Pokémon! They have built $N$ anthills numbered from $1$ to $N$, connected by $N - 1$ bidirectional tunnels, so that it is possible to travel from one anthill to any other following the tunnels. We define the distance $d(i,j)$ as the minimum number of tunnels that must be traversed to get from anthill $i$ to anthill $j$.

Candela, the leader of Team Valor, has summoned $M$ flareons, the $i$-th of which is stationed near anthill $Pos[i]$ and has a **Lava Plume** move with power $Power[i]$. A **Lava Plume** attack with power $p$ carried out at anthill $i$ adds the value $max(0, p - d(i, j))$ to the destruction degree $Dmg[j]$ of anthill $j$.

We need to determine, for each anthill $i$, its destruction degree $Dmg[i]$ after the attacks of all $M$ flareons.

# Implementation
Your program should contain a function:
```cpp
void solve(int N, int M, int* V, int* Pos, int* Power);
```

The parameters $N$ and $M$ represent the number of anthills and the number of flareons, respectively. The parameter $V$ is an array of length $N - 1$, **indexed from 0**, with the element at position $i$ representing the existence of a tunnel between anthills $i + 2$ and $V[i]$. The parameters $Pos$ and $Power$ are two arrays of size $M$, **indexed from 0**, with the meaning that the $i$-th flareon is located at position $Pos[i]$ and has a **Lava Plume** move with power $Power[i]$.

Once you have found the $N$ degrees of destruction, you should call the function, implemented by the grader:
```cpp
void answer(long long* Dmg);
```
When you call this function, you must pass the parameter $Dmg$, an array of length $N$ indexed from $0$, with the $i$-th element representing the destruction degree of anthill $i+1$.

In addition to the function you will implement, you can declare local or global variables and implement other helper functions. It is recommended that global variables and functions be declared with the `static` modifier.

# Testing
To test your solutions locally, we provide the `main.cpp` program and the `flareon.h` header. The `main.cpp` program reads from the input file `flareon.in`, calls the contestant's `solve` function, and prints the $Dmg$ array passed as a parameter through the `answer` function in the `flareon.out` file.

The first line of the `flareon.in` file contains the natural numbers $N$ and $M$. The second line contains $N - 1$ natural numbers, representing the elements of the $V$ array. The next $M$ lines contain $M$ pairs of integers, the $i$-th pair representing the numbers $Pos[i]$ and $Power[i]$. In the output file `flareon.out`, there will be $N$ natural numbers, the $i$-th of which represents the number $Dmg[i]$.

# Constraints and Clarifications
* $1 \leq N \leq 200\ 000$
* $1 \leq M \leq 500\ 000$
* For `20%` of the tests, $N \leq 1\ 000$ and $M \leq 2\ 000$
* For `70%` of the tests, $N \leq 30\ 000$ and $M \leq 30\ 000$
* There can be multiple flareons near an anthill.

# Example
`flareon.in`
```
4 3
1 1 3
2 2
3 2
4 10
```
`flareon.out`
```
10
9
11
11
```
Explanation
---

The `solve` function will receive the parameters: $N = 4$, $M = 3$, $T = \{1, 1, 3\}$, $\text{Pos} = \{2, 3, 4\}$, $\text{Power} = \{2, 2, 10\}$. The direct paths between anthills are $(2, 1), (3, 1), (4, 2)$.