Fie $n$ un număr natural nenul și un șir de $n$ numere naturale nenule, fiecare număr din șir având cel mult $3$ cifre. Șirul dat se „maximizează” prin aplicarea următoarelor transformări:

$T1$: Fiecare număr $y$ din șir este înlocuit cu cel mai mare număr care se poate obține prin aranjarea tuturor cifrelor lui $y$. De exemplu, pentru $y = 102$, prin aranjarea cifrelor, se obțin numerele: $12$, $21$, $102$, $120$, $201$, $210$, cel mai mare număr fiind $210$. Astfel, $y$ se va înlocui în șir cu numărul $210$.
$T2$: Se schimbă ordinea numerelor din șirul obținut după aplicarea transformării $T1$ astfel încât numărul $x$ obținut prin alipirea tuturor numerelor din șir, în ordinea în care apar după schimbare, să fie cel mai mare posibil.

De exemplu, pentru $n = 3$ și șirul: $12$, $132$, $102$, după aplicarea transformării $T1$ noul șir este format din numerele: $21$, $321$, $210$. Din acest șir, se pot obține, prin schimbarea ordinii numerelor, următoarele $6$ șiruri:

1) $21$, $321$, $210$
2) $21$, $210$, $321$ 
3) $321$, $21$, $210$
4) $321$, $210$, $21$
5) $210$, $21$, $321$
6) $210$, $321$, $21$

Numerele care rezultă prin alipirea numerelor din fiecare șir obținut sunt:

1) $21321210$
2) $21210321$
3) $32121210$
4) $32121021$
5) $21021321$
6) $21032121$

După aplicarea transformării $T2$, șirul „maximizat” este: $321, \\ 21, \\ 210$ deoarece cel mai mare număr dintre cele $6$ obținute este $x = 32121210$.

# Task

Write a program that reads the non-zero natural number $n$ and the $n$ non-zero natural numbers from the sequence and determines:

1. the largest number $m$ in the sequence of numbers obtained after applying transformation $T1$;
2. the number $x$ obtained by concatenating the numbers from the "maximized" sequence resulting from applying transformation $T2$.

# Input data

The input file `max.in` contains two lines. The first line contains the non-zero natural number $n$, and the second line contains the $n$ non-zero natural numbers from the sequence, separated by a space.

# Output data

The output file `max.out` will contain:

* on the first line the natural number $m$, representing the largest number in the sequence of numbers obtained after applying transformation $T1$.
* on the second line the natural number $x$, representing the number obtained by concatenating the numbers from the "maximized" sequence resulting from applying transformation $T2$.

# Constraints and clarifications

* The number $n$ is a natural number, $2 \leq n \leq 3 \ 500$
* The $n$ numbers in the read sequence are non-zero natural numbers, each number in the sequence having at most $3$ digits
* If a number in the sequence has at least one zero digit and by arranging the digits of this number, another number is obtained that has the first digit $0$, then this digit is ignored
* The determined natural number $x$ can have at most $10 \ 500$ digits
* Partial scores are awarded: for task $1$, $20\\%$ of the score, for task $2$, $80\\%$ of the score

# Example

`max.in`

```
9
34 23 9 43 21 67 121 79 213
```

`max.out`

```
321
9977643433232121211
```

## Explanation

After applying transformation $T1$, the sequence becomes: $43, \\ 32, \\ 9, \\ 43, \\ 21, \\ 76, \\ 211, \\ 97, \\ 321$. The largest number in this sequence is $m = 321$. After applying transformation $T2$, the maximized sequence is: $9, \\ 97, \\ 76, \\ 43, \\ 43, \\ 32, \\ 321, \\ 21, \\ 211$ and the number $x = 9977643433232121211$