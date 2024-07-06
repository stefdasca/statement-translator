Copa knocks on the gate of Orintia, but the gate is programmed to open only after the gatekeeper calls out $s$ digits into a box with $s$ spaces. The gatekeeper called: $1$, Copa pressed $1$, in the first space from left to right. The gatekeeper called: $0$, and, while Copa was pressing $0$ in the second space, $1$ became $2$ in the previous space. The gatekeeper called: $7$. Copa wrote $7$ in the third space, and in the first space, $2$ became $3$, and in the second space, $0$ became $1$. And so on until the $s$-th space, when Copa managed to write all the digits and the entire code appeared. And the gate opened, but surprise, there was another gate, and its code, $N$, was the smallest number formed from as many of the previous code digits as possible, so that no digit was repeated.

# Task

Desperate from so much digitalization, Copa, a humble citizen of Orintia, asks for your help to calculate the second code $N$.

# Input data

The input file `orintia.in` contains on the first line $s$, the number of digits called out by the gatekeeper, then, on the following lines the $s$ digits called out, one per line.

# Output data

The output file `orintia.out` will contain $N$, the second code requested.

# Constraints and clarifications

* $3 \leq s \leq 10$;
* after $9$ follows $0$.

# Example 1

`orintia.in`
```
10
1
0
7
9
7
3
6
9
4
6
```

`orintia.out`
```
102456789
```

