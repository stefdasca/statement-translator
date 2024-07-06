~[desen.png|align=right|width=20%]

At the drawing class, Gigel received a task to create a drawing following the next algorithm:
**Step $1$**: a triangle, numbered with $1$, is drawn, as in **Figure $1**;
**Step $2$**: triangle $1$ is divided into three polygons (a rectangle and two triangles numbered $2$ and $3$) by drawing two segments as in **Figure $2**;
**Step $3$**: each of the two triangles obtained in **Step $2**, is divided into a rectangle and two triangles (numbered 4, 5, 6, 7) by drawing two segments as in **Figure $3**;
**Step $4**: each of the four triangles obtained in **Step $3**, is divided into a rectangle and two triangles (numbered $8$, $9$, $10$, $11$, $12$, $13$, $14$, $15$) by drawing two segments as in **Figure $4**;
$\\dots$
**Step $N**: each triangle of the triangles obtained in **Step $N-1**, is divided into a rectangle and two triangles by drawing two segments. If the value of $K$ is the last number used for numbering the triangles obtained in **Step $N-1**, then the triangles resulting from **Step $N** will be numbered with consecutive distinct natural numbers $K+1$, $K+2$, $K+3$, $\\dots$, etc.

# Task

Write a program that reads the natural number $K$ and determines:
1. The **smallest** number $X$ and the **largest** number $Y$ among the numbers used for numbering the triangles obtained at the step where the triangle numbered $K$ is obtained;
2. The numbers of the triangles that were divided according to the algorithm in the statement in order to obtain the triangle numbered $K$.

# Input data

If $C=1$, the first line of the output file `desen.out` contains the two natural numbers $X$ and $Y$, separated by a single space, representing the answer to task $1$ of the problem.
If $C=2$, the first line of the output file `desen.out` contains a sequence of natural numbers sorted in ascending order, separated by a single space, representing the answer to task $2$ of the problem.

# Output data

The first line of the output file `desen.out` will contain a single integer, the sum of the two numbers.

# Constraints and clarifications
* $2 \leq K \leq 9\ 223\ 372\ 036\ 854\ 775\ 807\ (=2^{63}-1)$;
* Only the triangles are numbered;
* For the correct solving of task $1$, $40$ points are awarded;
* For the correct solving of task $2$, $60$ points are awarded.

# Example 1

`desen.in`
```
1
13
```

`desen.out`
```
8 15
```

## Explanation

The task is $1$, $K=13$. As shown in Figure 4, at Step 4 the triangles numbered $\\textbf{X=} \\ 8$, $9$, $10$, $11$, $12$, $13$, $14$, $\\textbf{Y=} \\ 15$ are obtained.

# Example 2

`desen.in`
```
2
13
```

`desen.out`
```
1 3 6
```

## Explanation

The task is $2$, $K=13$. As shown in Figure 4, the triangle numbered $K=13$ is obtained from triangle $6$. Triangle $6$ is obtained from triangle $3$ which is obtained from triangle $1$.