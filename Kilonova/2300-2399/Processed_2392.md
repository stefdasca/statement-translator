In Alba County, there are $n$ localities numbered from $1$ to $n$. Between these localities, there is a network of bidirectional roads such that between any two localities, there is exactly one path which may be either direct or through other localities. There are $n-1$ pairs of localities with the property that there is a direct road between the localities forming a pair. The lengths of these direct roads are known.
The TOL company produces consumer goods; it has a factory in the county seat, which is locality number $1$, and $n-1$ stores, one in each of the other $n-1$ localities of the county. To transport products from the factory to the $n-1$ stores, TOL has $p$ trucks available. Since the factory products are neither voluminous nor heavy, the trucks have practically unlimited capacity, so any truck could supply all the stores in the county in a single trip. A truck's trip must always start at the factory (i.e., in locality $1$), may pass multiple times through a locality, and can end in any locality of the county; it is not necessary for the truck to return to locality $1$ at the end of the trip. 
The cost of such a trip is directly proportional to the distance traveled. The trucks are quite old, so they can only make a single trip (regardless of its length). 
The TOL company programmer is tasked with creating a planning schedule that determines the routes for at most $p$ trips such that all the county's $n-1$ stores are supplied, and the sum of the distances traveled by the trucks on these trips is minimal. He is struggling with the program but knows that the national informatics team is in Alba Iulia. Thus, he asks for your help to solve the problem.

# Task
Write a program that determines a planning schedule for at most $p$ trips such that all the $n-1$ stores are supplied, and the sum of the distances traveled by the trucks on these trips is minimal.

# Input data
The file `camion.in` contains:
− The first line contains two positive natural numbers $n$ and $p$ with the meanings mentioned above;
− Each of the following $n-1$ lines contains $3$ positive natural numbers $v1, v2, d (v1 \neq v2)$ separated by a space, meaning: there is a direct road of length $d$ between localities $v1$ and $v2$.

# Output data
The file `camion.out` will contain a single line that will contain the sum of the distances traveled by the trucks.

# Constraints and clarifications
* $n \leq 1\ 000$; for $15 \%$ of the tests $n \leq 20$
* $p \leq 25$
* There are no two localities between which there are two direct roads.
* The length of a direct road does not exceed $100$ and is a non-zero number.

# Example 1

`camion.in`
```
5 1
1 2 10
3 1 7
4 3 1
3 5 2
```

`camion.out`
```
30
```

## Explanation

Only one truck is used; the trip follows the route: $1 \rightarrow 3 \rightarrow 4 \rightarrow 3 \rightarrow 5 \rightarrow 3 \rightarrow 1 \rightarrow 2$
The sum of the distances is: $7+1+1+2+2+7+10=30$

# Example 2

`camion.in`
```
5 3
1 2 10
3 1 7
4 3 1
3 5 2
```

`camion.out`
```
21
```

## Explanation

Two trucks are used; the two trips are: $1 \rightarrow 3 \rightarrow 4 \rightarrow 3 \rightarrow 5$ and $1 \rightarrow 2$. 
The sum of the distances is: $7+1+1+2+10=21$