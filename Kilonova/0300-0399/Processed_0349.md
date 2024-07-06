# Stefan has become interested in drawing various pictures. In order to enhance his skills, he decided to combine his new passion, drawing, with his older passion, which is computer science.

Therefore, he decided to start with a matrix of size $n$ and $m$, which has on its $n \cdot m$ squares either $0$, $1$ or $\ast$. After that, he will want to draw the matrix in such a way that for each column, we will start with zeroes and then we will continue with ones.

In other words, we want for each column $j$ to have the first $i$ lines completed with $0$ and the remaining $n - i$ lines with $1$, by replacing the squares equal to $*$ with either $0$ or $1$. The squares which are initially completed with $0$ and $1$ cannot be replaced. The $i$ doesn't have to be the same for every column.

Now, he wants to find the number of matrices which respect the pattern described previously.

In order to make this challenge more interesting, he will also ask you the answer for two different situations: The first situation is when the number of zeroes on each column doesn't have any restrictions.

The second situation is when the number of zeroes on each column has to be at least equal to the number of zeroes from the previous column, for each column from $2$ to $m$.

Since this answer can be really big, we want its reminder when dividing by $10^9 + 7$.

# Task

The first line of the input contains $c$, the type of requirement which has to be solved ($c = 1$ or $c = 2$). The second line of the input contain $n$ and $m$, the size of the grid $(1 \leq n, m \leq 10^3)$.

The next $n$ lines of the input contain $m$ characters each, representing the grid $(a_{ij} = 0, 1$ or $\ast)$. The characters are not separated by spaces.

Each subproblem is worth $50$ points.

For each of the subproblems, there are tests worth $20$ points, such that ($1 \leq n, m \leq 100$) (for a total of $40$ points).

# Output

The output contains the answer modulo $10^9 + 7$.

# Examples

`stdin`
```
1
4 5
0**0*
*1***
**1**
1****
```
`stdout`
```
360
```

`stdin`
```
2
4 5
0**0*
*1***
**1**
1****
```
`stdout`
```
16
```