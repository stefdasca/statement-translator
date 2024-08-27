## Task 

Let $T$ be an undirected tree with $N$ nodes. We will apply $M$ operations on it of the following types:

$1 \ x \ y$ The edge $x-y$ is deleted from the tree.

$2 \ x \ y$ The question is asked "Is there a path in the tree from node $x$ to node $y$?"

The task is for your program to display the correct answer for all operations of type $2$. 

## Input data

The input file `disconnect.in` will contain on the first line the numbers $N$ and $M$, indicating the number of nodes and the number of operations to be performed on the tree, respectively. The following $N - 1$ lines contain pairs of numbers $X \ Y$, indicating that there is an undirected edge between nodes $X$ and $Y$. The next $M$ lines contain three numbers $type \ X \ Y$. The number $type$ denotes the type of operation, being equal to $1$ if it is a deletion or $2$ if it is a question. The numbers $X$ and $Y$ will be used to generate the nodes on which the respective operation will be applied. Specifically, these nodes will be $A = X \ xor \ V$ and $B = X \ xor \ V$ where $V$ is an initially zero variable. After each operation of type $2$ the variable $V$ will change its value to $A$ (if the answer to the question was positive), or to $B$ (if it was negative).

We provide a fragment of C++ code that generates and solves the operations. 
```
int V = 0;  
for (int i = 0; i < M; ++i) { 
    int type, x, y; 
    cin >> type >> x >> y;  
    int a = x xor V; 
    int b = y xor V;  
    if (type == 1) { 
        removeEdge(a, b); 
    } else if (query(a, b)) { 
        cout << "YES\n"; 
        V = a; 
    } else { 
        cout << "NO\n"; 
        V = b; 
    } 
} 
```

## Output data

The output file `disconnect.out` will contain one line for each operation of type $2$. The line will contain `YES` if the answer is positive and `NO` otherwise. 

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 500\ 000$

### Clarifications

For 20% of the points the tests satisfy the constraint

$1 \leq N \leq 1\ 000$ 

$1 \leq M \leq 5\ 000$ 

For 40% of the points the tests satisfy the constraint

$1 \leq N \leq 10\ 000$ 

$1 \leq M \leq 500\ 000$ 

The xor operation can be implemented with the operator "^" or "xor" in C/C++ and with the "xor" operator in Pascal. 

## Example

`disconnect.in` 
```
6 7
1 2
1 3
1 4
4 5
4 6
2 2 5
1 3 6
2 0 7
2 7 6
2 7 4
1 4 7
2 6 7
```

`disconnect.out` 
```
YES
NO
YES
YES
NO
```

## Explanation

Once the operations are generated, they would appear as follows: 

$2 \ 2 \ 5$ 

$1 \ 1 \ 4$ 

$2 \ 2 \ 5$ 

$2 \ 2 \ 3$ 

$2 \ 5 \ 6$ 

$1 \ 1 \ 2$ 

$2 \ 3 \ 2$