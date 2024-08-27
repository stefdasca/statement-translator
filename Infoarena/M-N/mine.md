Mine

After recovering his map, Max Damage finds himself once again in the car chased by the police. To escape, he decides to hide in an abandoned mine. The problem is that it is dark inside, and after so many "collisions" the headlights no longer light up. He starts an old electricity generator to illuminate the mine's galleries, but it works strangely and sometimes provides more electricity, other times less. Fortunately, Damage knows how the amount of electrical energy varies. He also has a map of the mine. It is made up of galleries that connect at intersections. There can be any number of galleries between two intersections, two galleries only meet at intersections, and a gallery can be traversed in both directions. Max also knows for each gallery what the minimum amount of electricity produced by the generator should be to be safely traversed. All galleries have the same length and can be traversed in a single time interval (obviously, if there is enough light). So all he needs now is a plan.

## Task

Max wants to get from the main entrance (intersection number $1$) to the emergency exit (intersection number $N$), and you will have to tell him how quickly he can do that.

## Input data

The file `mine.in` contains on the first line $N$ (the number of intersections) and $M$ (the number of galleries). On the following $M$ lines, 3 numbers $i$ $j$ $k$ are read with the meaning that there is a gallery from intersection $i$ to intersection $j$ and the minimum amount of electricity required is $k$. On the next line, $W$ is found, followed by $W$ values. The $q$-th value represents the amount of electrical energy generated at moment $q$.

## Output data

In the file `mine.out` a single number $t$ will be written, the minimum time in which Max can exit the mine, or $-1$ if he has no chance.

## Constraints and clarifications

$1 \leq N \leq 10^4$

$1 \leq M \leq 10^5$

$1 \leq W \leq 10^6$

The minimum electricity requirement for an edge ranges between $0$ and $10^9$

Max Damage can wait any amount of time at an intersection

If the sequence of $W$ values ends, the generator stops and no one wants to stay in an abandoned mine in the dark (even if the last galleries to the exit have the value $k$ equal to $0$)

## Example

`mine.in`
```
3
2
1 2 5
2 3 10
5
2 6 9 10 0
4
```

`mine.out`
```
4
```

## Explanation

Max stays at time $1$ in intersection $1$, at time $2$ he moves to intersection $2$, at time $3$ he stays put, and at time $4$ he moves to intersection $3$.