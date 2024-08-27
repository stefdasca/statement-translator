## Task

Given an $NFA$ (nondeterministic finite automaton) with $N$ states, $M$ transitions, and $K$ final states, where each transition involves a lowercase letter from the English alphabet, determine for $Q$ words whether each is accepted by the automaton. Output $1$ for acceptance and $0$ otherwise.

## Input data

The input file `nfa.in` will contain:
- The first line will contain 3 numbers $N$, $M$, and $K$ (as described above).
- The second line will contain a number $S$, representing the initial state.
- The third line will contain $K$ numbers representing the final states.
- The following $M$ lines will contain 2 numbers and a character representing a transition between 2 states.
- The next line will contain a number $Q$, followed by $Q$ lines, each with a string of characters.

## Output data

The output file `nfa.out` will contain $Q$ lines, each containing a number $0$ or $1$, where the $i$-th value represents the acceptance of the $i$-th string.

## Constraints and clarifications

$1 \leq N \leq 300$

$1 \leq M \leq 1200$

$1 \leq Q \leq 50$

The length of the words is less than $150$.

For $20$ points:

$1 \leq N \leq 10$
$1 \leq M \leq 40$
$1 \leq Q \leq 5$
The length of the words is less than $20$.

For another $30$ points:

$1 \leq N \leq 50$
$1 \leq M \leq 200$
The length of the words is less than $100$.

For another $30$ points:

$1 \leq N \leq 100$
$1 \leq M \leq 400$

The given $NFA$ has only one initial state.

## Example

`nfa.in`

$5$ $5$ $2$

$3$

$2$ $5$

$3$ $1$ $a$

$1$ $2$ $b$

$2$ $1$ $a$

$3$ $5$ $a$

$5$ $4$ $d$

$7$

`ab`

`aba`

`abab`

`ad`

`nuchichi`

`a`

`dausu`

`nfa.out`

$1$

$0$

$1$

$0$

$0$

$1$

$0$

## Explanation

Informally, you need to find a traversal in the given graph starting from the source and reaching a final state; the letters on the edges must match the word (the $i$-th edge must have the $i$-th letter of the word).