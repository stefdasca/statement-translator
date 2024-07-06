Here is the translated text:

Fie $G$ un graf neorientat conex. Fiecare muchie $e$ are la momentul $t$ un cost dat de o funcție polinomială de gradul al doilea $fe(t) = a_e \cdot t^2 + b_e \cdot t + c \cdot e$. 

# Task

Găsiți timpul $t$ la care costul arborelui de acoperire minim al lui $G$ este cât mai mic posibil, precum și acest cost. 


# Input data

The file `mst.in` contains:

- The first line contains two natural numbers $N$ și $M$, separated by a space, representing the number of nodes in the graph, and the number of edges, respectively. On line $i + 1$, there are the numbers $u_i \ v_i \ a_i \ b_i \ c_i$, separated by a space, where $u_i$ și $v_i$ are the endpoints of the edge, and $a_i$, $b_i$, $c_i$ are the coefficients of the polynomial function.

# Output data

The file `mst.out` should contain two real numbers with exactly $6$ decimal places on the first line, the first being the sought time and the second being the cost of the minimal spanning tree at that moment.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $1 \leq M \leq 100$
* $0 \leq u_i, v_i < N$, for any $1 \leq i \leq M$.
* Coefficients $a_i, b_i, c_i$ are integers whose absolute value does not exceed 10^6, for any $1 \leq i \leq M$.
* Coefficient $a_i > 0$, for any $1 \leq i \leq M$.
* The time $t$ can be any value on the real axis.
* The functions associated with the edges are distinct pairwise.
* Results will be considered correct if they do not have an error greater than $10^{-6}$ (the sixth decimal place can differ by at most one unit).

# Example

`mst.in`
```
3 3
0 1 1 -2 1
1 2 1 -2 5
0 2 1 -8 16
```

`mst.out`
```
1.000000 4.000000
```

## Explanation

The functions associated with the edges are:

* $f(0,1)(t) = t^2 - 2t + 1$,
* $f(1,2)(t) = t^2 - 2t + 5$, 
* $f(2,0)(t) = t^2  - 8t + 16$. 

The minima of the functions $f(0,1)$, $f(1,2)$ are reached at time $t = 1$ and their sum is $4$.