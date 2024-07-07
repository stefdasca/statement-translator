Administratorul rețelei cu $N$ calculatoare de la SRI împarte, din motive strategice, aceste calculatoare în mai multe grupuri. De fapt, important este doar numărul de grupuri și numărul de calculatoare din fiecare grup, așa că împărțirea este descrisă prin șirul numerelor de calculatoare din fiecare grup, ordonat crescător.

Periodic, el procedează la o nouă împărțire pe grupe a calculatoarelor. Dintre toate împărțirile posibile ale calculatoarelor în grupuri putem alege ca următoare împărțire doar aceea a cărei descriere precede sau succede lexicografic imediat împărțirii curente.

Nota: Spunem că șirul $x_1 x_2 \ldots x_p$ precede lexicografic șirul $y_1 y_2 \ldots y_k$ dacă:

* există un indice $j$, astfel încât $x_i=y_i$ pentru toți indicii $i<j$ și $x_j<y_j$

**SAU**

* $p<k$ și $x_i=y_i$ pentru toți indicii $i \leq p$

Exemple:

* $3 \\ 7 \\ \\textbf{2} \\ 5 $ precede lexicografic $3 \\ 7 \\ \\textbf{4} \\ 1 \\ 6 \\ 2$
* $\\textbf{1} \\ 2 \\ 3 $ precede lexicografic $\\textbf{2}$


# Task

Given a distribution of the $N$ computers into groups, determine the two candidate variations for the next distribution.

# Input data

Input file: `grup.in`

Line $1$: $N$, $k$, natural non-zero numbers, representing the total number ($N$) of computers in the network and the number ($k$) of groups.

Line $2$: $g_1$, $g_2$, $\\dots$, $g_k$, the number of computers in each group.

# Output data

Output file: `grup.out`

Line $1$ contains $p$, the number of groups in the immediately lexicographically preceding distribution;

Line $2$ contains $h_1$, $h_2$, $\\dots$, $h_p$, the number of computers in the $p$ groups of the preceding distribution;

Line $3$ contains $u$, the number of groups in the immediately lexicographically succeeding distribution;

Line $4$ contains $t_1$, $t_2$, $\\dots$, $t_u$, the number of computers in the $u$ groups of the succeeding distribution.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$
* $g_1 + g_2+ \ldots + g_k = h_1 + h_2 + \ldots + h_p = t_1 + t_2 + \ldots + t_u = N$
* $1 \leq g_1 \leq g_2 \leq \ldots \leq g_k \text{;} 1 \leq h_1 \leq h_2 \leq \ldots \leq h_p \text{;} 1 \leq t_1 \leq t_2 \leq \ldots \leq t_u$;
* $1 < k < N$
* $1 \leq p, u \leq N$

# Example

`grup.in`
```
14 3
2 6 6
```

`grup.out`
```
3
2 5 7
2
2 12
