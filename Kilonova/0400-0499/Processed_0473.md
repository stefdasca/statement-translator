```markdown
Quantum Computing is a new technology that uses the properties of quantum mechanics to perform certain computations in a much shorter time than a classical computer is capable of. The fundamental difference between a classical computer and a quantum computer is the way they process information. A classical computer processes information using bits, which can be $0$ or $1$. On the other hand, a quantum computer uses qubits, which can simultaneously have the value $0$ (denoted by $| 0 \\rangle$) and the value $1$ (denoted by $| 1 \\rangle$) - we say that the qubit is in the quantum state $| \\psi \\rangle = \\alpha | 0 \\rangle + \\beta |1 \\rangle$. By making modifications to these qubits, we can develop quantum algorithms with better complexity than the best existing classical algorithms. However, quantum computers do not yet have practical utility because they do not have a sufficiently large number of qubits (currently, the most powerful quantum computers have a few hundred qubits). For simplicity, we will work only with pure states ($| 0 \\rangle$ or $| 1 \\rangle$).

Let's consider a quantum computer with $N$ qubits initially set to $| q_1 \\rangle | q_2 \\rangle .. | q_N \\rangle$. A single type of operation can be performed on these qubits: all qubits in a subarray (qubits on consecutive positions) are inverted ($| 0 \\rangle$ becomes $| 1 \\rangle$ and vice versa). Example: $| 0 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle$ becomes $| 0 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle$ if the qubits at positions $2$, $3$, and $4$ are inverted. An unfortunate characteristic of a quantum computer is that each operation introduces errors (for example, it is possible that a qubit does not invert, although it should). Therefore, it is necessary that a quantum algorithm performs as few operations as possible.

# Task

Determine the minimum number of operations necessary to set all qubits to $| 1 \\rangle$ in the following situations:

1. Operations can be performed on subarrays of any length;
2. Operations can be performed only on subarrays of length $K$.

# Input data

The input data contain on the first line two integers $C$ and $T$, separated by a space, where $C$ represents the type of task and $T$ the number of tests. The following lines contain the description of the tests.

If $C=1$ then the first line of each test contains the integer $N$, representing the number of qubits, and the second line contains $N$ characters representing the initial state of the qubits ($| 0 \\rangle$ is represented by $"0"$ and $| 1 \\rangle$ is represented by $"1"$).

If $C=2$ then the first line of each test contains two integers $N$ and $K$, separated by a space, representing the number of qubits and the length of a subarray on which an operation can be performed, and the second line contains the initial state of the qubits, described the same as for $C=1$.

# Output data

$T$ lines will be displayed, each containing the minimum number of operations necessary to set all qubits to $| 1 \\rangle$. For $C=1$ it is guaranteed that there is always a solution. For $C=2$, if there is no solution, $-1$ will be displayed.

# Constraints and clarifications

* $1 \leq T \leq 10$;
* $1 \leq K \leq N \leq 10^6$;
* The sum of the values of $N$ across all tests will not exceed $10^6$;
* Subtask $1$ ($40$p): $C = 1$;
* Subtask $2$ ($20$p): $C = 2$ and $N \leq 1\ 000$;
* Subtask $3$ ($40$p): $C = 2$.

# Example 1

`stdin`
```
1 2 
4 
0101 
7 
0010110
```

`stdout`
```
2
3
```

## Explanation

For the first test, we can achieve a minimum number of operations as follows: $| 0 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$.

For the second test, we can achieve a minimum number of operations as follows: $| 0 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle | 1 \\rangle | 0 \\rangle$ $\rightarrow$ $| 0 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$.

# Example 2

`stdin`
```
2 2 
12 4 
110100100000 
5 2 
01100
```

`stdout`
```
4
-1
```

## Explanation

For the first test, we can achieve a minimum number of operations as follows: $| 1 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle | 0 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 0 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$ $\rightarrow$ $| 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle | 1 \\rangle$.

For the second test, it can be demonstrated that there is no solution.
```