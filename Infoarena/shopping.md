Shopping

K0kalaru47 has gotten into a new trouble! His friend, The Great Anonymous, has recently bought a permutation $p$ of unprecedented beauty. Being naturally curious, K0kalaru47 wants to find out the permutation. The Great Anonymous only told him that it has a length of $N$ and that $1$ appears before $2$ in the permutation $p$, and decided not to reveal any more information directly. Instead, he will answer several questions. In a question, K0kalaru47 gives The Great Anonymous two strings $A$ and $B$ of length $N$. The Great Anonymous then creates two other strings $C$ and $D$ such that $A=C_{p_1}C_{p_2}C_{p_3}\dots C_{p_N}$ and $B=D_{p_1}D_{p_2}D_{p_3}\dots D_{p_N}$. Finally, The Great Anonymous answers the question with the length of the maximal common prefix between $C$ and $D$ with at most one mismatch. Before asking The Great Anonymous a question, K0kalaru47 needs to buy the ingredients for that question. Therefore, he goes to String Shopping City and buys $2*N$ lowercase letters of the English alphabet ($N$ for string $A$ and $N$ for string $B$). It is known that the letter that appears at position $c$ in the alphabet costs $c-1$ cents. Also, the ingredients used in one question cannot be reused in another subsequent question.

## Task

Help K0kalaru47 to find the mysterious permutation without exceeding the budget of $P$ cents.

## Interaction

First, the value $T$ is read, which represents the number of tests that need to be solved. For each test, $N$ is then read, representing the length of the searched permutation. After that, your program can ask questions in the form "? $A$ $B$", where $A$ and $B$ are strings of length $N$. These questions will be written to stdout. The answer to a question can then be read from stdin. When you have found the desired permutation $p$, display "! $p_1$ $p_2$ $p_3$ $\dots$ $p_N$".

## Clarifications

Reading and displaying will be done using standard input/output. After each operation, the newline character ('\n' or endl) must be displayed and the output buffer must be flushed (using cout.flush() or fflush(stdout)). If you receive the answer $-1$ to a question, it means that the question did not follow the format described above. In this case, you must stop the interaction immediately. Infoarena offers templates for C/C++ and Rust languages that handle interactions directly, which you can find HERE. If the wrong permutation is displayed, the interactor returns $-1$ and stops the interaction.

## Constraints

- Number of tests $T$
- $N$
- $P$

## Scoring

- 1 
  - $5$
  - $8$
  - $10$
  - $1000$
  - $10p$
- 2 
  - $5$
  - $50$
  - $10$
  - $1000$
  - $10p$
- 3 
  - $5$
  - $200$
  - $2000$
  - $30p$
- 4 
  - $5$
  - $200$
  - $840$
  - $20p$
- 5 
  - $5$
  - $200$
  - $440$
  - $30p$

## Example

```
standard input (cin)
2 
4 
3 
1 
1 
4 
4 
1 
? zzzz zzab 
? abcd efca 
? cacf cbdz 
! 3 1 4 2
? aqqq azqq 
? abcc bacc 
! 1 2 3 4
```

## Explanation

In the first test, the searched permutation is $p = (3 1 4 2)$. The interaction starts by reading the value $N = 4$. In the first question, $A = zzzz$ and $B = zzab$. We have $C = zzzz$ and $D = zbza$. The longest common prefix between $C$ and $D$ with at most one mismatch is of length 3. The cost of this question is the cost of buying the letters $z$, $z$, $z$, $z$, $z$, $z$, $a$, and $b$, which is $25+25+25+25+25+25+0+1=151$. In the second question, $A = abcd$ and $B = efca$. We have $C = bdac$ and $D = faec$. The longest common prefix between $C$ and $D$ with at most one mismatch is of length 1. The cost of this question is the cost of buying the letters $a$, $b$, $c$, $d$, $e$, $f$, $c$, and $a$, which is $0+1+2+3+4+5+2+0=17$. In the third question, $A = cacf$ and $B = cbdz$. We have $C = afcc$ and $D = bzcd$. The longest common prefix between $C$ and $D$ with at most one mismatch is of length 1. The cost of this question is the cost of buying the letters $c$, $a$, $c$, $f$, $c$, $b$, $d$, and $z$, which is $2+0+2+5+2+1+3+25=40$. The total cost for solving the first test is $151 + 17 + 40 = 208$. The interaction will continue by reading the value $N = 4$ corresponding to the next test.