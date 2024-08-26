## Task

You have a friend who is currently taking a course in Finite Automata and talks about it all the time. For a long time, you thought it wasn't a very legitimate course, because your friend talked about automata that "tolerate" words, whereas we all know that the established formulation is "accept". However, today your friend defined "tolerance" more precisely to you and, indeed, it is relatively interesting. We say that a Deterministic Finite Automaton (abbreviated as $DFA$) tolerates string $X$ if and only if there exists a string $Y$ such that $X$ is a subsequence of $Y$, and $Y$ is accepted by the $DFA$ in the classical sense. Given a $DFA$, you are curious about how dense the set of tolerated strings of this $DFA$ is relative to the set of all strings over the automaton's alphabet. More formally, you are curious if the limit of the ratio between the number of tolerated strings and the number of all possible strings (which, for a certain fixed length $L$, is equal to $SIGMA^L$) when the length tends to infinity is strictly positive.

## Input data

The input file `density.in` will contain on its first line the number of tests, $T$. The structure of a test is as follows: The first line will contain the values $N \ SIGMA \ F$, representing the number of states of the automaton, the size of the alphabet used by the automaton, and the number of final states of the automaton, respectively. It is followed by a line with $F$ distinct values from the set $\{1, 2, \dots, N\}$, representing the set of final states of the automaton. Then follow $N$ lines, each containing $SIGMA$ values from the set $\{1, 2, \dots, N\}$. The $j$-th element on line $i$ indicates the destination of the transition associated with the character number $j$ from state $i$.

## Output data

The output file `density.out` will contain $T$ lines, each containing the answer for the corresponding test. If the limit described in the statement is strictly greater than $0$, the answer is "YES". Otherwise, the answer is "NO".

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq N \leq 10\ 000$

$1 \leq SIGMA \leq 26$

The starting state is always state number $1$. 

For 90 tests $1 \leq N \leq 1\ 000$.

## Example

`density.in`

```
2
1 1 1
1
1
3 1 2
1 2
1 2
2 3
3
```

`density.out`

```
YES
NO
```

## Explanation

The first automaton tolerates any string formed from the first and only character of the alphabet. Thus its density is $1$. In the case of the second automaton, the alphabet is the same, but the automaton only tolerates strings of length less than or equal to $2$. It is clear that its density is $0$.